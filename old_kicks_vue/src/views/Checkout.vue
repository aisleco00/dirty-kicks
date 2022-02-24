<template>
  <div class="checkout-page">
    <div class="columns is-multiline is-justify-content-center">
      <div class="column is-12">
        <h1 class="title has-text-centered">Checkout</h1>
      </div>
      <div class="column is-7">
        <h2 class="subtitle">Shipping</h2>
        <p>Please enter your shipping details.</p>
        <p class="is-size-7 mb-5">All fields marked with an asterisk (*) are required</p>
        <br>
        <div class="columns is-multiline">
          <div class="column is-6">
            <div class="field">
              <label>First Name*</label>
              <div class="control">
                <input type="text" class="input" v-model="firstname" required>
              </div>
            </div>
          </div>
          <div class="column is-6">
            <div class="field">
              <label>Last Name*</label>
              <div class="control">
                <input type="text" class="input" v-model="lastname" required>
              </div>
            </div>
          </div>
          <div class="column is-12">
            <div class="field">
              <label>Address*</label>
              <div class="control is-expanded">
                <input type="text" class="input" v-model="address" required>
              </div>
            </div>
          </div>
          <div class="column is-4">
            <div class="field">
              <label>City*</label>
              <div class="control">
                <input type="text" class="input" v-model="city" required>
              </div>
            </div>
          </div>
          <div class="column is-4">
            <div class="field">
              <label>State*</label>
              <div class="control">
                <input type="text" class="input" v-model="state" required>
              </div>
            </div>
          </div>
          <div class="column is-4">
            <div class="field">
              <label>Zip Code*</label>
              <div class="control">
                <input type="text" class="input" v-model="zipcode" required>
              </div>
            </div>
          </div>
          <div class="column is-6">
            <div class="field">
              <label>Email*</label>
              <div class="control">
                <input type="email" class="input" v-model="email" required>
              </div>
            </div>
          </div>
          <div class="column is-6">
            <div class="field">
              <label>Phone Number*</label>
              <div class="control">
                <input type="text" class="input" v-model="phonenumber" required>
              </div>
            </div>
          </div>
        </div>
        <div class="notification is-danger mt-4" v-if="error.length">
          <p v-for="err in error" v-bind:key="err">{{ err }}</p>
        </div>
        <div id="card-confirmation" class="mb-5"></div>
        <template v-if="itemsInCart">
          <button class="button is-primary" @click="submitOrder">Place Order</button>
        </template>
      </div>
      <template v-if="!this.itemsInCart">
        <div id="checkout-summary" class="column is-3 card is-offset-1">
          <p class="subtitle has-text-centered">No items in your cart...</p>
        </div>
      </template>
      <template v-else>
        <div id="checkout-summary" class="column is-3 card is-offset-1">
          <p class="subtitle has-text-centered">In Your Cart</p>
          <p class="is-size-7"><strong>Cart Qty: {{ itemsInCart }}</strong></p>
          <p class="is-size-7"><strong>Total Price: ${{ totalPrice.toFixed(2) }}</strong></p>
          <br>
          <div class="card-content" v-for="item in cart.items" v-bind:key="item.sneaker.id">
            <div class="media">
              <div class="media-left">
                <figure class="image is48x48">
                  <img v-bind:src="item.sneaker.get_thumbnail" alt="sneaker">
                </figure>
              </div>
              <div class="media-content">
                <p class="is-size-7"><strong>{{ item.sneaker.name }}</strong></p>
                <p class="is-size-7">Qty: {{ item.quantity }} @ ${{ item.sneaker.price }}</p>
                <p class="is-size-7">${{ sneakerTotal(item).toFixed(2) }}</p>
              </div>
            </div>
          </div>
        </div>
      </template>
    </div>
  </div>
</template>

<script>
import stripeKey from '@/keys/key.js'
import axios from 'axios'
export default {
  name: 'Checkout',
  data () {
    return {
      cart: {
        items: []
      },
      stripe: {},
      card: {},
      firstname: '',
      lastname: '',
      address: '',
      city: '',
      state: '',
      zipcode: '',
      email: '',
      phonenumber: '',
      error: []
    }
  },
  mounted () {
    document.title = 'Checkout | Dirty Kicks'
    this.cart = this.$store.state.cart
    if (this.itemsInCart > 0) {
      this.stripe = stripeKey
      const elements = this.stripe.elements()
      this.card = elements.create('card', { hidePostalCode: true })
      this.card.mount('#card-confirmation')
    }
  },
  methods: {
    sneakerTotal (item) {
      return item.quantity * item.sneaker.price
    },
    submitOrder () {
      this.error = []
      if (this.firstname === '') {
        this.error.push('Invalid, First Name field must be filled!')
      }
      if (this.lastname === '') {
        this.error.push('Invalid, Last Name field must be filled!')
      }
      if (this.address === '') {
        this.error.push('Invalid, Address field must be filled!')
      }
      if (this.city === '') {
        this.error.push('Invalid, City field must be filled!')
      }
      if (this.state === '') {
        this.error.push('Invalid, State field must be filled!')
      }
      if (this.zipcode === '') {
        this.error.push('Invalid, Zip Code field must be filled!')
      }
      if (this.email === '') {
        this.error.push('Invalid, Email field must be filled!')
      }
      if (this.phonenumber === '') {
        this.error.push('Invalid, Phone Number field must be filled!')
      }
      if (!this.error.length) {
        this.$store.commit('setAppLoading', true)
        this.stripe.createToken(this.card).then(result => {
          if (result.error) {
            this.$store.commit('setAppLoading', false)
            this.error.push('An error occurred, please try again.')
            console.log(result.error.message)
          } else {
            this.stripeTokenHandler(result.token)
          }
        })
      }
    },
    async stripeTokenHandler (token) {
      const items = []
      for (let i = 0; i < this.cart.items.length; i++) {
        const item = this.cart.items[i]
        const obj = {
          sneaker: item.sneaker.id,
          quantity: item.quantity,
          price: item.sneaker.price * item.quantity
        }
        items.push(obj)
      }
      const data = {
        firstname: this.firstname,
        lastname: this.lastname,
        address: this.address,
        city: this.city,
        state: this.state,
        zipcode: this.zipcode,
        email: this.email,
        phonenumber: this.phonenumber,
        items: items,
        stripe_token: token.id
      }
      await axios
        .post('/api/v1/checkout/', data)
        .then(response => {
          this.$store.commit('emptyCart')
          this.$router.push('/cart/confirmation')
        })
        .catch(err => {
          this.error.push('Unable to process payment, please try again')
          console.log(err)
        })
      this.$store.commit('setAppLoading', false)
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
#checkout-summary {
  margin-bottom: auto;
}
</style>
