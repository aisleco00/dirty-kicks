import { createStore } from 'vuex'

export default createStore({
  state: {
    cart: {
      items: []
    },
    userAuthenticated: false,
    token: '',
    appLoading: false
  },
  mutations: {
    initializeStore (state) {
      if (localStorage.getItem('cart')) {
        state.cart = JSON.parse(localStorage.getItem('cart'))
      } else {
        localStorage.setItem('cart', JSON.stringify(state.cart))
      }
      if (localStorage.getItem('token')) {
        state.token = localStorage.getItem('token')
        state.userAuthenticated = true
      } else {
        state.token = ''
        state.userAuthenticated = false
      }
    },
    addToCart (state, item) {
      const cartExists = state.cart.items.filter(i => i.sneaker.id === item.sneaker.id)

      if (cartExists.length) {
        cartExists[0].quantity = parseInt(cartExists[0].quantity) + parseInt(item.quantity)
      } else {
        state.cart.items.push(item)
      }
      localStorage.setItem('cart', JSON.stringify(state.cart))
    },
    setAppLoading (state, status) {
      state.appLoading = status
    },
    setUserToken (state, token) {
      state.token = token
      state.userAuthenticated = true
    },
    deleteUserToken (state) {
      state.token = ''
      state.userAuthenticated = false
    },
    emptyCart (state) {
      state.cart = { items: [] }
      localStorage.setItem('cart', JSON.stringify(state.cart))
    }
  },
  actions: {
  },
  modules: {
  }
})
