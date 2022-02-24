<template>
  <div class="account-page">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title mb-5">Welcome back, {{ username }}</h1>
      </div>
      <br>
      <div class="column is-8 is-offset-2">
        <h3 class="subtitle is-size-4"><strong>My Orders</strong></h3>
        <OrderOverview
          v-for="order in orders"
          v-bind:key="order.id"
          v-bind:order="order" />
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import OrderOverview from '@/components/OrderOverview.vue'
export default {
  name: 'Account',
  components: {
    OrderOverview
  },
  data () {
    return {
      orders: [],
      username: localStorage.getItem('username')
    }
  },
  mounted () {
    document.title = 'My Account | Dirty Kicks'
    this.getUserOrder()
  },
  methods: {
    async getUserOrder () {
      this.$store.commit('setAppLoading', true)
      await axios
        .get('/api/v1/orders/')
        .then(response => {
          this.orders = response.data
        })
        .catch(err => {
          console.log(err)
        })
      this.$store.commit('setAppLoading', false)
    }
  }
}
</script>
