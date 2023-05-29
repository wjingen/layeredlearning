<template>
  <div class="main">
    <div class="left-sidebar">
      <v-btn-toggle
        v-model="difficultyButton"
        mandatory
        divided=""
        class="educationLevels"
      >
        <h1>Difficulty Level</h1>
        <v-btn :color="difficultyButton === 0 ? 'rgba(256, 256, 256, 0.9)' : ''"
          >5 Year Old</v-btn
        >
        <v-btn :color="difficultyButton === 1 ? 'rgba(256, 256, 256, 0.9)' : ''"
          >6th Grader</v-btn
        >
        <v-btn :color="difficultyButton === 2 ? 'rgba(256, 256, 256, 0.9)' : ''"
          >High School Student</v-btn
        >
        <v-btn :color="difficultyButton === 3 ? 'rgba(256, 256, 256, 0.9)' : ''"
          >University Undergraduate</v-btn
        >
        <v-btn :color="difficultyButton === 4 ? 'rgba(256, 256, 256, 0.9)' : ''"
          >Ph.D. Candidate</v-btn
        >
      </v-btn-toggle>
    </div>
    <div class="explanation">
      <div class="conversation-container">
        <img
          src="../../static/logo.png"
          style="height: 100px; width: 100px; display: inline"
        />
        <!-- {{ this.isLoading }} -->
        <div v-if="this.isLoading">
          <v-icon style="padding-top: 50px; padding-left: 50px" size="x-large"
            >mdi-loading mdi-spin</v-icon
          >
        </div>
        <div v-else style="padding: 20px; padding-top: 40px">
          <h1>
            Explanation Level:
            {{ this.mappingDifficulty[this.difficultyButton] }}
          </h1>
          <div
            v-for="(value, key) in this.response[
              this.mappingDifficulty[this.difficultyButton]
            ]"
            :key="key"
          >
            <v-card
              style="
                background: #283d67;
                padding: 50px;
                border-color: #ffffff;
                color: #ffffff;
              "
            >
              <h3>{{ key }}</h3>
              <template v-if="key === 'Subtopics'">
                <ul>
                  <li v-for="(subtopic, index) in value" :key="index">
                    {{ subtopic }}
                  </li>
                </ul>
              </template>
              <template v-else>
                {{ value }}
              </template>
            </v-card>
          </div>
        </div>
      </div>
    </div>
    <div class="right-side">
      <h1>Quiz Yourself</h1>
      <!--  -->
      <!-- {{ this.quizData }} -->
      <div v-for="(question, index) in quizData" :key="index">
        <h3>{{ question.question }}</h3>
        <div
          v-for="(choice, choiceIndex) in question.choices"
          :key="choiceIndex"
        >
          <div
            :class="{
              option: true,
              selected: selectedAnswers[index] === choice.option,
              correct:
                selectedAnswers[index] === choice.option &&
                choice.option === question.answer,
              incorrect:
                selectedAnswers[index] === choice.option &&
                choice.option !== question.answer,
            }"
            @click="selectAnswer(index, choice.option)"
          >
            {{ choice.option }}
          </div>
        </div>
      </div>
      <!--  -->
      <div style="display: flex; justify-content: space-around">
        <v-btn>Take Quiz</v-btn>
        <v-btn>Back to Home</v-btn>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  props: "userQuery",
  data() {
    return {
      difficultyButton: 0,
      response: "",
      // quizData: "",
      selectedAnswers: [],
      // processedResponse: "",
      userQuery: "",
      isLoading: false,
      userInput: "",
      mappingDifficulty: [
        "5 Year Old",
        "6th Grader",
        "High School Student",
        "University Undergraduate",
        "Ph.D. Candidate",
      ],
      quizData: {
        "What is an example of a black hat hacking technique?": {
          choices: [
            "Denial of Service attack",
            "Disaster recovery plan",
            "Social engineering",
            "Data mining",
          ],
          answer: "Denial of Service attack",
        },
        "Which of the following language is not commonly used in black hat hacking?":
          {
            choices: ["JavaScript", "Python", "C++", "COBOL"],
            answer: "COBOL",
          },
        "What is the purpose of a backdoor?": {
          choices: [
            "To provide an administrator with access to a system",
            "To allow for data encryption",
            "To send malicious requests to a website",
            "To store sensitive documents",
          ],
          answer: "To provide an administrator with access to a system",
        },
        "Which of the following is an example of a malicious script?": {
          choices: [
            "Trojan Horse",
            "Search engine optimization",
            "DNS Poisoning",
            "Ransomware",
          ],
          answer: "Ransomware",
        },
        "What is the primary purpose of malware?": {
          choices: [
            "To damage a target computer",
            "To gain access to confidential data",
            "To allow a user to bypass authentication",
            "To gain access to critical infrastructure",
          ],
          answer: "To gain access to confidential data",
        },
      },
    };
  },
  methods: {
    processResponse(response) {
      const regexPattern = /([^\n:]+):\s*([^]+?)(?=\n\n|\n$|$)/g;
      const parsedResponse = {};

      let match;
      while ((match = regexPattern.exec(response))) {
        const [, level, response] = match;
        parsedResponse[level.trim()] = this.processLevel(response);
      }
      return parsedResponse;
      // You can store the parsedResponse in a data property or use it as needed
    },
    async sendGetRequest() {
      try {
        this.isLoading = true;
        let data = JSON.stringify({
          topic: this.userQuery,
        });
        let config = {
          method: "post",
          maxBodyLength: Infinity,
          url: "https://xuanming.pythonanywhere.com/explainer",
          headers: {
            "Content-Type": "application/json",
          },
          data: data,
        };
        axios
          .request(config)
          .then((response) => {
            // console.log(JSON.stringify(response.data));
            this.response = response.data;
          })
          .catch((error) => {
            console.log(error);
          });

        this.isLoading = false;
      } catch (error) {
        this.isLoading = false;
        console.error("Error:", error);
      }
    },
    async sendQuizRequest() {
      const axios = require("axios");
      let data = JSON.stringify({
        topic: "black_hat_hacking",
        role: "university_undergraduate",
      });

      let config = {
        method: "post",
        maxBodyLength: Infinity,
        url: "https://xuanming.pythonanywhere.com/quiz",
        headers: {
          "Content-Type": "application/json",
        },
        data: data,
      };

      axios
        .request(config)
        .then((response) => {
          this.quizData = JSON.stringify(response.data);
          console.log(this.quizData);
          this.processQuizData();
        })
        .catch((error) => {
          console.log(error);
        });
    },
    processQuizData() {
      const transformedData = Object.entries(this.quizData).map(
        ([question, { choices, answer }]) => ({
          question,
          choices: choices.map((option) => ({ option })),
          answer,
        })
      );

      this.quizData = transformedData;
      this.selectedAnswers = Array(transformedData.length).fill(null);
      console.log(this.quizData);
      console.log(this.selectedAnswers);
    },
    selectAnswer(index, answer) {
      this.selectedAnswers.splice(index, 1, answer);
    },
    processLevel(string) {
      const explanationRegex = "^(.*?)(?=Subtopics)";
      const subtopicsRegex = "Subtopics:([^\\.]+)";
      const relatedMaterialsRegex = "Additional materials:([^\\.]+)";

      const explanationMatch = string.match(new RegExp(explanationRegex));
      const subtopicsMatch = string.match(new RegExp(subtopicsRegex));
      const relatedMaterialsMatch = string.match(
        new RegExp(relatedMaterialsRegex)
      );

      const explanation = explanationMatch ? explanationMatch[1].trim() : "";
      const subtopics = subtopicsMatch ? subtopicsMatch[1].trim() : "";
      const relatedMaterials = relatedMaterialsMatch
        ? relatedMaterialsMatch[1].trim()
        : "";

      const response = {
        Explanation: explanation,
        "Related Materials": relatedMaterials,
        Subtopics: subtopics,
      };
      // console.log(response);

      return response;
    },
  },

  async mounted() {
    this.userQuery = this.$route.query.userQuery;
    this.sendGetRequest();
    this.processQuizData();
    // this.sendQuizRequest();
  },
};
</script>

<style scoped>
.main {
  background: #283d67;
  color: white;
  display: flex;
  flex-flow: row nowrap;
  height: 1000px;
}
.left-sidebar {
  min-width: 20%;
  display: flex;
  flex-flow: column wrap;
  justify-content: center;
  align-items: center;
}
.left-sidebar h1 {
  color: white;
}
.educationLevels {
  display: flex;
  flex-flow: column nowrap;
  justify-content: flex-start;
  height: 100%;
}
.educationLevels .v-btn {
  padding: 30px 0px;
}
.explanation {
  width: 60%;
}
.conversation-container {
  width: 1000px;
  height: 100%;
  display: flex;
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
  /* background-color: red; */
  height: 400px;
  width: 400px;
}

.right-side {
  /* background-color: green; */
  width: 30%;
  display: flex;
  flex-flow: column nowrap;
  align-items: center;
}

/*  */
.option {
  padding: 10px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.option:hover {
  background-color: lightgray;
}

.selected {
  background-color: yellow;
}

.correct {
  background-color: green;
  color: white;
}

.incorrect {
  background-color: red;
  color: white;
}
</style>
