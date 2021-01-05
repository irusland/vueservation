<template>
  <div class="container">
    <b-form @submit="onSubmit" @reset="onReset">
      <b-form-group id="form-email-group"
                    label="Your email"
                    label-for="form-email-input"
                    :invalid-feedback="emailInvalid"
                    description="Let us know your name for discounts and confirmation.">
        <b-form-input id="form-email-input"
                      type="text"
                      v-model="email"
                      required
                      :state="emailValidate"
                      placeholder="example@mail.ru">
        </b-form-input>
      </b-form-group>

      <b-form-group id="form-name-group"
                    label="Name"
                    label-for="form-name-input">
        <b-form-input id="form-name-input"
                      type="text"
                      v-model="name"
                      required
                      placeholder="Ваше имя"
                      :disabled=isNameAutofilled>
        </b-form-input>
      </b-form-group>
      <b-card bg-variant="light">
        <b-form-group
          label-cols-lg="3"
          label="Reservation"
          label-size="lg"
          label-class="font-weight-bold pt-0"
          class="mb-0"
        >
          <b-form-group
            label="Choose restaurant"
            label-for="restaurant"
            label-cols-sm="3"
            label-align-sm="right"
          >
            <b-form-select
              id="restaurant"
              v-model="selected"
              :select-size="1"
              :options="options"
              @change="setRestaurantInfo"
            >
            </b-form-select>
            <p>{{ restaurant }}</p>
            <b-card fluid class="bg-secondary">

<!--              <b-col>-->
<!--                <b-img-->
<!--                  rounded-->
<!--                  fluid-->
<!--                  v-for="picture in pictures"-->
<!--                  :src="apiUrl+'/'+picture"-->
<!--                  :alt="apiUrl+'/'+picture"></b-img>-->
<!--              </b-col>-->
              <image-holder :restaurant="restaurant" :api-url="apiUrl"></image-holder>
            </b-card>

          </b-form-group>

          <b-form-group
            label="City:"
            label-for="nested-city"
            label-cols-sm="3"
            label-align-sm="right"
          >
            <b-form-input id="nested-city"></b-form-input>
          </b-form-group>

          <b-form-group
            label="State:"
            label-for="nested-state"
            label-cols-sm="3"
            label-align-sm="right"
          >
            <b-form-input id="nested-state"></b-form-input>
          </b-form-group>

          <b-form-group
            label="Country:"
            label-for="nested-country"
            label-cols-sm="3"
            label-align-sm="right"
          >
            <b-form-input id="nested-country"></b-form-input>
          </b-form-group>
        </b-form-group>
      </b-card>
      <b-button type="submit" variant="primary">Submit</b-button>
      <b-button type="reset" variant="danger">Reset</b-button>
    </b-form>
  </div>
</template>

<script>
import axios from 'axios';
import ImageHolder from '@/components/ImageHolder';

const apiUrl = 'http://0.0.0.0:8000';

export default {
  name: 'Reservation',
  components: {
    ImageHolder,
  },
  data() {
    return {
      name: null,
      email: null,
      isNameAutofilled: false,
      restaurant: null,
      selected: null,
      options: [],
      pictures: [],
      apiUrl,
    };
  },
  methods: {
    onSubmit(event) {
      event.preventDefault();
      alert(JSON.stringify(this.form));
    },
    onReset(event) {
      event.preventDefault();
      // Reset our form values
    },
    getRestaurants() {
      axios.get(`${apiUrl}/restaurants`)
        .then((res) => {
          this.options = [];
          res.data.forEach((restaurantData) => {
            const data = {
              value: restaurantData.id,
              text: restaurantData.address,
            };
            this.options.push(data);
          });
        })
        .catch((error) => {
          console.error(error);
        });
    },
    setRestaurantInfo(id) {
      axios.get(`${apiUrl}/restaurants/data`,
        {params: {id}})
        .then((res) => {
          this.restaurant = res.data;
          this.pictures = this.restaurant.pictures;
        });
    },
  },
  computed: {
    emailValidate() {
      const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      this.isNameAutofilled = false;
      if (!re.test(this.email)) {
        return false;
      }
      const path = `${apiUrl}/users`;
      axios.get(path, {params: {email: this.email}})
        .then((res) => {
          if (res.data.name) {
            this.isNameAutofilled = true;
            this.name = res.data.name;
          }
        })
        .catch((error) => {
          console.error(error);
        });
      return true;
    },
    emailInvalid() {
      if (!this.email) {
        return 'Empty email';
      }
      return 'This email is not supported';
    },
  },
  created() {
    this.getRestaurants();
  },
};
</script>

<style scoped>

</style>
