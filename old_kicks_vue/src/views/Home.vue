<template>
  <div class="home">
    <br>
    <section class="hero is-large has-bg-img is-transparent">
      <div class="hero-body"></div>
    </section>
    <br>
    <div class="columns is-multiline">
      <div class="column is-12">
        <h3 class="title">Featured Sneakers</h3>
      </div>
    </div>
    <section class="columns is-justify-content-center">
      <FeaturedSneaker
        v-for="sneaker in featuredSneakers"
        v-bind:key="sneaker.id"
        v-bind:sneaker="sneaker"/>
    </section>
  </div>
</template>

<script>
import axios from 'axios'
import FeaturedSneaker from '@/components/FeaturedSneaker'

export default {
  name: 'Home',
  data () {
    return {
      featuredSneakers: []
    }
  },
  components: {
    FeaturedSneaker
  },
  mounted () {
    this.getFeaturedSneakers()
    document.title = 'Home | Dirty Kicks'
  },
  methods: {
    async getFeaturedSneakers () {
      this.$store.commit('setAppLoading', true)
      await axios
        .get('/api/v1/featured-sneakers/')
        .then(response => {
          this.featuredSneakers = response.data
        })
        .catch(error => {
          console.log(error)
        })
      this.$store.commit('setAppLoading', false)
    }
  }
}
</script>

<style lang="scss">
.has-bg-img {
  background: url('../assets/banner.png') center center;
  background-size: cover;
}
.is-transparent {
  opacity: 0.7;
}
</style>
