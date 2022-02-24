<template>
  <router-link v-bind:to="sneaker.get_absolute_url" class="p-3 is-flex">
    <div class="card">
      <div class="card-image">
        <figure class="image">
          <img v-bind:src="sneaker.get_image" alt="sneaker image">
        </figure>
      </div>
      <div class="card-content has-text-centered">
        <div class="media">
          <div class="media-content">
            <p class="title is-5">{{ sneaker.name }}</p>
            <p class="subtitle is-6">${{ sneaker.price }}</p>
          </div>
        </div>
      </div>
    </div>
  </router-link>
</template>

<script>
export default {
  name: 'FeaturedSneaker',
  props: {
    sneaker: Object
  }
}
</script>
