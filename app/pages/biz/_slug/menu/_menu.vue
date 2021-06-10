<template>
	<v-card outlined color="basil" height="100%">
		<v-card-title class="text-center justify-center py-6">
			<h1 class="font-weight-bold display-3 basil--text">
				{{ biz.menu.name }}
			</h1>
		</v-card-title>

		<v-tabs
			v-model="tab"
			show-arrows
			background-color="transparent"
			color="basil"
			grow
		>
			<template v-for="(section, i) in biz.menu.sections">
				<v-tab
					:key="'menu-section' + i"
					@click="fetchItems(section.id)"
				>
					{{ section.name }}
				</v-tab>

				<v-btn
					v-if="biz.editor"
					:key="'menu-section-btn' + i"
					small
					text
					style="height: 100%"
					@click.prevent.stop=""
					><v-icon small>mdi-pencil</v-icon></v-btn
				>
			</template>
			<AddSectionDialog v-if="biz.editor" :menu="biz.menu" />
		</v-tabs>
		<v-tabs-items v-model="tab">
			<v-tab-item
				v-for="(section, i) in biz.menu.sections"
				:key="'menu-section' + i"
			>
				<v-container>
					<div
						class="
							menu-items
							d-flex
							flex-wrap
							justify-space-between
						"
					>
						<template v-if="section.items">
							<MenuItem
								v-for="item in section.items"
								:key="'menu-item' + item.id"
								:item="item"
								:section="section"
								:menu="biz.menu"
							/>
						</template>
						<AddItemDialog v-if="biz.editor" :section="section" />
						<template v-if="!section.items_loaded">
							<v-card
								v-for="skel in 3"
								:key="'skel' + skel"
								class="ma-2"
								max-width="344"
								outlined
							>
								<v-skeleton-loader
									type="article, actions"
									min-width="342px"
								></v-skeleton-loader>
							</v-card>
						</template>
					</div>
				</v-container>
			</v-tab-item>
		</v-tabs-items>
	</v-card>
</template>

<script>
import { mapState } from 'vuex'
import MenuItem from '@/components/MenuItem'
import AddSectionDialog from '@/components/AddSectionDialog'
import AddItemDialog from '@/components/AddItemDialog'
export default {
	components: {
		MenuItem,
		AddItemDialog,
		AddSectionDialog,
	},
	layout: 'biz',
	data: () => ({
		title: '',
		tab: null,
	}),
	head() {
		return {
			title: this.title,
		}
	},
	computed: {
		...mapState(['biz']),
	},
	mounted() {
		this.$store
			.dispatch('biz/loadBiz', this.$route.params.slug)
			.then((biz) => {
				this.$store
					.dispatch('biz/loadMenu', {
						slug: this.$route.params.slug,
						menu: this.$route.params.menu,
					})
					.then((menu) => {
						this.title = menu.name + ' | ' + biz.name
						if (menu.sections.length > 0)
							this.fetchItems(menu.sections[0].id)
					})
			})
	},
	methods: {
		fetchItems(id) {
			this.tab = null
			return this.$store.dispatch('biz/loadItems', id)
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
}
.menu-items:after {
	height: 0;
	width: 344px;
	content: '';
}
</style>
