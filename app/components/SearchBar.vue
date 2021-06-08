<template>
	<div>
		<v-autocomplete
			v-model="model"
			:items="items"
			:loading="isLoading"
			:search-input.sync="search"
			chips
			clearable
			hide-details
			hide-selected
			auto-select-first
			item-text="name"
			item-value="slug"
			label="Search places..."
			filled
			rounded
			dense
			outlined
			append-icon="mdi-magnify"
			:color="dark ? 'white' : ''"
			:dark="dark"
			return-object
		>
			<template #no-data>
				<v-list-item>
					<v-list-item-title> Search for a place </v-list-item-title>
				</v-list-item>
			</template>
			<template #selection="{ attr, on, item, selected }">
				<v-chip
					v-bind="attr"
					:input-value="selected"
					color="blue-grey"
					class="white--text"
					v-on="on"
				>
					<v-icon left> mdi-silverware </v-icon>
					<span v-text="item.name"></span>
				</v-chip>
			</template>
			<template #item="{ item }">
				<v-list-item-avatar
					color="indigo"
					class="headline font-weight-light white--text"
				>
					{{ item.name.charAt(0) }}
				</v-list-item-avatar>
				<v-list-item-content>
					<v-list-item-title v-text="item.name"></v-list-item-title>
					<v-list-item-subtitle
						v-text="item.slug"
					></v-list-item-subtitle>
				</v-list-item-content>
				<v-list-item-action>
					<v-icon>mdi-silverware</v-icon>
				</v-list-item-action>
			</template>
		</v-autocomplete>
	</div>
</template>
<script>
import axios from 'axios'

export default {
	name: 'SearchBar',
	props: {
		dark: { type: Boolean, required: false, default: false },
	},
	data: () => ({
		isLoading: false,
		items: [],
		model: null,
		search: null,
	}),

	watch: {
		model(val) {
			if (val) {
				this.isLoading = true
				this.$router.push('/biz/' + val.slug)
				this.isLoading = false
			}
		},
		search() {
			// Items have already been loaded
			if (this.items.length > 0) return

			this.isLoading = true

			// Lazily load input items
			axios
				.get('/api/business')
				.then((res) => {
					this.items = res.data.items
				})
				.catch((err) => {
					console.log(err)
				})
				.finally(() => (this.isLoading = false))
		},
	},
}
</script>
