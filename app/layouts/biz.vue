<template>
	<default-layout>
		<v-main style="max-width: 1920px; margin: auto; padding: 0">
			<Carousel :images="images" />
			<div class="carousel-overlay d-sm-flex">
				<div class="carousel-inner d-sm-flex flex-fill">
					<div class="flex-fill">
						<div class="content">
							<div class="mb-2">
								<h1
									class="text-h3 text-sm-h2 font-weight-black"
								>
									{{ biz.business.name }}
								</h1>
							</div>
							<div class="mb-2 d-block">
								<v-rating
									v-model="biz.business.rating"
									empty-icon="mdi-star-outline"
									full-icon="mdi-star"
									half-icon="mdi-star-half-full"
									hover
									readonly
									length="5"
									size="32"
									half-increments
									color="white"
									background-color="white"
								></v-rating>
							</div>
							<div class="mb-2 d-block font-weight-medium">
								<v-chip
									v-for="(category, i) in biz.business
										.categories"
									:key="'cat' + i"
									color="blue-grey"
									text-color="white"
									class="mr-2"
								>
									{{ category }}
								</v-chip>
							</div>
							<div class="mb-2 d-sm-inline font-weight-bold">
								<v-chip
									pill
									:color="
										biz.business.open_class + ' lighten-3'
									"
								>
									<v-avatar
										left
										:color="
											biz.business.open_class +
											' darken-4'
										"
									>
										<v-icon color="white">
											mdi-clock-outline
										</v-icon>
									</v-avatar>
									{{ biz.business.open_time }} -
									{{ biz.business.close_time }}
								</v-chip>
							</div>
							<div class="mb-2 d-sm-inline font-weight-bold">
								<v-icon
									v-for="i in biz.business.price_range"
									:key="'pr' + i"
									large
									color="amber"
								>
									mdi-currency-usd-circle-outline
								</v-icon>
							</div>
						</div>
					</div>
					<div>
						<v-btn
							v-if="biz.editor"
							:to="'/biz/' + $route.params.slug + '/edit/'"
							large
							outlined
							color="white"
							>Edit Business<v-icon right
								>mdi-pencil</v-icon
							></v-btn
						>
						<v-btn v-else large outlined color="orange"
							>Write a Review<v-icon right
								>mdi-star-outline</v-icon
							></v-btn
						>
					</div>
				</div>
			</div>
		</v-main>
		<v-container fluid style="max-width: 1920px; margin: auto">
			<v-row>
				<v-col cols="12" md="3" xl="2" class="order-1 order-md-1">
					<v-sheet rounded="lg" min-height="268">
						<LeftNav :menus="biz.menus" />
					</v-sheet>
				</v-col>

				<v-col cols="12" md="6" xl="8" class="order-3 order-md-2">
					<v-sheet min-height="70vh" rounded="lg">
						<nuxt />
					</v-sheet>
				</v-col>

				<v-col cols="12" md="3" xl="2" class="order-2 order-md-3">
					<v-sheet rounded="lg" min-height="268"> <Cart /></v-sheet>
				</v-col>
			</v-row>
		</v-container>
	</default-layout>
</template>

<script>
import { mapState } from 'vuex'
import LeftNav from '@/components/LeftNav'
import Cart from '@/components/Cart'
import Carousel from '@/components/Carousel'
import DefaultLayout from '~/layouts/default.vue'
export default {
	name: 'BizLayout',
	components: {
		DefaultLayout,
		LeftNav,
		Cart,
		Carousel,
	},
	data: () => ({
		model: 0,
		images: [
			'https://source.unsplash.com/900x600/?food',
			'https://source.unsplash.com/1200x800/?food',
			'https://source.unsplash.com/600x400/?food',
			'https://source.unsplash.com/1920x1080/?food',
			'https://source.unsplash.com/960x480/?food',
			'https://source.unsplash.com/900x600/?food',
			'https://source.unsplash.com/1920x1080/?food',
			'https://source.unsplash.com/960x480/?food',
			'https://source.unsplash.com/640x480/?food',
			'https://source.unsplash.com/1200x800/?food',
		],
	}),
	computed: {
		...mapState(['biz']),
	},
}
</script>

<style scoped>
.carousel-overlay {
	pointer-events: none;
	position: absolute;
	align-items: flex-end;
	display: inline-grid;
	top: 0;
	left: 0;
	right: 0;
	bottom: 0;
	z-index: 1;
	width: 100%;
	padding: 40px 64px;
	margin: auto;
	color: #fff;
	background: linear-gradient(
		to bottom,
		rgba(0, 0, 0, 0) 0%,
		rgba(0, 0, 0, 0.4) 75%,
		rgba(0, 0, 0, 0.7) 100%
	);
}
.carousel-overlay .carousel-inner {
	align-items: flex-end;
}

.carousel-overlay .content {
	pointer-events: all;
	display: inline-block;
}

.carousel-overlay .v-btn {
	pointer-events: all;
}
</style>
