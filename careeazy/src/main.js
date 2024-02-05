import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import router from './router'
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

const vuetify = createVuetify({
  components,
  directives,
})


import App from './App.vue'

const app = createApp(App)

app.use(router).use(vuetify)
app.mount('#app')