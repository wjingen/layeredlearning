<template>
  <div class="main">
    <div class="top">
      <div
        style="
          display: flex;
          flex-direction: column;
          justify-content: space-around;
          height: 500px;
          width: 400px;
        "
      >
        <h1>LayeredLearning: The 21st Century Learning Tool</h1>
        <p>We break down any concept into difficulty levels.</p>
        <div>
          <div
            style="
              display: flex;
              justify-content: space-between;
              align-items: center;
            "
          >
            <v-btn
              style="height: 40px; text-align: center"
              @click="scrollToNextPage"
              >Get Started</v-btn
            >
            <v-btn style="height: 40px; text-align: center" @click="scrollToFaq"
              >How it Works</v-btn
            >
          </div>
        </div>
      </div>
      <div><img src="../../static/logo.png" /></div>
    </div>
    <div class="bottom" ref="bottom">
      <div class="explainer-cards">
        <v-row>
          <v-col cols="2" md="3" v-for="card in cards" :key="card.id">
            <v-card
              class="card"
              @mouseover="card.hover = true"
              @mouseleave="card.hover = false"
            >
              <v-card-text>
                <v-icon v-if="card.hover">{{ card.iconHover }}</v-icon>
                <v-icon v-else>{{ card.iconHover }}</v-icon>
                <p>{{ card.text }}</p>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </div>
      <div
        style="
          display: flex;
          flex-direction: column;
          align-items: center;
          justify-content: space-around;
          width: 800px;
          height: 300px;
        "
      >
        <h1>
          Unpack any <span class="color-effect">concept</span>, one layer at a
          time.
        </h1>
        <h3>
          LayeredLearning explains your queries at a level suitable for you.
        </h3>
        <text style="font-size: 1.2rem"
          >Submit your query in text, PDF, or audio format.</text
        >
      </div>
      <div class="search">
        <v-card title="Query" class="query-card">
          <v-text-field
            v-model="userQuery"
            placeholder="Enter your topic"
            style="width: 80%; max-height: 80px"
            :append-icon="icon"
            @click:append="speechRecognition"
          ></v-text-field>
          <v-btn @click="handleSubmit"> Submit </v-btn>
        </v-card>
        <v-card title="File" class="query-card"
          ><v-file-input
            chips
            multiple
            label="File upload"
            style="width: 80%; max-height: 80px"
            v-model="uploadedFiles"
            :rules="rules"
            prepend-icon=""
            append-inner-icon="mdi-file"
            @change="handleFileUpload"
          ></v-file-input>
          <v-btn @click="handleSubmit"> Submit </v-btn>
        </v-card>
        <v-card title="Audio" class="query-card"
          ><v-file-input
            chips
            multiple
            label="File upload"
            style="width: 80%; max-height: 80px"
            v-model="uploadedFiles"
            :rules="rules"
            prepend-icon=""
            append-inner-icon="mdi-file"
            @change="handleFileUpload"
          ></v-file-input>
          <v-btn @click="handleSubmit"> Submit </v-btn>
        </v-card>
      </div>
    </div>
    <div class="faq" ref="faq">
      <h1>FAQs</h1>
      <body>
        Answers to some questions you might have.
      </body>
      <ul class="faq-dropdown__list">
        <li
          v-for="(question, index) in faqList"
          :key="index"
          class="faq-dropdown__item"
        >
          <button @click="toggleAnswer(index)" class="faq-dropdown__question">
            {{ question.title }}
            <span
              class="faq-dropdown__icon"
              :class="{ 'faq-dropdown__icon--open': question.open }"
            ></span>
          </button>
          <div v-if="question.open" class="faq-dropdown__answer">
            {{ question.answer }}
          </div>
        </li>
      </ul>
    </div>
  </div>
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
      cards: [
        {
          id: 1,
          iconHover: "mdi-emoticon-happy",
          text: "User Friendly",
        },
        {
          id: 2,
          iconHover: "mdi-school",
          text: "Concept Explainer",
        },
        {
          id: 3,
          iconHover: "mdi-help-box-multiple",
          text: "Quiz Generator",
        },
        {
          id: 4,
          iconHover: "mdi-account-group",
          text: "Progress Tracker",
        },
      ],
      faqList: [
        {
          title: "What is LayeredLearning?",
          answer:
            "LayeredLearning is an innovative online platform that offers a unique approach to learning by providing users with answers to their chosen topics at five different difficulty levels. It aims to cater to learners of all levels, from beginners to advanced.",
          open: false,
        },
        {
          title: "How does LayeredLearning work?",
          answer:
            "When you enter a topic into LayeredLearning, the platform generates five sets of answers, each designed to suit a specific difficulty level. The answers are presented in a layered format, with the easiest level displayed first and the most challenging level at the end. Users can explore the different levels of information based on their learning needs and preferences.",
          open: false,
        },
        {
          title: "What are the different difficulty levels available?",
          answer:
            "LayeredLearning provides five distinct difficulty levels to accommodate various learning abilities and preferences:\n\n- Level 1 (Easy): Beginner-friendly explanations and simple concepts.\n- Level 2 (Intermediate): Provides additional details and expands upon the basics.\n- Level 3 (Advanced): Offers more in-depth insights and complex ideas.\n- Level 4 (Expert): Presents comprehensive and detailed information for advanced learners.\n- Level 5 (Master): Provides the highest level of complexity and expertise on the chosen topic.",
          open: false,
        },
        {
          title: "How are the difficulty levels determined?",
          answer:
            "The difficulty levels in LayeredLearning are determined through a combination of algorithms and human input. The system analyzes the complexity and depth of information available on the chosen topic, categorizes it into appropriate levels, and fine-tunes it with the help of subject matter experts to ensure accuracy and relevance.",
          open: false,
        },
        {
          title: "Can I switch between difficulty levels?",
          answer:
            "Absolutely! LayeredLearning allows you to seamlessly switch between difficulty levels as per your preference. You can start with the easier levels and gradually progress to more challenging ones, or dive directly into a specific difficulty level based on your existing knowledge.",
          open: false,
        },
        {
          title: "Are the answers provided by LayeredLearning accurate?",
          answer:
            "LayeredLearning strives to provide accurate and reliable information. The content is curated and reviewed by a team of experts to ensure its quality. However, as with any online platform, it's always advisable to cross-reference information from multiple sources for a comprehensive understanding.",
          open: false,
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
    toggleAnswer(index) {
      this.faqList[index].open = !this.faqList[index].open;
    },
    cleanUserQuery() {
      this.userQuery = this.userQuery.replace(/\s+/g, "_").toLowerCase();
    },
    handleSubmit() {
      this.cleanUserQuery();
      this.$router.push({
        path: "/explanation",
        query: {
          userQuery: this.userQuery,
        },
      });
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
    scrollToNextPage() {
      this.$refs.bottom.scrollIntoView({ behavior: "smooth", block: "start" });
    },
    scrollToFaq() {
      this.$refs.faq.scrollIntoView({ behavior: "smooth", block: "start" });
    },
  },
};
</script>
<style scoped>
.main {
  display: flex;
  flex-direction: column;
  align-items: center;
  background: #27374d;
  color: white;
}
.top {
  min-height: 300px;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  width: 100%;
}
.bottom {
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 70%;
}
.explainer-cards {
  padding-top: 50px;
  width: 100%;
}

.card {
  padding: 20px;
  margin: 10px;
  text-align: center;
  cursor: pointer;
  transition: all 0.3s ease-in-out;
  color: #283d67;
}

h2 {
  color: #27374d;
}
.card:hover {
  transform: scale(1.05);
}

.search {
  display: flex;
  justify-content: space-between;
  width: 100%;
  padding-top: 20px;
}

.color-effect {
  background: linear-gradient(to right, #ff7f00, #4685ff);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.search .query-card {
  width: 350px;
  height: 500px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-around;
  box-shadow: 1px 4px 4px rgba(0, 0, 0, 0.2);
}
.faq {
  display: flex;
  flex-flow: column nowrap;
  align-items: center;
  padding-top: 50px;
}
.faq > * {
  padding: 20px;
}

.faq-dropdown__list {
  list-style-type: none;
  padding: 0;
  width: 1000px;
}

.faq-dropdown__item {
  margin-bottom: 15px;
  padding: 15px;
  border: solid rgba(255, 255, 255, 0.3);
}

.faq-dropdown__question {
  background-color: #27374d;
  color: #ffffff;
  border: none;
  cursor: pointer;
  padding: 10px;
  font-size: 18px;
  width: 100%;
  text-align: left;
}

.faq-dropdown__question:focus {
  outline: none;
}

.faq-dropdown__icon {
  display: inline-block;
  width: 10px;
  height: 10px;
  border-top: 2px solid #ffffff;
  border-right: 2px solid #ffffff;
  transform: rotate(45deg);
  transition: transform 0.3s;
  /* padding-left: 15px; */
}

.faq-dropdown__icon--open {
  transform: rotate(135deg);
}

.faq-dropdown__answer {
  /* background-color: #ffffff; */
  color: #ffffff;
  padding: 10px;
  font-size: 16px;
  display: flex;
}
</style>
