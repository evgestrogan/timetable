import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    component: () => import('../views/Menu.vue'),
    children: [
      {
        path: '',
        name: 'Menu',
        component: () => import('../components/MenuButton.vue'),
      },
      {
        path: 'student',
        name: 'Student',
        component: () => import('../components/MenuButton.vue'),
      },
      {
        path: 'teacher',
        name: 'Teacher',
        component: () => import('../components/TeacherInput.vue'),
      },
      {
        path: 'student/cadet',
        name: 'Cadet',
        component: () => import('../components/MenuButton.vue'),
      },
      {
        path: 'student/listener',
        name: 'Listener',
        component: () => import('../components/StudentGroupButton.vue'),
      },
      {
        path: 'student/course',
        name: 'Course',
        component: () => import('../components/StudentGroupButton.vue'),
      },
      {
        path: 'student/cadet/:number_course',
        name: 'Number_course',
        component: () => import('../components/StudentGroupButton.vue'),
      },
    ]
  },
  {
    path: '/student/listener/:number_group',
    name: 'ListenerTimetable',
    component: () => import('../views/StudentTimetable.vue'),
  },
  {
    path: '/student/course/:number_group',
    name: 'CourseTimetable',
    component: () => import('../views/StudentTimetable.vue'),
  },
  {
    path: '/student/cadet/:number_course/:number_group',
    name: 'CadetTimetable',
    component: () => import('../views/StudentTimetable.vue'),
  },
  {
    path: '/teacher/:personal_number',
    name: 'TeacherTimetable',
    component: () => import('../views/StudentTimetable.vue'),
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
