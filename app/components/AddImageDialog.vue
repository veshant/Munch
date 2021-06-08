<template>
	<div>
		<v-btn
			class="my-4"
			color="grey"
			min-width="342px"
			min-height="172px"
			outlined
			:loading="loading"
			@click="click"
			><v-icon large>mdi-plus-thick</v-icon></v-btn
		>
		<input
			ref="fileInput"
			name="uploadImage"
			type="file"
			style="display: none"
			@change="uploadFile($event)"
		/>
	</div>
</template>

<script>
export default {
	name: 'AddImageDialog',
	props: {},
	data: () => ({
		file: null,
		loading: false,
	}),
	methods: {
		click() {
			this.$refs.fileInput.click()
		},
		uploadFile(event) {
			const file = event.target.files[0]
			if (file) {
				this.$store.dispatch('biz/uploadImage', { event }).then(() => {
					this.loading = false
				})
			}
		},
	},
}
</script>
