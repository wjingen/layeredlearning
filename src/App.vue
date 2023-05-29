<template>
  <div class="app">
    <NavBar />
    <!-- <MainPage /> -->
    <!-- <TestComponent /> -->
    <router-view></router-view>
    <!-- <SpeechToText /> -->
  </div>
</template>

<script>
// import MainPage from "./components/MainPage.vue";
import NavBar from "./components/NavBar.vue";
// import TestComponent from "./components/TestComponent.vue";
// import SpeechToText from "./components/SpeechToText.vue";
export default {
  components: {
    // MainPage,
    // TestComponent,
    NavBar,
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,400;0,500;1,700&display=swap");
.app {
  font-family: "Roboto", sans-serif;
  /* font-family: "Inter", sans-serif; */
}
</style>
