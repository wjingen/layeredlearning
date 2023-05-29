import { createApp } from 'vue'
import App from './App.vue'
import { createRouter, createWebHistory } from 'vue-router'

// Vuetify
import 'vuetify/styles'
import { createVuetify } from '../node_modules/vuetify'
import * as components from 'vuetify/lib/components'
import * as directives from 'vuetify/lib/directives'
import '@mdi/font/css/materialdesignicons.css'

import TestComponentVue from './components/TestComponent.vue'
import ExplanationPageVue from './components/ExplanationPage.vue'
import FakeConversationVue from "./components/FakeConversation.vue"

import pdfjs from "pdfjs-dist"

const vuetify = createVuetify({
  components,
  directives,
})

const router = createRouter({
	routes: [
		{
			path: '/',
			component: TestComponentVue
		},
		{
			path: '/explanation',
			component: ExplanationPageVue,
			props: true
		},
		{
			path: '/fakeconvo',
			component: FakeConversationVue
		},
	], history: createWebHistory(),
})
console.log(router)

createApp(App)
.use(vuetify)
.use(router)
.use(pdfjs)
.mount('#app')