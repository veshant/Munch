<template>
	<v-dialog v-model="dialog" persistent max-width="600px">
		<template #activator="{ on, attrs }">
			<v-btn
				class="ma-2"
				color="grey"
				min-width="342px"
				min-height="172px"
				outlined
				v-bind="attrs"
				v-on="on"
				><v-icon large>mdi-plus-thick</v-icon></v-btn
			>
		</template>
		<v-card>
			<v-card-title>
				<span class="text-h5">Add Item to {{ section.name }}</span>
			</v-card-title>
			<v-card-text>
				<v-container>
					<v-row>
						<v-col cols="12">
							<v-text-field
								v-model="item.name"
								label="Name"
								required
							></v-text-field>
							<v-textarea
								v-model="item.description"
								label="Description"
								value=""
								hint="Type a description"
							></v-textarea>
							<v-text-field
								v-model="item.tag"
								label="Tag"
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
				<v-btn color="blue darken-1" text @click="AddItem">
					Save
				</v-btn>
			</v-card-actions>
		</v-card>
	</v-dialog>
</template>

<script>
export default {
	name: 'AddItemDialog',
	props: {
		section: { type: Object, required: true },
	},
	data: () => ({
		dialog: false,
		item: { name: '', description: '', tag: '' },
	}),
	methods: {
		AddItem() {
			this.$store
				.dispatch('biz/addItem', {
					item: this.item,
					section: this.section,
				})
				.then(() => {
					this.dialog = false
					this.item.name = this.item.description = this.item.tag = ''
				})
		},
	},
}
</script>
