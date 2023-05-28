<template>
  <div class="main">
    <h1>Welcome to LayeredLearning</h1>
    <p>Please enter a topic and select a difficulty level:</p>
    <div class="input-container">
      <v-text-field
        v-model="userQuery"
        placeholder="Enter your topic"
        style="width: 500px"
        :append-icon="icon"
        @click:append="speechRecognition"
      ></v-text-field>
      <p>Otherwise, upload your documents in JPEG, ZIP or PDF:</p>
      <v-file-input
        chips
        multiple
        label="File upload"
        style="width: 500px"
        v-model="uploadedFiles"
        :rules="rules"
        prepend-icon=""
        append-inner-icon="mdi-file"
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
  s
</template>

<script>
// import ExplanationPage from "./ExplanationPage.vue";
export default {
  name: "MainPage",
  components: {
    // ExplanationPage,
  },
  data() {
    return {
      userQuery: "",
      uploadedFiles: [],
      difficultyButton: null,
      recognition: null,
      isRecognizingSpeech: false,
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
  mounted() {
    this.initializeRecognition();
  },
  computed: {
    icon() {
      return this.isRecognizingSpeech
        ? "mdi-loading mdi-spin"
        : "mdi-microphone";
    },
  },
  methods: {
    handleFileUpload() {
      console.log("Uploaded file:", this.uploadedFiles);
    },
    handleSubmit() {
      console.log(this.userQuery);
    },
    initializeRecognition() {
      // Create a new SpeechRecognition object
      this.recognition = new (window.SpeechRecognition ||
        window.webkitSpeechRecognition)();

      // Set the language for speech recognition (optional)
      this.recognition.lang = "en-US";

      // Set the event listeners
      this.recognition.onresult = (event) => {
        const { transcript } = event.results[0][0];
        this.userQuery = transcript;
      };

      this.recognition.onerror = (event) => {
        console.error("Speech recognition error", event.error);
      };

      this.recognition.onend = () => {
        this.isRecognizingSpeech = false; // Toggle off the variable
      };
    },
    speechRecognition() {
      this.isRecognizingSpeech = !this.isRecognizingSpeech;
      if (this.isRecognizingSpeech) {
        this.recognition.start();
      } else {
        this.recognition.stop();
      }
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
