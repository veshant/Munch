<template>
	<v-app id="app">
		<AppBar />
		<v-main class="grey lighten-2">
			<v-container fluid fill-height>
				<v-layout align-center justify-center>
					<v-flex align-self-center xs12 sm10 md8 lg6 xl4>
						<v-sheet
							class="pa-8"
							elevation="20"
							min-height="20vh"
							rounded="lg"
							color="deep-orange lighten-1"
						>
							<nuxt />
						</v-sheet>
					</v-flex>
				</v-layout>
			</v-container>
		</v-main>
		<Footer />
	</v-app>
</template>

<script>
import AppBar from '@/components/AppBar'
import Footer from '@/components/Footer'
export default {
	components: {
		AppBar,
		Footer,
	},
	data: () => ({}),
}
</script>

<style scoped>
.v-main {
	background-image: url('/background.jpg') !important;
	background-size: cover;
	background-position: bottom center;
	min-height: inherit;
}
</style>
