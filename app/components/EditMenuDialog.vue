<template>
	<v-dialog v-model="dialog" persistent max-width="600px">
		<template #activator="{ on, attrs }">
			<v-btn
				v-if="$store.state.biz.editor"
				large
				plain
				rounded
				v-bind="attrs"
				v-on="on"
				@click.prevent.stop=""
				><v-icon small>mdi-pencil</v-icon></v-btn
			>
		</template>
		<v-card>
			<v-card-title>
				<span class="text-h5">Edit Menu</span>
			</v-card-title>
			<v-card-text>
				<v-container>
					<v-row>
						<v-col cols="12">
							<v-text-field
								v-model="name"
								label="Menu"
								required
							></v-text-field>
						</v-col>
						<v-col cols="12">
							<v-text-field
								v-model="slug"
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
				<v-btn color="blue darken-1" text @click="EditMenu()">
					Save
				</v-btn>
			</v-card-actions>
		</v-card>
	</v-dialog>
</template>

<script>
export default {
	name: 'EditMenuDialog',
	props: { menu: { type: Object, required: true } },
	data: () => ({
		dialog: false,
		name: '',
		slug: '',
		id: 0,
	}),
	mounted() {
		this.id = this.menu.id
		this.name = this.menu.name
		this.slug = this.menu.slug
	},
	methods: {
		EditMenu() {
			this.$store
				.dispatch('biz/editMenu', {
					business: {
						id: this.$store.state.biz.business.id,
						slug: this.$route.params.slug,
					},
					menu: { id: this.id, name: this.name, slug: this.slug },
				})
				.then(() => {
					this.dialog = false
				})
		},
	},
}
</script>
