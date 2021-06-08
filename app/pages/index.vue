<template>
	<div>
		<div class="text-center">
			<h1 class="text-h4 mb-4 overline white--text">
				{{ title[Math.floor(Math.random() * (title.length - 0) + 0)] }}
			</h1>
			<SearchBar dark />

			<v-chip class="ma-2" color="indigo" dark label>
				Mediterranean
			</v-chip>
			<v-chip class="ma-2" color="indigo" dark label> Pizza </v-chip>
			<v-chip class="ma-2" color="indigo" dark label> American </v-chip>
			<v-chip class="ma-2" color="indigo" dark label> Asian </v-chip>
		</div>
	</div>
</template>

<script>
import SearchBar from '@/components/SearchBar'
export default {
	components: {
		SearchBar,
	},
	layout: 'index',
	data: () => ({
		title: [
			'____ Seeking Food',
			'What do you crave?',
			'Find your food',
			'Great eats await',
			"Secret's in the sauce",
			'You are what you eat',
		],
	}),
}
</script>
