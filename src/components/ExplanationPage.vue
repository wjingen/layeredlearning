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
        <div v-if="isLoading">
          <v-icon style="padding-top: 50px; padding-left: 50px" size="x-large"
            >mdi-loading mdi-spin</v-icon
          >
        </div>
        <!-- <text v-else style="display: inline">{{ this.response }}</text> -->
        <div v-else style="padding: 20px; padding-top: 40px">
          <h1>{{ this.mappingDifficulty[this.difficultyButton] }}</h1>
          <!-- <div
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
              {{ value }}
            </v-card>
          </div> -->
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
              <h3>
                {{ key }}
              </h3>
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
import axios from "axios";
export default {
  props: "userQuery",
  // computed: {
  //   processedResponse() {
  //     console.log(this.difficultyButton);
  //     console.log(this.response);
  //     return this.processLevel(
  //       this.response[this.mappingDifficulty[this.difficultyButton]]
  //     );
  //   },
  // },
  data() {
    return {
      difficultyButton: 0,
      response: "",
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
          topic: "grey_hat_hacking",
        });

        // let config = {
        //   method: "post",
        //   maxBodyLength: Infinity,
        //   url: "https://xuanming.pythonanywhere.com/explainer",
        //   headers: {
        //     "Content-Type": "application/json",
        //   },
        //   data: data,
        // };
        // const response = await axios.get(url);
        // this.response = response.data;
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
      // this.response = this.processResponse(this.response);
      // console.log(this.response);
      // console.log(this.response[this.mappingDifficulty[this.difficultyButton]]);
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

  mounted() {
    this.userQuery = this.$route.query.userQuery;
    this.sendGetRequest();
  },
};
</script>

<style scoped>
.main {
  background: #283d67;
  color: white;
  display: flex;
  flex-flow: row nowrap;
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
  background-color: red;
  height: 400px;
  width: 400px;
}
</style>
