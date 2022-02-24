<template>
  <div class="sneaker-brand">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h3 class="is-size-2 has-text-centered">{{ brand.name }}</h3>
      </div>
      <FeaturedSneaker
        v-for="sneaker in brand.sneakers"
        v-bind:key="sneaker.id"
        v-bind:sneaker="sneaker" />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'
import FeaturedSneaker from '@/components/FeaturedSneaker'
export default {
  name: 'Brand',
  components: {
    FeaturedSneaker
  },
  data () {
    return {
      brand: {
        sneakers: []
      }
    }
  },
  mounted () {
    this.getBrand()
  },
  watch: {
    $route (to, from) {
      if (to.name === 'Brand') {
        this.getBrand()
      }
    }
  },
  methods: {
    async getBrand () {
      const brandSlug = this.$route.params.brand_slug
      this.$store.commit('setAppLoading', true)
      await axios
        .get(`/api/v1/sneakers/${brandSlug}/`)
        .then(response => {
          this.brand = response.data
          document.title = this.brand.name + ' | Dirty Kicks'
        })
        .catch(error => {
          console.log(error)
          toast({
            message: 'Error, please try again :(',
            type: 'is-danger',
            position: 'bottom-center',
            duration: 3000,
            pauseOnHover: true,
            dismissible: true
          })
        })
      this.$store.commit('setAppLoading', false)
    }
  }
}
</script>
