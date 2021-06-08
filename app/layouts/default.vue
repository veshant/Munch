<template>
	<v-app id="app">
		<AppBar />
		<v-main class="grey lighten-2">
			<nuxt v-if="!$slots.default" />
			<slot />
		</v-main>
		<Footer />
	</v-app>
</template>

<script>
import 'swiper/css/swiper.css'
import AppBar from '@/components/AppBar'
import Footer from '@/components/Footer'
export default {
	name: 'DefaultLayout',
	components: {
		AppBar,
		Footer,
	},
	data: () => ({
		links: ['Dashboard', 'Messages', 'Profile', 'Updates'],
		model: 0,
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
.v-main {
	background-image: url('https://source.unsplash.com/1920x1080/?food') !important;
	background-size: cover;
	background-position: bottom center;
	min-height: inherit;
}
.swiper {
	height: 460px;
}
.swiper-slide {
	width: auto;
}
.photo-header {
	pointer-events: none;
	position: absolute;
	display: flex;
	align-items: flex-end;
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
.photo-header .content {
	pointer-events: all;
}
</style>
