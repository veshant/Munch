<template>
	<v-container fluid style="max-width: 860px; margin: auto">
		<v-sheet min-height="70vh" rounded="lg" class="pa-8">
			<h2 class="text-h4 overline">Add a business</h2>
			<v-form>
				<v-row>
					<v-col cols="12" md="6">
						<v-text-field
							v-model="biz.name"
							:counter="10"
							label="Business Name"
							required
						></v-text-field>
					</v-col>

					<v-col cols="12" md="6">
						<v-text-field
							v-model="biz.slug"
							:counter="10"
							label="Slug"
							required
						></v-text-field>
					</v-col>
				</v-row>
				<v-row>
					<v-col cols="12" md="12">
						<v-combobox
							v-model="biz.categories"
							hide-selected
							hint="Maximum of 5 tags"
							label="Categories"
							multiple
							persistent-hint
							small-chips
						>
						</v-combobox>
					</v-col>
				</v-row>
				<v-row>
					<v-col cols="12" md="12">
						<v-textarea
							v-model="biz.description"
							label="Description"
							value=""
							hint="Type a description"
						></v-textarea>
					</v-col>
				</v-row>
				<v-row>
					<v-col cols="12" md="6">
						<span class="text-body-1">Rating</span>
						<v-rating
							v-model="biz.rating"
							empty-icon="mdi-star-outline"
							full-icon="mdi-star"
							half-icon="mdi-star-half-full"
							hover
							length="5"
							size="32"
							half-increments
							color="deep-orange"
							background-color="deep-orange accent-1"
						></v-rating>
					</v-col>

					<v-col cols="12" md="6">
						<span class="text-body-1">Price Range</span>
						<v-rating
							v-model="biz.price_range"
							empty-icon="mdi-currency-usd-circle-outline"
							full-icon="mdi-currency-usd-circle"
							hover
							length="5"
							size="32"
							color="deep-orange"
							background-color="deep-orange accent-1"
						></v-rating>
					</v-col>
				</v-row>
				<v-row>
					<v-col cols="12" md="6">
						<v-menu
							ref="open_time_picker"
							v-model="open_time_picker"
							:close-on-content-click="false"
							:nudge-right="40"
							:return-value.sync="biz.open_time"
							transition="scale-transition"
							offset-y
							max-width="290px"
							min-width="290px"
						>
							<template #activator="{ on, attrs }">
								<v-text-field
									v-model="biz.open_time"
									label="Open Time"
									prepend-icon="mdi-clock-time-four-outline"
									readonly
									type="text"
									v-bind="attrs"
									v-on="on"
								></v-text-field>
							</template>
							<v-time-picker
								v-if="open_time_picker"
								v-model="biz.open_time"
								full-width
								@click:minute="
									$refs.open_time_picker.save(biz.open_time)
								"
							></v-time-picker> </v-menu
					></v-col>

					<v-col cols="12" md="6"
						><v-menu
							ref="close_time_picker"
							v-model="close_time_picker"
							:close-on-content-click="false"
							:nudge-right="40"
							:return-value.sync="biz.close_time"
							transition="scale-transition"
							offset-y
							max-width="290px"
							min-width="290px"
						>
							<template #activator="{ on, attrs }">
								<v-text-field
									v-model="biz.close_time"
									label="Close Time"
									prepend-icon="mdi-clock-time-four-outline"
									readonly
									type="text"
									v-bind="attrs"
									v-on="on"
								></v-text-field>
							</template>
							<v-time-picker
								v-if="close_time_picker"
								v-model="biz.close_time"
								full-width
								@click:minute="
									$refs.close_time_picker.save(biz.close_time)
								"
							></v-time-picker>
						</v-menu>
					</v-col>
				</v-row>
				<v-btn
					block
					large
					depressed
					dark
					color="deep-orange"
					class="my-4"
					@click="addBiz"
				>
					submit
				</v-btn>
				<v-btn block depressed @click="clear"> clear </v-btn>
			</v-form>
		</v-sheet>
	</v-container>
</template>

<script>
export default {
	layout: 'default',
	middleware: 'auth',
	data: () => ({
		biz: {
			name: '',
			slug: '',
			description: '',
			rating: 0,
			categories: [],
			open_time: null,
			close_time: null,
			price_range: 0,
		},
		open_time_picker: false,
		close_time_picker: false,
	}),
	mounted() {},
	methods: {
		addBiz() {
			this.$store
				.dispatch('biz/addBiz', { business: this.biz })
				.then(() => {
					this.$router.push('/biz/' + this.biz.slug)
				})
		},
		clear() {
			this.biz.name = ''
			this.biz.rating = 0
			this.biz.categories = []
			this.biz.open_time = ''
			this.biz.close_time = ''
			this.biz.price_range = 0
		},
	},
}
</script>
