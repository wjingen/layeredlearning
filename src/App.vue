<template>
  <div class="app">
    <MainPage />
    <!-- <SpeechToText /> -->
  </div>
</template>

<script>
import MainPage from "./components/MainPage.vue";
// import SpeechToText from "./components/SpeechToText.vue";
export default {
  components: {
    MainPage,
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
