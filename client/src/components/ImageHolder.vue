<template>
  <div>
    <b-carousel
      id="carousel-1"
      v-model="slide"
      :interval="4000"
      controls
      indicators
      background="#ababab"
      img-width="1024"
      img-height="480"
      style="text-shadow: 1px 1px 2px #333;"
      @sliding-start="onSlideStart"
      @sliding-end="onSlideEnd"
    >
      <!--      <p>{{restaurant}}</p>-->
      <!--      <p>{{apiUrl}}</p>-->

      <b-carousel-slide v-for="(path, i) in pictures">
        <template #img>
          <img
            class="d-block img-fluid w-100"
            width="1024"
            height="480"
            :src="path"
            :alt="i"
          >
        </template>
      </b-carousel-slide>

      <!--      <b-carousel-slide-->
      <!--        caption="First slide"-->
      <!--        text="Nulla vitae elit libero, a pharetra augue mollis interdum."-->
      <!--        img-src="https://picsum.photos/1024/480/?image=52"-->
      <!--      ></b-carousel-slide>-->

      <!--      &lt;!&ndash; Slides with custom text &ndash;&gt;-->
      <!--      <b-carousel-slide img-src="https://picsum.photos/1024/480/?image=54">-->
      <!--        <h1>Hello world!</h1>-->
      <!--      </b-carousel-slide>-->

      <!--      &lt;!&ndash; Slides with image only &ndash;&gt;-->
      <!--      <b-carousel-slide img-src="https://picsum.photos/1024/480/?image=58"></b-carousel-slide>-->

      <!--      &lt;!&ndash; Slides with img slot &ndash;&gt;-->
      <!--      &lt;!&ndash; Note the classes .d-block and .img-fluid to prevent browser default image alignment &ndash;&gt;-->
      <!--      <b-carousel-slide>-->
      <!--        <template #img>-->
      <!--          <img-->
      <!--            class="d-block img-fluid w-100"-->
      <!--            width="1024"-->
      <!--            height="480"-->
      <!--            src="https://picsum.photos/1024/480/?image=55"-->
      <!--            alt="image slot"-->
      <!--          >-->
      <!--        </template>-->
      <!--      </b-carousel-slide>-->

      <!--      &lt;!&ndash; Slide with blank fluid image to maintain slide aspect ratio &ndash;&gt;-->
      <!--      <b-carousel-slide caption="Blank Image" img-blank img-alt="Blank image">-->
      <!--        <p>-->
      <!--          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse eros felis, tincidunt-->
      <!--          a tincidunt eget, convallis vel est. Ut pellentesque ut lacus vel interdum.-->
      <!--        </p>-->
      <!--      </b-carousel-slide>-->
    </b-carousel>

    <p class="mt-4">
      Slide #: {{ slide }}<br>
      Sliding: {{ sliding }}
    </p>
  </div>
</template>

<script>
export default {
  props: ['restaurant', 'apiUrl'],
  data() {
    return {
      slide: 0,
      sliding: null,
      pictures: [],
    };
  },
  methods: {
    onSlideStart(slide) {
      this.sliding = true;
    },
    onSlideEnd(slide) {
      this.sliding = false;
    },
  },
  created() {
    const paths = this.restaurant.pictures;
    if (paths) {
      this.pictures = paths.map(p => `${this.apiUrl}/${p}`);
    }
  },
};
</script>
