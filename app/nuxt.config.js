import colors from 'vuetify/es5/util/colors'

export default {
	server: {
		host: '0.0.0.0', // default: localhost
	},
	// Global page headers: https://go.nuxtjs.dev/config-head
	head: {
		titleTemplate: '%s - app',
		title: 'Munch',
		meta: [
			{ charset: 'utf-8' },
			{
				name: 'viewport',
				content: 'width=device-width, initial-scale=1',
			},
			{ hid: 'description', name: 'description', content: '' },
		],
		link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }],
	},

	// Global CSS: https://go.nuxtjs.dev/config-css
	css: [],

	// Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
	plugins: [],

	// Auto import components: https://go.nuxtjs.dev/config-components
	components: true,

	// Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
	buildModules: [
		// https://go.nuxtjs.dev/typescript
		'@nuxt/typescript-build',
		// https://go.nuxtjs.dev/vuetify
		'@nuxtjs/vuetify',
		'@nuxtjs/moment',
	],

	// Modules: https://go.nuxtjs.dev/config-modules
	modules: [
		// https://go.nuxtjs.dev/axios
		'@nuxtjs/axios',
		// https://go.nuxtjs.dev/pwa
		'@nuxtjs/pwa',
		// https://go.nuxtjs.dev/content
		'@nuxt/content',

		'@nuxtjs/auth-next',
		'@nuxtjs/proxy',
	],

	// Axios module configuration: https://go.nuxtjs.dev/config-axios
	axios: {
		baseURL: '/',
		proxy: true,
		credentials: true,
	},

	proxy: {
		'/api/': {
			target: 'https://api.letsmunch.app/',
			pathRewrite: { '^/api/': '' },
			changeOrigin: true,
		},
	},

	auth: {
		strategies: {
			cookie: {
				cookie: {
					name: '_default_session',
				},
				endpoints: {
					csrf: {
						url: '',
					},
					login: {
						url: '/api/auth/api/login',
						method: 'post',
					},
					logout: {
						url: '/api/auth/api/logout',
						method: 'post',
					},
					user: {
						url: '/api/auth/api/profile',
						method: 'get',
					},
				},
				user: {
					property: 'user',
					autoFetch: true,
				},
			},
		},
	},

	// PWA module configuration: https://go.nuxtjs.dev/pwa
	pwa: {
		manifest: {
			lang: 'en',
		},
	},

	// Content module configuration: https://go.nuxtjs.dev/config-content
	content: {},

	// Vuetify module configuration: https://go.nuxtjs.dev/config-vuetify
	vuetify: {
		customVariables: ['~/assets/variables.scss'],
		theme: {
			dark: false,
			themes: {
				light: {
					primary: '#1976D2',
					secondary: '#424242',
					accent: '#82B1FF',
					error: '#FF5252',
					info: '#2196F3',
					success: '#4CAF50',
					warning: '#FFC107',
					google: '#ED1C24',
					facebook: '#1877F2',
					twitter: '#1DA1F2',
					microsoft: '#737373',
				},
				dark: {
					primary: colors.blue.darken2,
					accent: colors.grey.darken3,
					secondary: colors.amber.darken3,
					info: colors.teal.lighten1,
					warning: colors.amber.base,
					error: colors.deepOrange.accent4,
					success: colors.green.accent3,
				},
			},
		},
	},

	// Build Configuration: https://go.nuxtjs.dev/config-build
	build: {
		loaders: {
			vue: {
				prettify: false,
			},
		},
	},
}
