<template>
	<v-container class="px-12 py-8">
		<h3 class="text-h3">About</h3>
		<p>
			{{ biz.business.description }}
		</p>
		<v-divider></v-divider>
	</v-container>
</template>

<script>
import { mapState } from 'vuex'
export default {
	layout: 'biz',
	data: () => ({
		title: '',
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
			.then((res) => {
				this.title = res.name
			})
	},
	methods: {},
}
</script>
