<template>
	<v-app id="app">
		<v-main class="grey lighten-2">
			<v-container fluid fill-height>
				<v-layout align-center justify-center>
					<v-flex align-self-center xs12 sm10 md6 lg4 xl3>
						<v-sheet
							class="pa-8"
							elevation="20"
							min-height="60vh"
							rounded="lg"
							color="rgba(255,255,255,0.85)"
						>
							<nuxt />
						</v-sheet>
					</v-flex>
				</v-layout>
			</v-container>
		</v-main>
	</v-app>
</template>

<script>
export default {
	components: {},
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
