<template>
	<v-dialog v-model="dialog" persistent max-width="600px">
		<template #activator="{ on, attrs }">
			<div class="add-section" @click.prevent.stop="">
				<v-btn text v-bind="attrs" v-on="on"
					><v-icon>mdi-plus-thick</v-icon></v-btn
				>
			</div>
		</template>
		<v-card>
			<v-card-title>
				<span class="text-h5">Add Section to {{ menu.name }}</span>
			</v-card-title>
			<v-card-text>
				<v-container>
					<v-row>
						<v-col cols="12">
							<v-text-field
								v-model="section.name"
								label="Name"
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
				<v-btn color="blue darken-1" text @click="AddSection()">
					Save
				</v-btn>
			</v-card-actions>
		</v-card>
	</v-dialog>
</template>

<script>
export default {
	name: 'AddSectionDialog',
	props: {
		menu: { type: Object, required: true },
	},
	data: () => ({
		dialog: false,
		section: { name: '' },
	}),
	methods: {
		AddSection() {
			this.$store
				.dispatch('biz/addSection', {
					section: this.section,
					menu: this.menu,
				})
				.then(() => {
					this.dialog = false
					this.section.name = ''
				})
		},
	},
}
</script>

<style scoped>
.add-section {
	flex: none !important;
	margin: 0px !important;
	padding: 0px !important;
	min-width: auto !important;
}
.add-section .v-btn {
	border-radius: 0;
	height: 100%;
	min-width: 90px;
}
</style>
