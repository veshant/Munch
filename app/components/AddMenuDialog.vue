<template>
	<v-dialog v-model="dialog" persistent max-width="600px">
		<template #activator="{ on, attrs }">
			<v-btn large block text v-bind="attrs" v-on="on"
				>Add Menu <v-icon right>mdi-plus-thick</v-icon></v-btn
			>
		</template>
		<v-card>
			<v-card-title>
				<span class="text-h5">Add Menu</span>
			</v-card-title>
			<v-card-text>
				<v-container>
					<v-row>
						<v-col cols="12">
							<v-text-field
								v-model="menu.name"
								label="Menu"
								required
							></v-text-field>
						</v-col>
						<v-col cols="12">
							<v-text-field
								v-model="menu.slug"
								label="Slug"
								required
							></v-text-field>
						</v-col>
					</v-row>
				</v-container>
			</v-card-text>
			<v-card-actions>
				<v-spacer></v-spacer>
				<v-btn color="blue darken-1" text @click="dialog = false">
					Close
				</v-btn>
				<v-btn color="blue darken-1" text @click="AddMenu()">
					Save
				</v-btn>
			</v-card-actions>
		</v-card>
	</v-dialog>
</template>

<script>
export default {
	name: 'AddMenuDialog',
	props: {},
	data: () => ({
		dialog: false,
		menu: { name: '', slug: '' },
	}),
	methods: {
		AddMenu() {
			this.$store
				.dispatch('biz/addMenu', {
					business: {
						id: this.$store.state.biz.business.id,
						slug: this.$route.params.slug,
					},
					menu: this.menu,
				})
				.then(() => {
					this.dialog = false
					this.menu.name = this.menu.slug = ''
				})
		},
	},
}
</script>
