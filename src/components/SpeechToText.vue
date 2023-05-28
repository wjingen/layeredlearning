<template>
  <div>
    <button @click="startListening">Start Listening</button>
    <textarea
      v-model="transcription"
      placeholder="Speak here..."
      rows="5"
    ></textarea>
  </div>
</template>

<script>
export default {
  data() {
    return {
      recognition: null, // SpeechRecognition object
      transcription: "", // Transcribed text
    };
  },
  mounted() {
    this.initializeRecognition();
  },
  methods: {
    initializeRecognition() {
      // Create a new SpeechRecognition object
      this.recognition = new (window.SpeechRecognition ||
        window.webkitSpeechRecognition)();

      // Set the language for speech recognition (optional)
      this.recognition.lang = "en-US";

      // Set the event listeners
      this.recognition.onresult = (event) => {
        const { transcript } = event.results[0][0];
        this.transcription = transcript;
      };

      this.recognition.onerror = (event) => {
        console.error("Speech recognition error", event.error);
      };
    },
    startListening() {
      // Start speech recognition
      this.recognition.start();
    },
  },
};
</script>
