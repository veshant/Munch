"""
This file defines actions, i.e. functions the URLs are mapped into
The @action(path) decorator exposed the function at URL:

	http://127.0.0.1:8000/{app_name}/{path}

If app_name == '_default' then simply

	http://127.0.0.1:8000/{path}

If path == 'index' it can be omitted:

	http://127.0.0.1:8000/

The path follows the bottlepy syntax.

@action.uses('generic.html')  indicates that the action uses the generic.html template
@action.uses(session)		 indicates that the action uses the session
@action.uses(db)			  indicates that the action uses the db
@action.uses(T)			   indicates that the action uses the i18n & pluralization
@action.uses(auth.user)	   indicates that the action requires a logged in user
@action.uses(auth)			indicates that the action requires the auth object

session, db, T, auth, and tempates are examples of Fixtures.
Warning: Fixtures MUST be declared with @action.uses({fixtures}) else your app will result in undefined behavior
"""


import datetime
import json
import os
import traceback
import uuid

from nqgcs import NQGCS

from py4web import action, request, abort, redirect, URL, Field, Flash
from py4web.utils.form import Form, FormStyleBulma
from yatl.helpers import A
from .common import db, session, T, cache, auth, logger, authenticated, unauthenticated, flash
from pydal.restapi import RestAPI, Policy
from py4web.utils.url_signer import URLSigner
from .models import get_user_email, get_user_id
from .settings import APP_FOLDER
from py4web.utils.auth import Auth
from .gcs_url import gcs_url

BUCKET = '/munch-images'
GCS_KEY_PATH = os.path.join(APP_FOLDER, 'private/gcs_keys.json')
with open(GCS_KEY_PATH) as gcs_key_f:
    GCS_KEYS = json.load(gcs_key_f)

gcs = NQGCS(json_key_path=GCS_KEY_PATH)

auth = Auth(session, db)
# (configure here)
auth.enable()

policy = Policy()
#policy.set('business', 'GET', authorize=False, allowed_patterns=['*'])
policy.set('*', 'GET', authorize=False, allowed_patterns=['*'])

# for security reasons we disabled here all methods but GET at the policy level, to enable any of them just set authorize = True
policy.set('*', 'PUT', authorize=False)
policy.set('*', 'POST', authorize=False)
policy.set('*', 'DELETE', authorize=False)


# Login Controller
@action('addUsertoList/<tablename>/<column>/<rec_id>', method = ['PUT', 'DELETE'])
@action.uses(db, auth.user)
def api_list(tablename, column, rec_id):
    user = get_user_id()
    assert user is not None
    assert request.json is not None
    method = request.method
    row = db(db[tablename].id == rec_id).select().first()
    column_val = row[column]
    if request.method == 'PUT' :
        if column_val is not None :
            column_val.append(user)
        else :
            column_val = [user]
        
    if request.method == 'DELETE' :
        method = 'PUT'
        column_val.remove(user)
        
    request.json[column] = column_val
    
    return RestAPI(db, policy)(method,
                               tablename,
                               rec_id,
                               request.GET,
                               request.json
                               )
                             
@action('obtain_gcs', method="POST")
@action.uses(db)
def obtain_gcs():
    user = get_user_id()
    #assert user is not None
    """Returns the URL to do download / upload / delete for GCS."""
    verb = request.json.get("action")
    if verb == "PUT":
        mimetype = request.json.get("mimetype", "")
        file_name = request.json.get("file_name")
        extension = os.path.splitext(file_name)[1]
        # Use + and not join for Windows, thanks Blayke Larue
        file_path = BUCKET + "/" + str(uuid.uuid1()) + extension
        # Marks that the path may be used to upload a file.
        mark_possible_upload(file_path)
        upload_url = gcs_url(GCS_KEYS, file_path, verb='PUT',
                             content_type=mimetype)
        return dict(
            signed_url=upload_url,
            file_path=file_path
        )
    elif verb in ["GET", "DELETE"]:
        file_path = request.json.get("file_path")
        if file_path is not None:
            # We check that the file_path belongs to the user.
            r = db(db.upload.file_path == file_path).select().first()
            if r is not None and r.owner == get_user_email():
                # Yes, we can let the deletion happen.
                delete_url = gcs_url(GCS_KEYS, file_path, verb='DELETE')
                return dict(signed_url=delete_url)
        # Otherwise, we return no URL, so we don't authorize the deletion.
        return dict(signer_url=None)
        
@action('notify_upload', method="POST")
@action.uses(db)
def notify_upload():
    """We get the notification that the file has been uploaded."""
    file_type = request.json.get("file_type")
    file_name = request.json.get("file_name")
    file_path = request.json.get("file_path")
    file_size = request.json.get("file_size")
    print("File was uploaded:", file_path, file_name, file_type)
    # Marks the upload as confirmed.
    d = datetime.datetime.utcnow()
    db.upload.update_or_insert(
        ((db.upload.owner == get_user_email()) &
         (db.upload.file_path == file_path)),
        owner=get_user_email(),
        file_path=file_path,
        file_name=file_name,
        file_type=file_type,
        file_date=d,
        file_size=file_size,
        confirmed=True,
    )
    # Returns the file information.
    return dict(
        download_url=gcs_url(GCS_KEYS, file_path, verb='GET'),
        file_date=d,
    )

def mark_possible_upload(file_path):
    """Marks that a file might be uploaded next."""
    db.upload.insert(
        owner=get_user_email(),
        file_path=file_path,
        confirmed=False,
    )



@action('<tablename>/', method = ['GET', 'POST'])
@action('<tablename>/<rec_id>', method = ['GET', 'PUT', 'DELETE'])
@action.uses(db, auth.user)
def api(tablename, rec_id=None):
    policy.set('business', 'GET', authorize=True, allowed_patterns=['*'])
    policy.set('menu', 'GET', authorize=True, allowed_patterns=['*'])
    policy.set('menu_section', 'GET', authorize=True, allowed_patterns=['*'])
    policy.set('menu_item', 'GET', authorize=True, allowed_patterns=['*'])
    
    if request.method in ['POST', 'PUT', 'DELETE']:
        user = get_user_id()
        assert user is not None
    
        if tablename == 'business' :
            business = db(db.business.id == rec_id).select().first()
        if tablename == 'menu' :
            menu = db(db.menu.id == rec_id).select().first()
            business = db(db.business.id == menu.business).select().first()
        if tablename == 'menu_section' :
            menu_section = db(db.menu_section.id == rec_id).select().first()
            menu = db(db.menu.id == menu_section.menu).select().first()
            business = db(db.business.id == menu.business).select().first()
        if tablename == 'menu_item' :
            menu_item = db(db.menu_item.id == rec_id).select().as_list()[0]
            menu_section = db(db.menu_section.id == menu_item["menu_section"]).select().as_list()[0]
            menu = db(db.menu.id == menu_section["menu"]).select().as_list()[0]
            business = db(db.business.id == menu["business"]).select().as_list()[0]
        
        if user in business["editors"] :
            policy.set('business', 'POST', authorize=True)
            policy.set('menu', 'POST', authorize=True)
            policy.set('menu_section', 'POST', authorize=True)
            policy.set('menu_item', 'POST', authorize=True)
            policy.set('business', 'PUT', authorize=True)
            policy.set('menu', 'PUT', authorize=True)
            policy.set('menu_section', 'PUT', authorize=True)
            policy.set('menu_item', 'PUT', authorize=True)
    
    # Check user owns record in database and set policy
    return RestAPI(db, policy)(request.method,
                               tablename,
                               rec_id,
                               request.GET,
                               request.json
                               )
                               
