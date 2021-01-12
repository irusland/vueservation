<template>
  <div class="container">
    <alert :message=message v-if="showMessage"></alert>
    <b-card v-if="info">
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
import Alert from './Alert';

export default {
  name: 'check',

  components: {
    ImageHolder,
    alert: Alert,
  },
  data() {
    return {
      order_id: null,
      info: null,
      restaurant: null,
      pictures: null,
      message: null,
      showMessage: false,
    };
  },
  methods: {
    setRestaurantInfo(id) {
      axios.get(`${process.env.VUE_APP_API}/restaurants/data`,
        { params: { id } })
        .then((res) => {
          this.restaurant = res.data;
          this.pictures = this.restaurant.pictures;
        });
    },
  },
  created() {
    this.order_id = localStorage.getItem('order_id');
    axios.get(`${process.env.VUE_APP_API}/orders/${this.order_id}`)
      .then((res) => {
        if (res.data.status === 'FAILED') {
          this.message = 'You have not ordered any thing yet';
          this.showMessage = true;
          localStorage.removeItem('order_id');
        } else {
          this.info = res.data;
          this.setRestaurantInfo(this.info.restaurant);
          this.showMessage = false;
        }
      })
      .catch((error) => {
        console.error(error);
      });
  },
};
</script>

<style scoped>

</style>
