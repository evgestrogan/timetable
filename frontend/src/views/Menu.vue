<template>
  <div class="home w-100 h-75">
    <div class="container">
      <marquee span="" style="font-family: arial, helvetica, sans-serif; font-size: 30px; margin-top: 30px;" width="1110px" heigth="10px" bevavior="alternate" direction="left" scrollamount="3.5" scrolldelay="1" loop="loop" hspace="2">
        <p style="color: #FFFFFF; text-decoration: none;">
            <span style="font-family: impact;">БЫТЬ ДОСТОЙНЫМИ ПАМЯТИ ПОБЕДИТЕЛЕЙ !</span>
        </p>
      </marquee>
    </div>
    <router-view :buttons_list="buttons_list[change_page]" :course="course"></router-view>
  </div>
</template>

<script>
import menuButton from '../components/MenuButton'
const axios = require('axios');

export default {
  name: 'Home',
  components:{
    menuButton,
  },
  data: () => ({
    buttons_list: {
      'Menu': {
        'Teacher' : 'Преподаватель',
        'Student': 'Студент',
      },
      'Teacher': {

      },
      'Student': {
        'Cadet': 'Курсаны',
        'Listener': 'Слушатели',
        'Course': 'Курсы ПК',
      },
      'Cadet': {
        'Number_course': {}
      },
      'Number_course': {
        'Link': 'CadetTimetable',
      },
      'Listener': {
        'Link': 'ListenerTimetable',
      },
      'Course': {
        'Link': 'CourseTimetable',
      },
    },
    change_page: '',
    course: false,
  }),
  methods: {
    get_course_list(){
      axios.get('http://127.0.0.1:8000/api/listcourse/')
        .then(response => (this.buttons_list.Cadet.Number_course = response.data))
      this.course = true
    }
  },
  beforeRouteUpdate (to, from, next) {
    this.change_page = to.name
    this.course = false
    next()
    if (this.change_page === 'Cadet') {
      this.get_course_list()
    }
  },
  created() {
    this.change_page = this.$route.name
    this.course = false
    if (this.change_page === 'Cadet') {
      this.get_course_list()
    }
  }

}
</script>
