<template>
  <div class="sneaker-search">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="title">Search</h2>
        <p><strong>Results for: "{{ query }}"</strong></p>
      </div>
      <FeaturedSneaker
        v-for="sneaker in sneakers"
        v-bind:key="sneaker.id"
        v-bind:sneaker="sneaker" />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import FeaturedSneaker from '@/components/FeaturedSneaker'

export default {
  name: 'Search',
  components: {
    FeaturedSneaker
  },
  data () {
    return {
      sneakers: [],
      query: ''
    }
  },
  mounted () {
    document.title = 'Search Results | Dirty Kicks'

    const uri = window.location.search.substring(1)
    const params = new URLSearchParams(uri)

    if (params.get('query')) {
      this.query = params.get('query')
      this.findSneaker()
    }
  },
  methods: {
    async findSneaker () {
      this.$store.commit('setAppLoading', true)
      await axios
        .post('/api/v1/sneakers/search/', { query: this.query })
        .then(response => {
          this.sneakers = response.data
        })
        .catch(error => {
          console.log(error)
        })
      this.$store.commit('setAppLoading', false)
    }
  }
}
</script>
