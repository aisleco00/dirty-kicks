<template>
  <div class="sign-up-page">
    <div class="columns">
      <div class="column is-4 is-offset-4">
        <h1 class="title">Create your account</h1>
        <form class="box" @submit.prevent="submitSignUp">
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
          <div class="field">
            <label>Confirm Password</label>
            <div class="control has-icons-left">
              <input type="password" class="input" v-model="confirmPassword" required>
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
              <button class="button is-primary">Sign Up</button>
            </div>
          </div>
          <hr>
          <p class="has-text-centered is-size-7">Already have an account? <router-link to="/sign-in">Click here to sign in</router-link></p>
        </form>
        <div class="terms-page has-text-centered is-size-7">
          <p><strong>Dirty Kicks</strong> is a ecommerce marketplace.</p>
          <p>By signing up, you're accepting the <router-link to="/terms-of-service">terms of service</router-link></p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'
export default {
  name: 'SignUp',
  data () {
    return {
      username: '',
      password: '',
      confirmPassword: '',
      error: []
    }
  },
  mounted () {
    document.title = 'Sign Up | Dirty Kicks'
  },
  methods: {
    submitSignUp () {
      this.error = []
      if (this.username === '') {
        this.error.push('Username must not be blank')
      }
      if (this.username.length <= 3) {
        this.error.push('Username must be at least 4 characters long')
      }
      if (this.password === '') {
        this.error.push('Invalid password')
      }
      if (this.password !== this.confirmPassword) {
        this.error.push('Passwords do not match')
      }
      if (!this.error.length) {
        const formData = {
          username: this.username,
          password: this.password
        }
        axios
          .post('/api/v1/users/', formData)
          .then(response => {
            toast({
              message: 'Account created successfully!',
              type: 'is-success',
              position: 'bottom-center',
              duration: 3000,
              pauseOnHover: true,
              dismissible: true
            })
            this.$router.push('/sign-in')
          })
          .catch(err => {
            if (err.response) {
              for (const value in err.response.data) {
                this.error.push(`${value}: ${err.response.data[value]}`)
              }
              console.log(JSON.stringify(err.response.data))
            } else if (err.message) {
              this.error.push('Whoops! There was an error, please try again')
              console.log(JSON.stringify(err))
            }
          })
      }
    }
  }
}
</script>
