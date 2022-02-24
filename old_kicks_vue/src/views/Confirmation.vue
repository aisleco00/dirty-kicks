<template>
  <div class="confirmation-page">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="title">Thank You, {{ username }} for your purchase!</h2>
        <p class="subtitle">Your order will be processed shortly</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Confirmation',
  data () {
    return {
      username: localStorage.getItem('username')
    }
  },
  mounted () {
    document.title = 'Confirmation | Dirty Kicks'
  }
}
</script>
