<template>
	<v-container fluid class="px-12 py-8">
		<h2 class="text-h4 overline">Edit {{ biz.name }}</h2>
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
				@click="editBiz"
			>
				save
			</v-btn>
			<v-btn block depressed @click="clear"> revert </v-btn>
		</v-form>

		<v-divider class="my-4" />

		<h2 class="text-h4 overline mb-2">Add Images</h2>

		<div class="d-flex flex-wrap justify-space-between">
			<template v-for="i in 3">
				<v-hover v-slot="{ hover }" :key="i">
					<v-card
						class="my-4"
						:elevation="hover ? 12 : 2"
						:class="{ 'on-hover': hover, 'image-card': true }"
						max-width="344"
						min-width="342px"
						outlined
					>
						<v-img src="/background.jpg" height="225px">
							<v-btn
								:class="{
									'show-btns': hover,
								}"
								depressed
								color="#ff572270"
							>
								<v-icon large color="white">
									mdi-trash-can-outline
								</v-icon>
							</v-btn>
						</v-img>
					</v-card>
				</v-hover>
			</template>

			<AddImageDialog />
		</div>
	</v-container>
</template>

<script>
import AddImageDialog from '@/components/AddImageDialog'
export default {
	components: {
		AddImageDialog,
	},
	layout: 'biz',
	data: () => ({
		biz: {
			name: '',
			slug: '',
			rating: 0,
			categories: [],
			open_time: null,
			close_time: null,
			price_range: 0,
			menus: [],
		},
		open_time_picker: false,
		close_time_picker: false,
	}),
	mounted() {
		this.$store
			.dispatch('biz/loadBiz', this.$route.params.slug)
			.then(() => {
				Object.assign(this.biz, this.$store.state.biz.business)
			})
	},
	methods: {
		editBiz() {
			this.$store
				.dispatch('biz/editBiz', { business: this.biz })
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

<style scoped>
.v-card {
	transition: opacity 0.4s ease-in-out;
}

.v-card:not(.on-hover) {
}

.image-card button {
	visibility: hidden;
}

.on-hover button {
	transition: opacity 0.4s ease-in-out;
	visibility: visible;
	height: 100% !important;
	width: 100%;
}
</style>
