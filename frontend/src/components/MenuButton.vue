<template>
  <b-row class="h-100 align-content-center">
    <b-col v-if="course" v-for="(button, link) in buttons_list.Number_course" :key="link">
      <router-link class="btn btn-info button-timetable" :to="{ name: 'Number_course', params: {'number_course': link} }">{{button}}</router-link>
    </b-col>
    <b-col v-if="!course" v-for="(button, link) in buttons_list" :key="button">
      <router-link class="btn btn-info button-timetable" :to="{ name: link }">{{button}}</router-link>
    </b-col>
  </b-row>
</template>

<script>
export default {
  name: "MenuButtonGroup",
  props: {
    buttons_list: Object,
    course: Boolean,
  },
}
</script>

<style scoped>
.button-timetable {
    width: 500px;
    height: 100px;
    font-size: 30px;
    margin-bottom: 0px;
    margin-top: 20px;
    color: white;
    padding-top: 20px;
}
</style>