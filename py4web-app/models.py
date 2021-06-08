"""
This file defines the database models
"""

import datetime
from .common import db, Field, auth
from pydal.validators import *
import uuid


def get_user_email():
    return auth.current_user.get('email') if auth.current_user else None
    
def get_user_id():
    return auth.current_user.get('id') if auth.current_user else None

def get_time():
    return datetime.datetime.utcnow()


### Define your table below
#
# db.define_table('thing', Field('name'))
#
## always commit your models to avoid problems later

db.define_table(
	'settings',
    Field('admins', 'reference auth_user'),
	Field('created_by', default=get_user_email),
	Field('created_time', 'datetime', default=get_time),
)

db.define_table(
	'business',
    Field('uuid', length=64),
	Field('name'),
	Field('slug', unique=True),
	Field('description', 'text'),
	Field('rating', 'decimal(2,2)'),
	Field('categories', 'list:string'),
	Field('open_time', 'time'),
	Field('close_time', 'time'),
	Field('price_range', 'integer'),
    Field('editors', 'list:reference auth_user', default=[]),
	Field('created_by', default=get_user_email),
	Field('created_time', 'datetime', default=get_time),
)

db.define_table(
	'menu',
	Field('name'),
	Field('slug'),
	Field('business', 'reference business'),
	Field('created_by', default=get_user_email),
	Field('created_time', 'datetime', default=get_time),
)

db.define_table(
	'menu_section',
	Field('name'),
	Field('slug'),
	Field('menu', 'reference menu'),
	Field('created_by', default=get_user_email),
	Field('created_time', 'datetime', default=get_time),
)

db.define_table(
	'menu_item',
	Field('name'),
	Field('description', 'text'),
	Field('tag'),
    Field('image'),
	Field('price', 'decimal(3,2)'),
	Field('menu_section', 'reference menu_section'),
    Field('favorites', 'list:reference auth_user', default=[]),
	Field('created_by', default=get_user_email),
	Field('created_time', 'datetime', default=get_time),
)

db.define_table(
	'cart',
    Field('menu_item', 'reference menu_item'),
    Field('business', 'reference business'),
    Field('quantity', 'integer'),
    Field('ordered', 'boolean'),
    Field('paid', 'boolean'),
	Field('created_by', default=get_user_email),
	Field('created_time', 'datetime', default=get_time),
)

db.define_table(
    'upload',
    Field('file_name'),
    Field('file_type'),
    Field('file_date'),
    Field('file_path'),
    Field('file_size', 'integer'),
    Field('owner', default=get_user_email),
    Field('confirmed', 'boolean', default=False), # Was the upload to GCS confirmed?
)


db.menu_item.favorites.requires = IS_IN_DB(db, 'auth_user.id', multiple=True)

#db.birds.id.readable = db.birds.id.writable = False
#db.birds.created_by.readable = db.birds.created_by.writable = False
#db.birds.created_time.readable = db.birds.created_time.writable = False

#db.birds.bird.requires = [IS_NOT_EMPTY(), IS_NOT_IN_DB(db, 'birds.bird')]

db.commit()
