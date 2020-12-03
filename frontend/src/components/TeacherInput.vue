<template>
  <b-row class="h-100">
    <b-input-group class="my-auto">
      <b-form-input v-model="personal_number" :state="numberState" type="number" min="100" max="999" placeholder="Введите ваш личный код" class="inp-form"></b-form-input>
      <router-link class="btn button-timetable" :class="numberState ? 'btn-success' : 'btn-danger'" :to="numberState ? {name: 'TeacherTimetable', params: {'personal_number': personal_number}} : ''">Подтвердить</router-link>
    </b-input-group>
  </b-row>
</template>

<script>
export default {
  name: "TeacherInput",
  data: () => ({
    personal_number: '',
  }),
  computed: {
    numberState() {
      return this.personal_number.length === 3 ? true : false
    }
  },
}
</script>

<style scoped>
.inp-form {
  font-size: 40px;
  text-align: center;
}

input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

.button-timetable {
    width: 300px;
    font-size: 30px;
    color: white;
}
</style>