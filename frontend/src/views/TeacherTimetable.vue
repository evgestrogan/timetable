<template>
  <b-row class="w-100 h-75">
    <b-col v-show="show" class="h-100 align-content-center">
      <h3 class="text-date"> Преподаватель: {{ teacher.last_name }}</h3>
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
export default {
name: "TeacherTimetable"
}
</script>

<style scoped>

</style>