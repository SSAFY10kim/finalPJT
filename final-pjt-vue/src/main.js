import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'

// bootstrap 3
// npm install vue bootstrap bootstrap-vue-3

// import BootstrapVue3 from 'bootstrap-vue-3';
// import 'bootstrap/dist/css/bootstrap.css'
// import 'bootstrap-vue-3/dist/bootstrap-vue-3.css'


// vuetify
// npm i vuetify

// import 'vuetify/styles'
// import { createVuetify } from 'vuetify'
// import * as components from 'vuetify/components'
// import * as directives from 'vuetify/directives'

const app = createApp(App)
const pinia = createPinia()

// vuetify
// const vuetify = createVuetify({
//     components,
//     directives,
//   })

pinia.use(piniaPluginPersistedstate)
// app.use(createPinia())
app.use(pinia)
app.use(router)

// bootstrap 3
// app.use(BootstrapVue3)

// vuetify
// app.use(vuetify)

app.mount('#app')
