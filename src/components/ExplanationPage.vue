<template>
  <div class="main">
    <div class="left-sidebar">
      <v-btn-toggle
        v-model="difficultyButton"
        mandatory
        divided=""
        class="educationLevels"
      >
        <h3>Difficulty Level</h3>
        <v-btn :color="difficultyButton === 0 ? 'blue' : ''">Beginner</v-btn>
        <v-btn :color="difficultyButton === 1 ? 'yellow' : ''"
          >Intermediate</v-btn
        >
        <v-btn :color="difficultyButton === 2 ? 'orange' : ''">Advanced</v-btn>
        <v-btn :color="difficultyButton === 3 ? 'red' : ''">Expert</v-btn>
      </v-btn-toggle>
    </div>
    <div class="explanation">
      <h1>LayeredLearning Response</h1>
      <div class="conversation-container">
        <div class="messages">
          <div
            v-for="(message, index) in conversation"
            :key="index"
            :class="['message', message.type]"
          >
            <v-icon style="padding: 30px">mdi-account</v-icon>
            <div class="message-content">
              <span>{{ message.text }}</span>
            </div>
          </div>
        </div>
        <div class="input-container">
          <input
            v-model="userInput"
            @keydown.enter="sendMessage"
            type="text"
            placeholder="Type your message..."
          />
          <button @click="sendMessage">Send</button>
        </div>
      </div>
    </div>
    <div class="right-side">
      <h3>Summary</h3>
      <v-card class="summary">hello there</v-card>
      <p>
        Still unsure of your understanding? Ask a follow-up question or take a
        quiz to find out.
      </p>
      <v-card class="quiz">quiz section</v-card>
      <div style="display: flex; justify-content: space-around">
        <v-btn>Take Quiz</v-btn>
        <v-btn>Back to Home</v-btn>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      difficultyButton: null,
      conversation: [
        {
          type: "bot",
          text: "REST (Representational State Transfer) API (Application Programming \
      Interface) is an architectural style and set of guidelines used for \
      designing and interacting with web services. It provides a standardized \
      way for systems to communicate over the internet. REST APIs are widely \
      used in modern web development to enable communication between client \
      applications, such as web browsers or mobile apps, and server-side s\
      applications.",
        },
      ],
      userInput: "",
    };
  },
  methods: {
    sendMessage() {
      if (this.userInput.trim() !== "") {
        this.conversation.push({ type: "user", text: this.userInput });
        this.userInput = "";

        // Simulate bot response (replace this with your actual logic)
        setTimeout(() => {
          this.conversation.push({
            type: "bot",
            text: "I am just a demo chatbot. I cannot provide real responses.",
          });
        }, 1500);
      }
    },
  },
};
</script>

<style scoped>
.main {
  background-color: white;
  display: flex;
  flex-flow: row nowrap;
}
.left-sidebar {
  min-width: 15%;
}
.educationLevels {
  display: flex;
  flex-flow: column nowrap;
  justify-content: space-around;
  height: 100%;
}
.educationLevels .v-btn {
  padding: 50px;
}
.explanation {
  width: 60%;
}
.conversation-container {
  width: 1000px;
  height: 100%;
  border: 1px solid #ccc;
  border-radius: 4px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.messages {
  padding: 10px;
  max-height: 800px;
  overflow-y: scroll;
}

.message {
  display: flex;
  margin-bottom: 10px;
}

.bot {
  flex-direction: row;
  justify-content: flex-start;
}

.user {
  flex-direction: row-reverse;
  justify-content: flex-start;
}

.message-content {
  padding: 6px 12px;
  background-color: #f2f2f2;
  border-radius: 4px;
}

.input-container {
  display: flex;
  align-items: center;
  padding: 10px;
  background-color: #f5f5f5;
}

input[type="text"] {
  flex-grow: 1;
  padding: 8px;
  border-radius: 4px;
  border: 1px solid #ccc;
}

.conversation-container button {
  margin-left: 10px;
  padding: 8px 12px;
  border-radius: 4px;
  background-color: #007bff;
  color: #fff;
  border: none;
  cursor: pointer;
}
.summary {
  background-color: red;
  height: 400px;
  width: 400px;
}
.quiz {
  background-color: red;
  height: 400px;
  width: 400px;
}
</style>
