<template>
  <div class="sneaker-cart">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">In Your Cart</h1>
      </div>
    </div>
    <br>
    <div class="columns is-multiline is-justify-content-center">
      <div class="column is-7">
        <table class="table is-fullwidth" v-if="itemsInCart">
          <thead>
            <tr>
              <th></th>
              <th>Sneaker</th>
              <th>Price</th>
              <th>Quantity</th>
              <th>Total</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <CartOverview
              v-for="item in cart.items"
              v-bind:key="item.sneaker.id"
              v-bind:cartItem="item"
              v-on:deleteItem="deleteItem" />
          </tbody>
        </table>
        <p v-else>Cart is empty</p>
      </div>
      <div id="order-summary" class="column is-3 is-offset-1 box">
        <h3 class="subtitle has-text-centered"><strong>Order Summary</strong></h3>
        <p>Total: <strong>${{ totalPrice.toFixed(2) }}</strong></p>
        <hr>
        <router-link to="/cart/checkout" class="button is-primary is-fullwidth">Checkout</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import CartOverview from '@/components/CartOverview.vue'
export default {
  name: 'Cart',
  components: {
    CartOverview
  },
  data () {
    return {
      cart: {
        items: []
      }
    }
  },
  mounted () {
    document.title = 'Cart | Dirty Kicks'
    this.cart = this.$store.state.cart
  },
  methods: {
    deleteItem (item) {
      this.cart.items = this.cart.items.filter(i => i.sneaker.id !== item.sneaker.id)
    }
  },
  computed: {
    itemsInCart () {
      return this.cart.items.reduce((acc, curVal) => {
        return (acc += curVal.quantity)
      }, 0)
    },
    totalPrice () {
      return this.cart.items.reduce((acc, curVal) => {
        return (acc += curVal.sneaker.price * curVal.quantity)
      }, 0)
    }
  }
}
</script>

<style lang="scss">
#order-summary {
  margin-bottom: auto;
}
</style>
