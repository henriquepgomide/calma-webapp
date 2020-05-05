<template>
  <div id="personcard">
    <div class="columns">
      <div class="column is-one-fifth">
        <figure class="image is-128x128">
          <img
            class="is-rounded"
            :src="`${publicPath}img/team/${photo_link}`"
          />
        </figure>
      </div>
      <div class="column">
        <h1 class="title">{{ name }}</h1>
        <p class="is-size-5">{{ description }}</p>
        <p class="is-size-5"><a href="link">Link para currículo</a></p>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  props: {
    name: String,
    photo_link: String,
    description: String,
    link: String
  },
  data() {
    return {
      publicPath: process.env.BASE_URL
    };
  }
};
</script>
