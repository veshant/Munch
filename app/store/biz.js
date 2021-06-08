import axios from 'axios'
import moment from 'moment'

// State
export const state = () => ({
	business: {
		'business.menu': [],
		categories: '',
		close_time: '',
		created_by: '',
		created_time: '',
		id: 0,
		name: '',
		open_time: '',
		price_range: 0,
		rating: 0,
		slug: '',
	},
	menus: [],
	menu: {
		business: 0,
		id: 0,
		sections: [{ id: 0, items: [] }],
		name: '',
		slug: '',
	},
	editor: false,
	images: [],
})

// Getters
export const getters = {}

// Actions
export const actions = {
	loadBiz({ commit, rootState }, slug) {
		return new Promise((resolve) => {
			axios
				.get(
					'/api/business?slug.eq=' +
						slug +
						'&@lookup=menu:business.menu'
				)
				.then((response) => {
					commit('setBiz', {
						business: response.data.items[0],
						rootState,
					})
					resolve(response.data.items[0])
				})
		})
	},
	loadMenu({ commit }, { slug, menu }) {
		return new Promise((resolve) => {
			axios
				.get(
					'/api/menu?business.slug.eq=' +
						slug +
						'&slug.eq=' +
						menu +
						'&@lookup=sections:menu.menu_section'
				)
				.then((response) => {
					commit('setMenu', response.data.items[0])
					resolve(response.data.items[0])
				})
		})
	},
	loadItems({ commit, state, rootState }, id) {
		return new Promise((resolve) => {
			for (const element of state.menu.sections) {
				if (element.id === id) {
					if (element.items_loaded) break
					axios
						.get(
							'/api/menu_section?id.eq=' +
								id +
								'&@lookup=items:menu_section.menu_item'
						)
						.then((response) => {
							commit('setItems', {
								response,
								rootState,
								section: id,
								items: response.data.items[0].items,
							})
							resolve(response.data.items[0])
						})
					break
				} else {
					resolve(element.items)
				}
			}
		})
	},
	addMenu({ commit }, { business, menu }) {
		return new Promise((resolve, reject) => {
			axios
				.post('/api/menu', {
					business: business.id,
					name: menu.name,
					slug: menu.slug,
				})
				.then((response) => {
					if (response.data.code === 200) {
						commit('addMenu', {
							response,
							business,
							menu,
						})
						resolve(response.data)
					} else {
						reject(response.data)
					}
				})
		})
	},
	editMenu({ commit }, { business, menu }) {
		return new Promise((resolve, reject) => {
			axios
				.put('/api/menu/' + menu.id, {
					name: menu.name,
					slug: menu.slug,
				})
				.then((response) => {
					if (response.data.code === 200) {
						commit('editMenu', {
							response,
							business,
							menu,
						})
						resolve(response.data)
					} else {
						reject(response.data)
					}
				})
		})
	},
	addBiz({ commit, rootState }, { business }) {
		return new Promise((resolve, reject) => {
			axios
				.post('/api/business', {
					name: business.name,
					slug: business.slug,
					description: business.description,
					rating: business.rating,
					price_range: business.price_range,
					categories: business.categories,
					open_time: business.open_time,
					close_time: business.close_time,
					editors: [rootState.auth.user.id],
				})
				.then((response) => {
					if (response.data.code === 200) {
						resolve(response.data)
					} else {
						reject(response.data)
					}
				})
		})
	},
	editBiz({ commit }, { business }) {
		return new Promise((resolve, reject) => {
			axios
				.put('/api/business/' + business.id, {
					name: business.name,
					slug: business.slug,
					description: business.description,
					rating: business.rating,
					price_range: business.price_range,
					categories: business.categories,
					open_time: business.open_time,
					close_time: business.close_time,
				})
				.then((response) => {
					if (response.data.code === 200) {
						resolve(response.data)
					} else {
						reject(response.data)
					}
				})
		})
	},
	addSection({ commit }, { section, menu }) {
		return new Promise((resolve, reject) => {
			axios
				.post('/api/menu_section', {
					menu: menu.id,
					name: section.name,
				})
				.then((response) => {
					if (response.data.code === 200) {
						commit('addSection', {
							response,
							section,
							menu,
						})
						resolve(response.data)
					} else {
						reject(response.data)
					}
				})
		})
	},
	addItem({ commit }, { item, section }) {
		return new Promise((resolve, reject) => {
			axios
				.post('/api/menu_item', {
					menu_section: section.id,
					name: item.name,
					description: item.description,
					tag: item.tag,
				})
				.then((response) => {
					if (response.data.code === 200) {
						commit('addItem', {
							response,
							item,
							section,
						})
						resolve(response.data)
					} else {
						reject(response.data)
					}
				})
		})
	},
	setFav({ commit, rootState }, { item, menu, section }) {
		return new Promise((resolve, reject) => {
			axios
				.put('/api/addUsertoList/menu_item/favorites/' + item.id, {})
				.then((response) => {
					if (response.data.code === 200) {
						commit('setFav', {
							response,
							item,
							section,
						})
						resolve(response.data)
					} else {
						reject(response.data)
					}
				})
		})
	},
	unsetFav({ commit, rootState }, { item, menu, section }) {
		return new Promise((resolve, reject) => {
			axios
				.delete('/api/addUsertoList/menu_item/favorites/' + item.id, {
					data: {},
				})
				.then((response) => {
					if (response.data.code === 200) {
						commit('unsetFav', {
							response,
							item,
							section,
						})
						resolve(response.data)
					} else {
						reject(response.data)
					}
				})
		})
	},
	uploadImage({ commit, rootState }, { file }) {
		return new Promise((resolve, reject) => {
			this.loading = true
			axios
				.post('/api/obtain_gcs', {
					action: 'PUT',
					mimetype: file.type,
					file_name: file.name,
				})
				.then((res) => {
					const req = new XMLHttpRequest()
					req.addEventListener('load', () => {
						axios
							.post('/api/notify_upload', {
								file_name: file.name,
								file_type: file.type,
								file_path: res.data.file_path,
								file_size: file.size,
							})
							.then((response) => {
								resolve(response)
							})
					})
					req.open('PUT', res.data.signed_url, true)
					req.send(file)
				})
		})
	},
}

// Mutations
export const mutations = {
	setBiz(state, { business, rootState }) {
		business.open_time = moment(business.open_time, 'hh:mm:ss').format('LT')
		business.close_time = moment(business.close_time, 'hh:mm:ss').format(
			'LT'
		)
		business.open = moment().isBetween(
			moment(business.open_time, 'hh:mm:ss'),
			moment(business.close_time, 'hh:mm:ss')
		)
		business.open_class = business.open ? 'teal' : 'red'

		state.menus = [
			{
				title: 'About',
				link: '/biz/' + business.slug + '/',
				class: 'font-weight-bold text-button',
			},
		]
		business.menu.forEach((element) => {
			state.menus.push({
				title: element.name,
				link: '/biz/' + business.slug + '/menu/' + element.slug,
				id: element.id,
				name: element.name,
				slug: element.slug,
			})
		})

		business.editors = [8] // REMOVE THIS LINE
		if (rootState.auth.user && business.editors)
			state.editor = business.editors.includes(rootState.auth.user.id)
		delete business.editors

		state.business = business
	},
	setMenu(state, menu) {
		for (const section of menu.sections) {
			section.items = []
		}
		state.menu = menu
	},
	setItems(state, { rootState, section, items }) {
		items.forEach((item) => {
			item.favorite = false
			if (rootState.auth.user && item.favorites)
				item.favorite = item.favorites.includes(rootState.auth.user.id)
			delete item.favorites
		})
		for (const element of state.menu.sections) {
			if (element.id === section) {
				element.items = items
				element.items_loaded = true
				return
			}
		}
	},
	addMenu(state, { business, menu }) {
		state.menus.push({
			link: '/biz/' + business.slug + '/menu/' + menu.slug,
			title: menu.name,
		})
	},
	editMenu(state, { business, menu }) {
		for (const i in state.menus) {
			if (state.menus[i].id === menu.id) {
				state.menus[i].link =
					'/biz/' + business.slug + '/menu/' + menu.slug
				state.menus[i].name = menu.name
				state.menus[i].slug = menu.slug
				state.menus[i].title = menu.name
			}
		}
	},
	addSection(state, { response, section, menu }) {
		state.menu.sections.push({
			id: response.data.id,
			items: [],
			items_loaded: true,
			menu: menu.id,
			name: section.name,
			slug: section.slug,
		})
	},
	addItem(state, { response, item, section }) {
		for (const elem of state.menu.sections) {
			if (elem.id === section.id) {
				elem.items.push({
					id: response.data.id,
					name: item.name,
					description: item.description,
					tag: item.tag,
					menu_section: section.id,
				})
				break
			}
		}
	},
	setFav(state, { response, item, section }) {
		for (const elem of state.menu.sections) {
			if (elem.id === section.id) {
				for (const itemElem of elem.items) {
					if (itemElem.id === item.id) {
						itemElem.favorite = true
						break
					}
				}
				break
			}
		}
	},
	unsetFav(state, { response, item, section }) {
		for (const elem of state.menu.sections) {
			if (elem.id === section.id) {
				for (const itemElem of elem.items) {
					if (itemElem.id === item.id) {
						itemElem.favorite = false
						break
					}
				}
				break
			}
		}
	},
}
