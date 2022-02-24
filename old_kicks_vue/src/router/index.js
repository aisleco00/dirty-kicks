import { createRouter, createWebHistory } from 'vue-router'
import store from '../store'
import Home from '../views/Home.vue'
import Sneaker from '../views/Sneaker.vue'
import Brand from '../views/Brand.vue'
import Cart from '../views/Cart.vue'
import Search from '../views/Search.vue'
import SignUp from '../views/SignUp.vue'
import SignIn from '../views/SignIn.vue'
import Account from '../views/Account.vue'
import Checkout from '../views/Checkout.vue'
import Confirmation from '../views/Confirmation.vue'
import TermsOfService from '../views/TermsOfService.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/sign-in',
    name: 'SignIn',
    component: SignIn
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/my-account',
    name: 'Account',
    component: Account,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/search',
    name: 'Search',
    component: Search
  },
  {
    path: '/terms-of-service',
    name: 'TermsOfService',
    component: TermsOfService
  },
  {
    path: '/cart',
    name: 'Cart',
    component: Cart
  },
  {
    path: '/cart/confirmation',
    name: 'Confirmation',
    component: Confirmation
  },
  {
    path: '/cart/checkout',
    name: 'Checkout',
    component: Checkout,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/:brand_slug/:sneaker_slug',
    name: 'Sneaker',
    component: Sneaker
  },
  {
    path: '/:brand_slug',
    name: 'Brand',
    component: Brand
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.userAuthenticated) {
    next({ name: 'SignIn', query: { to: to.path } })
  } else {
    next()
  }
})

export default router
