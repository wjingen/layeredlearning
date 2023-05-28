<template>
  <div class="conversation-container">
    <div class="messages">
      <div
        v-for="(message, index) in conversation"
        :key="index"
        :class="['message', message.type]"
      >
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
</template>

<script>
export default {
  data() {
    return {
      conversation: [
        { type: "bot", text: "Hello! How can I assist you today?" },
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
        }, 500);
      }
    },
  },
};
</script>

<style scoped>
.conversation-container {
  width: 400px;
  border: 1px solid #ccc;
  border-radius: 4px;
  overflow: hidden;
}

.messages {
  padding: 10px;
  max-height: 300px;
  overflow-y: scroll;
}

.message {
  display: flex;
  margin-bottom: 10px;
}

.bot {
  justify-content: flex-start;
}

.user {
  justify-content: flex-end;
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

button {
  margin-left: 10px;
  padding: 8px 12px;
  border-radius: 4px;
  background-color: #007bff;
  color: #fff;
  border: none;
  cursor: pointer;
}
</style>
