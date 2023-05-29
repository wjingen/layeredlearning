<template>
  <div>
    <h1>Quiz</h1>
    <div v-for="(question, index) in quizData" :key="index">
      <h3>{{ question.question }}</h3>
      <div v-for="(choice, choiceIndex) in question.choices" :key="choiceIndex">
        <div
          :class="{
            option: true,
            selected: selectedAnswers[index] === choice.option,
            correct:
              choice.isCorrect && selectedAnswers[index] === choice.option,
            incorrect:
              !choice.isCorrect && selectedAnswers[index] === choice.option,
          }"
          @click="selectAnswer(index, choice.option)"
        >
          {{ choice.option }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      quizData: [],
      selectedAnswers: [],
    };
  },
  methods: {
    processQuizData(data) {
      console.log(data);
      const transformedData = Object.entries(data).map(
        ([question, choices]) => ({
          question,
          choices: choices[0].map((option, index) => ({
            option,
            isCorrect: index === choices[1].indexOf(option),
          })),
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
  },
  mounted() {
    const quizData = {
      "What is an example of a black hat hacking technique?": [
        [
          "Denial of Service attack",
          "Disaster recovery plan",
          "Social engineering",
          "Data mining",
        ],
        "Denial of Service attack",
      ],
      "Which of the following language is not commonly used in black hat hacking?":
        [["JavaScript", "Python", "C++", "COBOL"], "COBOL"],
      "What is the purpose of a backdoor?": [
        [
          "To provide an administrator with access to a system",
          "To allow for data encryption",
          "To send malicious requests to a website",
          "To store sensitive documents",
        ],
        "To provide an administrator with access to a system",
      ],
      "Which of the following is an example of a malicious script?": [
        [
          "Trojan Horse",
          "Search engine optimization",
          "DNS Poisoning",
          "Ransomware",
        ],
        "Ransomware",
      ],
      "What is the primary purpose of malware?": [
        [
          "To damage a target computer",
          "To gain access to confidential data",
          "To allow a user to bypass authentication",
          "To gain access to critical infrastructure",
        ],
        "To gain access to confidential data",
      ],
    };

    this.processQuizData(quizData);
  },
};
</script>

<style scoped>
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
