<template>
	<v-list dense rounded>
		<v-list-item-group active-class="blue--text text--accent-4">
			<v-list-item
				v-for="(menu, i) in menus"
				:key="'left-nav' + i"
				:to="menu.link"
				exact
				style="padding-right: 0"
			>
				<v-list-item-title :class="menu.class">{{
					menu.title
				}}</v-list-item-title>

				<EditMenuDialog v-if="$store.state.biz.editor" :menu="menu" />
			</v-list-item>
		</v-list-item-group>

		<AddMenuDialog v-if="$store.state.biz.editor" />
	</v-list>
</template>

<script>
import AddMenuDialog from '@/components/AddMenuDialog'
import EditMenuDialog from '@/components/EditMenuDialog'
export default {
	name: 'LeftNav',
	components: { AddMenuDialog, EditMenuDialog },
	props: { menus: { type: Array, required: true } },
	data: () => ({}),
}
</script>
