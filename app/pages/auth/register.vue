<template>
	<div class="text-center">
		<span class="text-h3">Register</span>
		<v-form>
			<v-container>
				<v-text-field
					v-model="register.first_name"
					label="First Name"
					required
				></v-text-field>
				<v-text-field
					v-model="register.last_name"
					label="Last Name"
					required
				></v-text-field>
				<v-text-field
					v-model="register.email"
					label="E-mail"
					required
				></v-text-field>
				<v-text-field
					v-model="register.password"
					:append-icon="showPass ? 'mdi-eye' : 'mdi-eye-off'"
					:type="showPass ? 'text' : 'password'"
					name="input-10-1"
					label="Password"
					hint="At least 8 characters"
					counter
					@click:append="showPass = !showPass"
				></v-text-field>
				<v-btn block outlined class="mt-4" @click="userRegister">
					Register
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

		<v-btn class="" color="" plain> Register </v-btn>
	</div>
</template>

<script>
export default {
	components: {},
	layout: 'auth',
	data: () => ({
		showPass: false,
		register: {
			first_name: '',
			last_name: '',
			email: '',
			password: '',
		},
	}),
	methods: {
		async userRegister() {
			try {
				await this.$axios.post('/api/auth/api/register', {
					first_name: this.register.first_name,
					last_name: this.register.last_name,
					email: this.register.email,
					password: this.register.password,
				})

				await this.$auth.loginWith('local', {
					data: {
						email: this.register.email,
						password: this.register.password,
					},
				})

				this.$router.push('/')
			} catch (e) {
				this.error = e.response.data.message
			}
		},
	},
}
</script>
