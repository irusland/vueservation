<template>
  <div class="container">
    <b-form @submit="onSubmit">
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
      <b-form-group>
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
                required
                id="restaurant"
                v-model="selected"
                :select-size="1"
                :options="options"
                @change="setRestaurantInfo"
              >
              </b-form-select>
              <image-holder :restaurant="restaurant"></image-holder>
            </b-form-group>

            <b-form-group
              label="Time"
              label-for="time"
              label-cols-sm="3"
              label-align-sm="right"
            >
              <date-picker
                v-model="time"
                valueType="format"
                type="time"
                :input-attr="{required: 'true'}"
                :disabled="!restaurant"
                format="HH:mm"
                :time-picker-options="timePickerOptions"
              ></date-picker>
            </b-form-group>

            <b-form-group
              label="Comment"
              label-for="comment"
              label-cols-sm="3"
              label-align-sm="right"
            >
              <b-form-input id="comment" v-model="comment"></b-form-input>
            </b-form-group>
          </b-form-group>
        </b-card>
      </b-form-group>
      <b-form-group>
        <b-button type="submit" variant="success">Submit</b-button>
      </b-form-group>
    </b-form>
    <b-modal ref="validationModal"
             id="validation-modal"
             title="New order"
             hide-footer>
      Order created, you will be automatically redirected
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import ImageHolder from '@/components/ImageHolder';
import DatePicker from 'vue2-datepicker';
import 'vue2-datepicker/index.css';


export default {
  name: 'Reservation',
  components: {
    DatePicker,
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
      time: null,
      timePickerOptions: null,
      comment: null,
      order_id: null,
      is_validated: null,
    };
  },
  methods: {
    onSubmit(event) {
      event.preventDefault();
      this.$refs.validationModal.show();
      const data = {
        email: this.email,
        name: this.name,
        restaurant_id: this.restaurant.id,
        time: this.time,
        comment: this.comment,
      };
      axios.post(`${process.env.VUE_APP_API}/orders`, data)
        .then((res) => {
          this.order_id = res.data.id;
          this.is_validated = res.data.is_validated;
          localStorage.setItem('order_id', res.data.id);
          this.$router.push({
            name: 'Check',
          });
        })
        .catch((error) => {
          console.error(error);
        });
    },
    getRestaurants() {
      axios.get(`${process.env.VUE_APP_API}/restaurants`)
        .then((res) => {
          this.options = [];
          res.data.forEach((restaurantData) => {
            const data = {
              value: restaurantData.id,
              text: restaurantData.address,
              disabled: !restaurantData.available,
            };
            this.options.push(data);
          });
        })
        .catch((error) => {
          console.error(error);
        });
    },
    setRestaurantInfo(id) {
      axios.get(`${process.env.VUE_APP_API}/restaurants/data`,
        {params: {id}})
        .then((res) => {
          this.restaurant = res.data;
          this.pictures = this.restaurant.pictures;
          this.setWorkingHours();
        });
    },
    setWorkingHours() {
      this.timePickerOptions = {
        start: this.restaurant.working_hours[0],
        step: '00:30',
        end: this.restaurant.working_hours[1],
      };
    }
  },
  computed: {
    emailValidate() {
      const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      this.isNameAutofilled = false;
      if (!re.test(this.email)) {
        return false;
      }
      const path = `${process.env.VUE_APP_API}/users`;
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
