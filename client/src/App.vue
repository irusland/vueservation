<template>
  <div id="app">
<!--    <img src="./assets/logo.png">-->
    <h1 v-if="checkapi()"></h1>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
  methods: {
    checkapi() {
      console.log(process.env.VUE_APP_API);
      console.log(process.env);
      console.log(process);
      return true;
    },
  },
};
</script>

<style>
#app {
  /*font-family: 'Avenir', Helvetica, Arial, sans-serif;*/
  /*-webkit-font-smoothing: antialiased;*/
  /*-moz-osx-font-smoothing: grayscale;*/
  /*text-align: center;*/
  color: #2c3e50;
  margin-top: 60px;
}
</style>
