<template>
  <nav class="navbar" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <router-link to="/" class="navbar-item" id="dirty-k">
        <img alt="Dirty Kicks Logo" src="../assets/logo1.png">
        <strong>Dirty Kicks</strong>
      </router-link>
      <a class="navbar-burger" role="button" aria-label="menu" aria-expanded="false"
        data-target="mobileBurger" @click="toggleMobileMenu = !toggleMobileMenu">
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
    </div>
    <div id="mobileBurger" class="navbar-menu"
      v-bind:class="{'is-active': toggleMobileMenu}">
      <div class="navbar-end">
        <div class="navbar-item">
          <form action="/search" method="get">
            <div class="field has-addons">
              <div class="control has-icons-left">
                <input type="text" name="query" class="input is-rounded"
                  placeholder="Search for brand">
                  <span class="icon is-small is-left">
                    <i class="fas fa-search"></i>
                  </span>
              </div>
            </div>
          </form>
        </div>
        <div class="navbar-item has-dropdown is-hoverable">
          <a class="navbar-link">
            Brand
          </a>
          <div class="navbar-dropdown">
            <router-link class="navbar-item" to="/adidas">Adidas</router-link>
            <router-link class="navbar-item" to="/jordan">Jordan</router-link>
            <router-link class="navbar-item" to="/nike">Nike</router-link>
          </div>
        </div>
        <router-link class="navbar-item" to="/about">About</router-link>
        <template v-if="$store.state.userAuthenticated">
          <router-link class="navbar-item" to="/my-account">My Account</router-link>
          <router-link class="navbar-item" to="/" @click="logout()">Log Out</router-link>
        </template>
        <template v-else>
          <router-link class="navbar-item" to="/sign-in">Sign In</router-link>
        </template>
        <div class="navbar-item">
          <div class="buttons">
            <router-link to="/cart" class="button is-info is-outlined">
              <span class="icon"><i class="fas fa-shopping-cart"></i></span>
              <span>Cart ({{itemsInCart}})</span>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      toggleMobileMenu: false,
      cart: {
        items: []
      }
    }
  },
  mounted () {
    this.cart = this.$store.state.cart
  },
  computed: {
    itemsInCart () {
      let itemTotal = 0
      for (let i = 0; i < this.cart.items.length; i++) {
        itemTotal += this.cart.items[i].quantity
      }
      return itemTotal
    }
  },
  methods: {
    logout () {
      axios.defaults.headers.common.Authorization = ''
      localStorage.removeItem('token')
      localStorage.removeItem('username')
      localStorage.removeItem('userid')
      this.$store.commit('deleteUserToken')
      this.$router.push('/')
    }
  }
}
</script>

<style lang="scss">
#dirty-k.router-link-active.router-link-exact-active,
#dirty-k:visited,
#dirty-k:hover {
  color: currentColor;
}

.fa-search {
  color: #3e8ed0;
}
</style>
