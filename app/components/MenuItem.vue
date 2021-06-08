<template>
	<v-card class="ma-2" max-width="344" min-width="342px" outlined>
		<v-list-item three-line>
			<v-list-item-content>
				<v-chip
					v-if="item.tag"
					outlined
					color="orange"
					class="overline mb-4"
					>{{ item.tag }}</v-chip
				>
				<v-chip v-else color="white" class="overline mb-4"></v-chip>
				<v-list-item-title class="headline mb-1">
					{{ item.name }}
				</v-list-item-title>
				<v-list-item-subtitle>{{
					item.description
				}}</v-list-item-subtitle>
			</v-list-item-content>

			<v-list-item-avatar tile size="80" color="grey">
				<img src="" />
			</v-list-item-avatar>
		</v-list-item>

		<v-card-actions>
			<v-btn
				v-if="item.favorite"
				depressed
				rounded
				dark
				color="red"
				@click="unsetFav"
			>
				<v-icon small>mdi-star</v-icon>
			</v-btn>
			<v-btn
				v-else
				depressed
				outlined
				rounded
				dark
				color="red"
				@click="setFav"
			>
				<v-icon small>mdi-star</v-icon>
			</v-btn>
			<v-btn outlined rounded dark color="indigo">
				<v-icon small>mdi-basket-plus</v-icon>
			</v-btn>

			<v-btn
				v-if="$store.state.biz.editor"
				outlined
				rounded
				@click.prevent.stop=""
				><v-icon small>mdi-pencil</v-icon></v-btn
			>
		</v-card-actions>
	</v-card>
</template>

<script>
export default {
	name: 'MenuItem',
	props: {
		item: { type: Object, required: true },
		section: { type: Object, required: true },
		menu: { type: Object, required: true },
	},
	data: () => ({}),
	methods: {
		setFav() {
			return this.$store.dispatch('biz/setFav', {
				item: this.item,
				section: this.section,
			})
		},
		unsetFav() {
			return this.$store.dispatch('biz/unsetFav', {
				item: this.item,
				section: this.section,
			})
		},
	},
}
</script>
