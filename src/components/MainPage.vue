<template>
  <div class="main">
    <h1>Welcome to LayeredLearning</h1>
    <p>Please enter a topic and select a difficulty level:</p>
    <div class="input-container">
      <v-text-field
        v-model="userQuery"
        label="Enter your text"
        style="width: 500px"
      ></v-text-field>
      <p>Otherwise, upload your documents in JPEG, ZIP or PDF:</p>
      <v-file-input
        chips
        multiple
        label="File upload"
        style="width: 500px"
        v-model="uploadedFiles"
        :rules="rules"
        @change="handleFileUpload"
      ></v-file-input>
    </div>

    <p>Choose a difficulty level to explain the concept:</p>
    <div class="button-container">
      <v-btn-toggle v-model="difficultyButton" mandatory divided="">
        <v-btn :color="difficultyButton === 0 ? 'blue' : ''">Beginner</v-btn>
        <v-btn :color="difficultyButton === 1 ? 'yellow' : ''"
          >Intermediate</v-btn
        >
        <v-btn :color="difficultyButton === 2 ? 'orange' : ''">Advanced</v-btn>
        <v-btn :color="difficultyButton === 3 ? 'red' : ''">Expert</v-btn>
      </v-btn-toggle>
    </div>

    <v-btn @click="handleSubmit">Submit</v-btn>
  </div>
</template>

<script>
export default {
  name: "MainPage",
  data() {
    return {
      userQuery: "",
      uploadedFiles: [],
      difficultyButton: null,
      rules: [
        (value) => {
          return (
            !value ||
            !value.length ||
            value[0].size < 2000000 ||
            "Avatar size should be less than 2 MB!"
          );
        },
      ],
    };
  },
  methods: {
    handleFileUpload() {
      console.log("Uploaded file:", this.uploadedFiles);
    },
    handleSubmit() {
      console.log(this.userQuery);
    },
  },
};
</script>

<style scoped>
.main {
  background-color: #27374d;
  color: #dde6ed;
  height: 1000px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-family: "Roboto", sans-serif;
}

.input-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
}

.button-container {
  display: flex;
  gap: 10px;
  padding-bottom: 50px;
}

v-btn {
  color: #dde6ed;
}
</style>
