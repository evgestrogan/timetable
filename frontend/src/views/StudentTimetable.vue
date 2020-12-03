<template>
  <b-row class="w-100 h-75">
    <b-col v-show="show" class="h-100 align-content-center">
      <h3 v-if="type_timetable === 'student'" class="text-date"> Расписание для {{ params.number_group }} группы</h3>
      <h3 v-if="type_timetable === 'teacher'" class="text-date"> Расписание для преподавателя c личным номером: {{ params.personal_number }}</h3>
      <b-row class="h-100">
        <b-col cols="1" class="my-auto">
          <b-img type="button" @click="get_past_week('back')" src='/left.png'></b-img>
        </b-col>
        <b-col>
          <b-row>
            <b-col cols="4" v-for="(lessons, day, day_key) of list_lessons" :key="'day' + day_key">
              <b-row :class="'color' + day_key" class="justify-content-center ">
                <h5>{{day}}</h5>
              </b-row>
              <b-row v-for="(lesson, lesson_key) in lessons" :key="'lesson' + lesson_key" class="justify-content-md-center" :class="'row' + lesson_key%2">
                <b-col cols="2">
                  {{lesson.time}}
                </b-col>
                <b-col cols="8">
                  <b-row class="justify-content-md-center">
                    {{lesson.subject}}
                  </b-row>
                  <b-row class="justify-content-md-center">
                    <div v-for="(employment, employment_key) in lesson.employment" :key="'employment' + employment_key" class="px-2">
                      {{employment.type_subject}}{{employment.number_subject}}
                    </div>
                  </b-row>
                  <b-row v-if="type_timetable === 'student'" class="justify-content-md-center">
                    <div v-for="(teacher, teacher_key) in lesson.teacher" :key="'teacher' + teacher_key" class="px-2">
                      {{teacher.last_name}}
                    </div>
                  </b-row>
                  <b-row v-if="type_timetable === 'teacher'" class="justify-content-md-center">
                      {{lesson.group}}
                  </b-row>
                </b-col>
                <b-col cols="2">
                  <b-row v-for="(classroom, classroom_key) in lesson.classroom" :key="'classroom' + classroom_key">
                    {{classroom.number_classroom}}
                  </b-row>
                </b-col>
              </b-row>
            </b-col>
          </b-row>
        </b-col>
        <b-col cols="1" class="my-auto">
          <b-img type="button" @click="get_past_week('next')" src='/right.png'></b-img>
        </b-col>
      </b-row>
    </b-col>
  </b-row>
</template>

<script>
const axios = require('axios');

export default {
  name: "StudentTimetable",
  data: () => ({
    params: {},
    teacher_last_name: '',
    list_lessons: {},
    type_timetable: null,
    show: false,
    date: new Date()
  }),
  methods:{
    normalize_data_list(response){
      for (const lesson of response) {
        if (!(lesson.date in this.list_lessons)){
          this.list_lessons[lesson.date] = []
        }

        this.list_lessons[lesson.date].push(lesson)
      }
      this.show = true
    },
    normalize_date(){
      let dd = String(this.date.getDate()).padStart(2, '0');
      let mm = String(this.date.getMonth() + 1).padStart(2, '0');
      let yyyy = this.date.getFullYear();
      return  yyyy + '-' + mm + '-' + dd;
    },
    get_lessons_for_week(){
      this.params['date'] = this.normalize_date()
      axios({
        method: "get",
        url: 'http://127.0.0.1:8000/api/lessons/',
        params: this.params
      }).then(response => (this.normalize_data_list(response.data)))
    },
    get_past_week(type){
      this.show = false
      this.list_lessons = {}
      if(type === 'back') {
        this.date.setDate(this.date.getDate() - 7)
      }
      if(type === 'next') {
        this.date.setDate(this.date.getDate() + 7)
      }
      this.get_lessons_for_week()
    }
  },
  created() {
    if (this.$route.name === 'TeacherTimetable') {
      this.type_timetable = 'teacher'
      this.params['personal_number']  =this.$route.params.personal_number
    }
    else {
      this.type_timetable = 'student'
      this.params['number_group'] = this.$route.params.number_group
    }
    this.get_lessons_for_week()
  }
}
</script>

<style scoped>
.text-date {
    margin-top: 40px;
    font-weight: lighter;
    font-size: 30px;
    text-transform: uppercase;
    text-align: center;
    color: white;
}
.color0 {
    background-color: #0A9FB0;
}

.color1 {
    background-color: #0C69DF;
}

.color2 {
    background-color: #EB2C35;
}

.color3 {
    background-color: #00A01D;
}

.color4 {
    background-color: #B04CB7;
}

.color5 {
    background-color: #E7AF18;
}

.color6 {
    background-color: thistle;
}

.color0, .color1, .color2, .color3, .color4, .color5, .color6, .color7 {
    margin: 0;
    margin-bottom: 10px;
    margin-top: 20px;
}

.row1, .row0 {
    height: 70px;
    margin: 0;
}

.row1 {
	background-color: white;
}

.row0 {
	background-color: #F0F0F0;
}
</style>