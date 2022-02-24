<template>
  <div id="main">
    <Navbar />
    <section class="section">
      <router-view/>
    </section>
    <footer class="footer">
      <div class="content has-text-centered">
        <p><a href="http://www.github.com/defitjo/dirty-kicks" target="_blank">Devon</a></p>
      </div>
    </footer>
  </div>
</template>

<script>
import axios from 'axios'
import Navbar from '@/components/Navbar.vue'
export default {
  components: {
    Navbar
  },
  beforeCreate () {
    this.$store.commit('initializeStore')
    const token = this.$store.state.token
    if (token) {
      axios.defaults.headers.common.Authorization = 'Token ' + token
    } else {
      axios.defaults.headers.common.Authorization = ''
    }
  }
}
</script>

<style lang="scss">
@import '../node_modules/bulma';

#app {
  display: flex;
  min-height: 100vh;
  flex-direction: column;
}

#main {
  flex: 1;
  display: flex;
  flex-direction: column;
}

footer {
  margin-top: auto;
}
</style>
