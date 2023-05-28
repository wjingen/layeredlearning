<template>
  <div class="main">
    <h3>LayeredLearning</h3>
    <div class="buttons">
      <v-btn class="links">Login</v-btn>
      <v-btn class="links">Sign Up</v-btn>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.main {
  display: flex;
  justify-content: space-between;
}
.buttons {
  display: flex;
}

.buttons .links {
  padding: 0% 5%;
  height: 90%;
  align-self: center;
}
</style>
