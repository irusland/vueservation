<template>
  <div>
    <b-card title="Main" no-body>
      <b-card-header header-tag="nav">
        <b-nav card-header tabs>
          <b-nav-item to="/restaurants" exact exact-active-class="active">Restaurants</b-nav-item>
          <b-nav-item to="/reservation" exact exact-active-class="active">Reserve</b-nav-item>
          <b-nav-item to="/check" exact exact-active-class="active">Check</b-nav-item>
        </b-nav>
      </b-card-header>

      <b-card-body>
        <router-view></router-view>
      </b-card-body>
    </b-card>
  </div>
</template>

<script>
export default {
  name: 'Main',
  data() {
    return {
    };
  },
};
</script>

<style scoped>

</style>
