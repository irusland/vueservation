<template>
  <div class="">
    <b-table small bordered striped hover :items="items"></b-table>
<!--    <table class="table table-hover text-center">-->
<!--      <thead>-->
<!--      <tr>-->
<!--        <th scope="col">id</th>-->
<!--        <th scope="col">name</th>-->
<!--        <th scope="col">email</th>-->
<!--        <th scope="col">time</th>-->
<!--        <th scope="col">restaurant</th>-->
<!--        <th scope="col">comment</th>-->
<!--        <th scope="col">is validated?</th>-->
<!--        <th></th>-->
<!--      </tr>-->
<!--      </thead>-->
<!--      <tbody>-->
<!--      <tr v-for="(item, index) in items" :key="index">-->
<!--        <td>{{ item.id }}</td>-->
<!--        <td>{{ item.user.name }}</td>-->
<!--        <td>{{ item.user.email }}</td>-->
<!--        <td>{{ item.time }}</td>-->
<!--        <td>{{ item.restaurant }}</td>-->
<!--        <td>{{ item.comment }}</td>-->
<!--        <td>-->
<!--          <span v-if="item">Yes</span>-->
<!--          <span v-else>No</span>-->
<!--        </td>-->
<!--&lt;!&ndash;        <td>&ndash;&gt;-->
<!--&lt;!&ndash;          <button&ndash;&gt;-->
<!--&lt;!&ndash;            type="button"&ndash;&gt;-->
<!--&lt;!&ndash;            class="btn btn-warning btn-sm"&ndash;&gt;-->
<!--&lt;!&ndash;            v-b-modal.book-update-modal&ndash;&gt;-->
<!--&lt;!&ndash;            @click="editBook(book)">&ndash;&gt;-->
<!--&lt;!&ndash;            Update&ndash;&gt;-->
<!--&lt;!&ndash;          </button>&ndash;&gt;-->
<!--&lt;!&ndash;          <button&ndash;&gt;-->
<!--&lt;!&ndash;            type="button"&ndash;&gt;-->
<!--&lt;!&ndash;            class="btn btn-danger btn-sm"&ndash;&gt;-->
<!--&lt;!&ndash;            @click="onDeleteBook(book)">&ndash;&gt;-->
<!--&lt;!&ndash;            Delete&ndash;&gt;-->
<!--&lt;!&ndash;          </button>&ndash;&gt;-->
<!--&lt;!&ndash;        </td>&ndash;&gt;-->
<!--      </tr>-->
<!--      </tbody>-->
<!--    </table>-->
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: 'Orders',
  data() {
    return {
      items: [],
    };
  },
  methods: {
    getOrders() {
      axios.get(`${process.env.VUE_APP_API}/orders`)
        .then((res) => {
          this.items = [];
          res.data.forEach((item) => {
            const data = {
              id: item.id,
              name: item.user.name,
              email: item.user.email,
              time: item.time,
              restaurant: item.restaurant,
              comment: item.comment,
              confirmed: item.is_validated,
              _rowVariant: !item.is_validated ? 'danger' : 'success',
            }
            this.items.push(data);
          });
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getOrders();
  },
};
</script>

<style scoped>

</style>
