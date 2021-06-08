<template>
	<div class="pa-4">
		<div>
			<h5 class="text-h6 mb-2">Bag</h5>
			<v-divider></v-divider>
			<v-simple-table dense>
				<template #default>
					<thead>
						<tr>
							<th class="text-left">Item</th>
							<th class="text-left">Quantity</th>
							<th class="text-left">Actions</th>
						</tr>
					</thead>
					<tbody>
						<tr>
							<td>Item 1</td>
							<td>Item 1</td>
							<td>
								<v-btn outlined x-small
									><v-icon small>mdi-pencil</v-icon></v-btn
								>
							</td>
						</tr>
					</tbody>
				</template>
			</v-simple-table>
			<v-btn block depressed class="mt-2">Place Order</v-btn>
		</div>
		<div class="mt-4">
			<h5 class="text-h6 mb-2">Orders</h5>
			<v-divider></v-divider>
			<v-btn block depressed class="mt-2">Checkout</v-btn>
		</div>
	</div>
</template>

<script>
export default {
	name: 'Cart',
	components: {},
	props: {},
	data: () => ({}),
}
</script>
