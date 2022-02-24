<template>
  <tr>
    <td>
      <img class="image is-64x64" v-bind:src="item.sneaker.get_thumbnail" alt="sneaker">
    </td>
    <td><router-link :to="item.sneaker.get_absolute_url">{{ item.sneaker.name }}</router-link></td>
    <td>${{ item.sneaker.price }}</td>
    <td>
      {{ item.quantity }}
      <a @click="increaseQuantity(item)">
        <span class="icon is-small">
          <i class="fas fa-angle-up"></i>
        </span>
      </a>
      <a @click="decreaseQuantity(item)">
        <span class="icon is-small">
          <i class="fas fa-angle-down"></i>
        </span>
      </a>
    </td>
    <td>${{ totalPrice(item).toFixed(2) }}</td>
    <td>
      <a id="trash-delete" @click="deleteItem(item)">
        <span class="icon">
          <i class="fas fa-trash"></i>
        </span>
      </a>
    </td>
  </tr>
</template>

<script>
export default {
  name: 'CartOverview',
  props: {
    cartItem: Object
  },
  data () {
    return {
      item: this.cartItem
    }
  },
  methods: {
    totalPrice (item) {
      return item.quantity * item.sneaker.price
    },
    decreaseQuantity (item) {
      item.quantity -= 1
      if (item.quantity === 0) {
        this.$emit('deleteItem', item)
      }
      this.cartIsUpdated()
    },
    increaseQuantity (item) {
      item.quantity += 1
      this.cartIsUpdated()
    },
    cartIsUpdated () {
      localStorage.setItem('cart', JSON.stringify(this.$store.state.cart))
    },
    deleteItem (item) {
      this.$emit('deleteItem', item)
      this.cartIsUpdated()
    }
  }
}
</script>

<style lang="scss">
#trash-delete {
  color: hsl(0, 0%, 29%);
}
#trash-delete:hover {
  color: hsl(348, 100%, 61%);
}
</style>
