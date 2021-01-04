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
                      placeholder="Ваше имя">
        </b-form-input>
      </b-form-group>
      <b-button type="submit" variant="primary">Submit</b-button>
      <b-button type="reset" variant="danger">Reset</b-button>
    </b-form>
  </div>
</template>

<script>
import axios from 'axios';

const apiUrl = 'http://0.0.0.0:8000';

export default {
  name: 'Reservation',
  data() {
    return {
      errors: [],
      name: null,
      email: null,
      movie: null,
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
  },
  computed: {
    emailValidate() {
      const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      if (!re.test(this.email)) {
        return false;
      }
      const path = `${apiUrl}/users`;
      axios.get(path, { params: { email: this.email } })
        .then((res) => {
          this.name = res.data.name;
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
};
</script>

<style scoped>

</style>
