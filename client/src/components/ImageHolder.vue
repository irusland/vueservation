<template>
  <div v-if="restaurant">
    <b-form-group>
      <b-carousel
        id="carousel-1"
        v-model="slide"
        :interval="4000"
        controls
        indicators
        @sliding-start="onSlideStart"
        @sliding-end="onSlideEnd"
      >
        <b-carousel-slide v-for="(path, i) in pictures">
          <template #img>
            <img class="d-block img-fluid w-100" :src="path" :alt="i">
          </template>
        </b-carousel-slide>
      </b-carousel>
    </b-form-group>
    <b-form-group>
      <p class="text-justify text-left"> {{ restaurant.description }} </p>
    </b-form-group>
  </div>
</template>

<script>
export default {
  props: {
    restaurant: Object,
  },
  data() {
    return {
      slide: 0,
      sliding: null,
      pictures: null,
    };
  },
  methods: {
    onSlideStart(slide) {
      this.sliding = true;
    },
    onSlideEnd(slide) {
      this.sliding = false;
    },
    resolvePictures() {
      if (this.restaurant) {
        const paths = this.restaurant.pictures;
        console.log(paths);
        this.pictures = paths.map((path) => {
          if (!path.startsWith('http')) {
            return `${process.env.VUE_APP_API}/pictures/${path}`;
          }
          return path;
        });
      }
    },
  },
  watch: {
    'restaurant': function () {
      this.resolvePictures();
    },
  },
  created() {
    this.resolvePictures();
  },
};
</script>
<style>
</style>
