<template>
  <div class="sign-in-page">
    <div class="columns">
      <div class="column is-4 is-offset-4">
        <h1 class="title">Sign In</h1>
        <form class="box" @submit.prevent="submitSignIn">
          <div class="field">
            <label>Username</label>
            <div class="control has-icons-left">
              <input type="text" class="input" v-model="username" required>
              <span class="icon is-small is-left">
                <i class="fas fa-user"></i>
              </span>
            </div>
          </div>
          <div class="field">
            <label>Password</label>
            <div class="control has-icons-left">
              <input type="password" class="input" v-model="password" required>
              <span class="icon is-small is-left">
                <i class="fas fa-lock"></i>
              </span>
            </div>
          </div>
          <div class="notification is-danger" v-if="error.length">
            <p v-for="err in error" v-bind:key="err">{{ err }}</p>
          </div>
          <div class="field">
            <div class="control">
              <button class="button is-primary">Sign In</button>
            </div>
          </div>
          <hr>
          <p class="has-text-centered is-size-7">Don't have an account? <router-link to="/sign-up">Click here to sign up</router-link></p>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'SignIn',
  data () {
    return {
      username: '',
      password: '',
      error: []
    }
  },
  mounted () {
    document.title = 'Sign In | Dirty Kicks'
  },
  methods: {
    async submitSignIn () {
      axios.defaults.headers.common.Authorization = ''
      localStorage.removeItem('token')
      const formData = {
        username: this.username,
        password: this.password
      }
      await axios
        .post('/api/v1/token/login/', formData)
        .then(response => {
          const token = response.data.auth_token
          this.$store.commit('setUserToken', token)
          axios.defaults.headers.common.Authorization = 'Token ' + token
          localStorage.setItem('token', token)
          localStorage.setItem('username', this.username)
          const toRoute = this.$route.query.to || '/cart'
          this.$router.push(toRoute)
        })
        .catch(err => {
          if (err.response) {
            for (const value in err.response.data) {
              this.error.push(`${value}: ${err.response.data[value]}`)
            }
          } else {
            this.error.push('Whoops! There was an error, please try again')
            console.log(JSON.stringify(err))
          }
        })
    }
  }
}
</script>
