<template>
	<div class="text-center">
		<span class="text-h3">Login</span>
		{{ this.$store.state.auth.user }}
		<v-form>
			<v-container>
				<v-text-field
					v-model="login.email"
					label="E-mail"
					required
				></v-text-field>
				<v-text-field
					v-model="login.password"
					:append-icon="showPass ? 'mdi-eye' : 'mdi-eye-off'"
					:type="showPass ? 'text' : 'password'"
					name="input-10-1"
					label="Password"
					hint="At least 8 characters"
					counter
					@click:append="showPass = !showPass"
				></v-text-field>
				<v-btn block outlined class="mt-4" @click="userLogin">
					Login
				</v-btn>
			</v-container>
		</v-form>

		<v-divider class="ma-4"></v-divider>

		<span class="text-subtitle">Sign in with</span>
		<v-container>
			<v-row>
				<v-col>
					<v-btn fab dark large color="google">
						<v-icon dark>mdi-google</v-icon>
					</v-btn>
				</v-col>

				<v-col>
					<v-btn fab dark large color="facebook">
						<v-icon dark>mdi-facebook</v-icon>
					</v-btn>
				</v-col>

				<v-col>
					<v-btn fab dark large color="twitter">
						<v-icon dark>mdi-twitter</v-icon>
					</v-btn>
				</v-col>

				<v-col>
					<v-btn fab dark large color="microsoft">
						<v-icon dark>mdi-microsoft</v-icon>
					</v-btn>
				</v-col>
			</v-row>
		</v-container>

		<v-btn class="" color="" plain to="/auth/register"> Register </v-btn>
	</div>
</template>

<script>
export default {
	components: {},
	layout: 'auth',
	data: () => ({
		showPass: false,
		login: {
			email: '',
			password: '',
		},
	}),
	methods: {
		loggedIn() {
			this.user = this.$store.state.auth.user
		},
		async userLogin() {
			try {
				await this.$auth.loginWith('cookie', {
					data: this.login,
				})
			} catch (err) {}
		},
	},
}
</script>
