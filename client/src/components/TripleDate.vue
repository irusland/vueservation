<template>
  <div class="container">
    <date-picker
      v-model="time1"
      valueType="format"
      @change="onChange()"
    ></date-picker>
    <date-picker v-model="time2" type="datetime"></date-picker>
    <date-picker v-model="time3" range></date-picker>
  </div>
</template>

<script>
import DatePicker from "vue2-datepicker";
import "vue2-datepicker/index.css";

export default {
  name: "Ping",
  components: { DatePicker },
  data() {
    return {
      time1: new Date(2016, 9, 16),
      time2: null,
      time3: null,
      Disabled: {
        dates: [
          new Date(2016, 9, 16),
          new Date(2016, 9, 17),
          new Date(2016, 9, 18)
        ],
      },
    };
  },
  methods: {
    onChange() {
      console.log(this.time1);
    },
    getDisabled() {
        console.log("asdasdasdadasd");
        return { to: this.time1 };
    }
  },
};
</script>
