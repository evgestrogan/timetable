<template>
  <b-row class="h-100 align-content-center">
    <b-col v-if="group" v-for="(group, key) in list_group" :key="key">
      <router-link class="btn btn-info button-timetable" :to="{ name: buttons_list.Link, params: {'number_group': group.number_group} }">{{group.number_group}}</router-link>
    </b-col>
  </b-row>
</template>

<script>
const axios = require('axios');

export default {
  name: "StudentGroupButton",
  props: {
    buttons_list: Object,
    group: Boolean,
  },
  data: () => ({
    list_group: null,
  }),
  created() {
    let type_group
    if (this.$route.name === 'Number_course') {
      type_group = this.$route.params.number_course
    }
    else {
      type_group = this.$route.name
    }
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/api/listgroups/' + type_group,
    })
      .then(response => (this.list_group = response.data))
  }
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
