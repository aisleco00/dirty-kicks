<template>
  <div class="sneaker-page">
    <br>
    <div class="columns is-multiline is-justify-content-center">
      <div class="column is-3">
        <figure class="image mb-6">
          <img v-bind:src="sneaker.get_image" alt="sneaker image">
        </figure>
        <p>{{ sneaker.description }}</p>
      </div>
      <div id="sneaker-title" class="box column is-3 is-offset-2">
        <h1 class="title">{{ sneaker.name }}</h1>
        <p class="pb-2">${{ sneaker.price }}</p>
        <div class="field">
          <label class="label">Quantity</label>
          <div class="control">
            <input type="number" class="input" min="1" v-model="quantity">
          </div>
        </div>
        <button class="button is-success is-fullwidth" @click="addToCart">Add to Cart</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'
export default {
  name: 'Sneaker',
  data () {
    return {
      sneaker: {},
      quantity: 1
    }
  },
  mounted () {
    this.getSneaker()
  },
  methods: {
    async getSneaker () {
      this.$store.commit('setAppLoading', true)
      const brandSlug = this.$route.params.brand_slug
      const sneakerSlug = this.$route.params.sneaker_slug

      await axios
        .get(`/api/v1/sneakers/${brandSlug}/${sneakerSlug}`)
        .then(response => {
          this.sneaker = response.data
          document.title = this.sneaker.name + ' | Dirty Kicks'
        })
        .catch(error => {
          console.log(error)
        })
      this.$store.commit('setAppLoading', false)
    },
    addToCart () {
      if (isNaN(this.quantity) || this.quantity < 1) {
        this.quantity = 1
      }
      const item = {
        sneaker: this.sneaker,
        quantity: this.quantity
      }
      this.$store.commit('addToCart', item)
      toast({
        message: this.sneaker.name + ' added to cart!',
        type: 'is-success',
        position: 'bottom-center',
        duration: 3000,
        pauseOnHover: true,
        dismissible: true
      })
    }
  }
}
</script>

<style lang="scss">
#sneaker-title {
  margin-bottom: auto;
}
</style>
