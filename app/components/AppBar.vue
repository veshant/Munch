<template>
	<div>
		<v-app-bar app color="white" flat class="">
			<v-app-bar-nav-icon
				class="d-md-none"
				@click="drawer = true"
			></v-app-bar-nav-icon>
			<div class="mx-auto" style="height: inherit">
				<nuxt-link to="/">
					<v-img
						class="mx-2"
						src="/logo.png"
						max-width="200"
						height="100%"
						contain
					></v-img
				></nuxt-link>
			</div>

			<SearchBar class="d-none d-md-block mx-6" style="width: 420px" />
			<v-tabs centered class="d-none d-md-block" color="grey darken-1">
				<v-tab v-for="link in links" :key="link">
					{{ link }}
				</v-tab>
			</v-tabs>

			<v-menu offset-y>
				<template #activator="{ on, attrs }">
					<v-avatar
						class=""
						color="primary"
						size="32"
						v-bind="attrs"
						v-on="on"
					>
						<v-icon dark>mdi-account-circle</v-icon>
					</v-avatar>
				</template>
				<v-list width="160px">
					<template v-if="$store.state.auth.loggedIn">
						<v-list-item>
							<v-list-item-title>Profile</v-list-item-title>
						</v-list-item>
						<v-list-item @click="logout">
							<v-list-item-title>Logout</v-list-item-title>
						</v-list-item>
					</template>
					<template v-else>
						<v-list-item to="/auth/login">
							<v-list-item-title>Login</v-list-item-title>
						</v-list-item>
					</template>
				</v-list>
			</v-menu>
		</v-app-bar>
		<v-navigation-drawer
			v-model="drawer"
			absolute
			temporary
			class="deep-orange accent-2"
			dark
		>
			<SearchBar class="ma-2" />
			<v-list nav dense>
				<v-list-item-group
					v-model="group"
					active-class="deep-purple--text text--accent-4"
				>
					<v-list-item>
						<v-list-item-icon>
							<v-icon>mdi-home</v-icon>
						</v-list-item-icon>
						<v-list-item-title>Home</v-list-item-title>
					</v-list-item>

					<v-list-item>
						<v-list-item-icon>
							<v-icon>mdi-account</v-icon>
						</v-list-item-icon>
						<v-list-item-title>Account</v-list-item-title>
					</v-list-item>
				</v-list-item-group>
			</v-list>
		</v-navigation-drawer>
	</div>
</template>
<script>
export default {
	name: 'AppBar',
	data: () => ({
		links: ['Dashboard', 'Messages', 'Profile', 'Check In'],
		items: [{ title: 'Profile' }, { title: 'Logout' }],
		drawer: false,
		group: null,
	}),
	methods: {
		async logout() {
			await this.$auth.logout()
		},
	},
}
</script>
