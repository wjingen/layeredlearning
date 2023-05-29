<template>
  <div class="main">
    <div style="display: flex; align-items: center">
      <img src="../../static/logo.png" class="image" />
      <h3>LayeredLearning</h3>
    </div>
    <div class="buttons">
      <p class="links">Login</p>
      <p class="links">Sign Up</p>
    </div>
  </div>
  <v-divider></v-divider>
</template>

<script>
export default {};
</script>

<style scoped>
.main {
  display: flex;
  justify-content: space-around;
}
.buttons {
  display: flex;
}

.image {
  height: 60px;
  width: 60px;
}

.buttons {
  /* background-color: red; */
  width: 20%;
  justify-content: flex-end;
  align-self: center;
}
.buttons .links {
  padding: 0% 5%;
  height: 90%;
  align-self: center;
  transition: transform 0.3s ease-in-out;
}

.buttons .links:hover {
  color: #27374d;
  transform: translateY(-5px);
}
</style>
