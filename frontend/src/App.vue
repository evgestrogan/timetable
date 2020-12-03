<template>
    <b-container id="app" fluid class="h-100 w-100">
      <b-row>
        <b-col class="text-left"><a class="btn btn-info button-menu" @click="back_button()">НАЗАД</a></b-col>
        <b-col class="text-center"><router-link class="btn btn-info button-menu" :to="{ name: 'Menu' }">НА ГЛАВНУЮ</router-link></b-col>
        <b-col class="text-right"><a class="btn btn-info button-menu" href="#">ИНФО-ПОРТАЛ</a></b-col>
      </b-row>
      <router-view class="text-center"></router-view>
    </b-container>
</template>

<script>
export default {
  name: 'App',
  methods: {
    back_button(){
      this.$router.go(-1)
    }
  },
}
</script>

<style scoped>
.button-menu {
    height: 80px;
    margin-bottom: 0px;
    margin-top: 0px;
    font-size: 25px;
    color: white;
    padding-top: 20px;
    width: 210px;
}
</style>
