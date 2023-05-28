<template>
  <div class="app">
    <!-- <MainPage /> -->
    <TestComponent />
    <!-- <SpeechToText /> -->
  </div>
</template>

<script>
// import MainPage from "./components/MainPage.vue";
import TestComponent from "./components/TestComponent.vue";
// import SpeechToText from "./components/SpeechToText.vue";
export default {
  components: {
    // MainPage,
    TestComponent,
    // SpeechToText,
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,400;0,500;1,700&display=swap");
.app {
  font-family: "Roboto", sans-serif;
}
</style>
