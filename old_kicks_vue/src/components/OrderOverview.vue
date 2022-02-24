<template>
  <div class="is-8">
    <div><strong>Order number:</strong> {{ order.id }}</div>
    <table class="table is-fullwidth">
      <thead>
        <tr>
          <th></th>
          <th>Sneaker</th>
          <th>Price</th>
          <th>Quantity</th>
          <th>Total</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in order.items" v-bind:key="item.sneaker.id">
          <td>
            <img class="image is-64x64" v-bind:src="item.sneaker.get_thumbnail" alt="sneaker">
          </td>
          <td>{{ item.sneaker.name }}</td>
          <td>${{ item.sneaker.price }}</td>
          <td>{{ item.quantity }}</td>
          <td>${{ totalPerItem(item).toFixed(2) }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'OrderOverview',
  props: {
    order: Object
  },
  methods: {
    totalPerItem (item) {
      return item.quantity * item.sneaker.price
    }
  }
}
</script>
