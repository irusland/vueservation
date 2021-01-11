<template>
  <div class="container">
    <b-form-group v-for="(restaurant, i) in restaurants">
      <b-card
        :title="restaurant.address">
          <b-form-group>
              <span v-if="!restaurant.available" class="text-danger">unavailable</span>
              <span v-if="restaurant.available" class="text-success">
                available
                <span class="text-primary">{{ formatWorkingHours(restaurant.working_hours) }}
                </span>
              </span>
          </b-form-group>
        <image-holder
          v-if="restaurant.available"
          :restaurant="restaurant">
        </image-holder>
      </b-card>
    </b-form-group>
  </div>
</template>

<script>
import axios from 'axios';
import ImageHolder from './ImageHolder';


export default {
  name: 'Restaurants',
  data() {
    return {
      restaurants: [],
    };
  },
  components: {
    ImageHolder,
  },
  methods: {
    async getRestaurants() {
      await axios.get(`${process.env.VUE_APP_API}/restaurants`)
        .then((res) => {
          this.restaurants = [];
          res.data.forEach((restaurantData) => {
            this.getRestaurantInfo(restaurantData.id).then((r) => {
              this.restaurants.push(r);
            });
          });
        })
        .catch((error) => {
          console.error(error);
        });
    },
    async getRestaurantInfo(id) {
      return await axios
        .get(`${process.env.VUE_APP_API}/restaurants/data`, {params: {id}})
        .then((res) => res.data);
    },
    formatWorkingHours(wh) {
      return `from ${wh[0]} to ${wh[1]}`;
    },
  },
  created() {
    this.getRestaurants();
  },
};
</script>

<style scoped>

</style>
