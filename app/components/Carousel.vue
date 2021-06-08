<template>
	<swiper class="swiper" :options="swiperOption">
		<swiper-slide v-for="(image, i) in images" :key="'swiper' + i">
			<img :src="image" height="100% " />
		</swiper-slide>
		<div slot="button-prev" class="swiper-button-prev"></div>
		<div slot="button-next" class="swiper-button-next"></div>
	</swiper>
</template>

<script>
import { Swiper, SwiperSlide, directive } from 'vue-awesome-swiper'
export default {
	name: 'Carousel',
	components: {
		Swiper,
		SwiperSlide,
	},
	directives: {
		swiper: directive,
	},
	props: { images: { type: Array, required: true } },
	data: () => ({
		swiperOption: {
			slidesPerView: 'auto',
			spaceBetween: 0,
			loop: true,
			navigation: {
				nextEl: '.swiper-button-next',
				prevEl: '.swiper-button-prev',
			},
		},
	}),
}
</script>

<style scoped>
.swiper {
	height: 460px;
}
.swiper-slide {
	width: auto;
}
</style>
