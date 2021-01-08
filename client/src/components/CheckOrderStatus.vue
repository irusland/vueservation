<template>
  <div class="container">
    <b-card>
      <p>Your order: <b>{{ order_id }}</b></p>
      <p v-if="!info.is_validated">Check your email <span class="text-info">{{ info.user.email }}</span> for reservation
        <span class="text-info">confirmation</span></p>
      <p v-if="info.is_validated">{{ info.user.name }}, Your order <span class="text-success font-weight-bold">confirmed</span>, we will
        be waiting for you at <span class="text-primary">{{ info.time }}</span> in restaurant <b>{{restaurant.address}}</b></p>
    </b-card>
  </div>
</template>

<script>
import axios from 'axios';
import ImageHolder from '@/components/ImageHolder';

const apiUrl = 'http://0.0.0.0:8000';

export default {
  name: 'check',

  components: {
    ImageHolder,
  },
  data() {
    return {
      order_id: null,
      info: null,
      restaurant: null,
      pictures: null,
      apiUrl,
    };
  },
  methods: {
    setRestaurantInfo(id) {
      axios.get(`${apiUrl}/restaurants/data`,
        { params: { id } })
        .then((res) => {
          this.restaurant = res.data;
          this.pictures = this.restaurant.pictures;
        });
    },
  },
  created() {
    this.order_id = localStorage.getItem('order_id');
    axios.get(`${apiUrl}/orders/${this.order_id}`)
      .then((res) => {
        this.info = res.data;
        this.setRestaurantInfo(this.info.restaurant);
      })
      .catch((error) => {
        console.error(error);
      });
  },
};
</script>

<style scoped>

</style>
