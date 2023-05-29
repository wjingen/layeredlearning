<template>
  <div class="faq-dropdown">
    <h2 class="faq-dropdown__title">Frequently Asked Questions</h2>
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
</template>

<script>
export default {
  data() {
    return {
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
  methods: {
    toggleAnswer(index) {
      this.faqList[index].open = !this.faqList[index].open;
    },
  },
};
</script>

<style scoped>
.faq-dropdown {
  background-color: #27374d;
  color: #ffffff;
  padding: 20px;
}

.faq-dropdown__title {
  font-size: 24px;
  margin-bottom: 10px;
}

.faq-dropdown__list {
  list-style-type: none;
  padding: 0;
}

.faq-dropdown__item {
  margin-bottom: 15px;
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
}

.faq-dropdown__icon--open {
  transform: rotate(135deg);
}

.faq-dropdown__answer {
  background-color: #ffffff;
  color: #27374d;
  padding: 10px;
  font-size: 16px;
  display: flex;
}
</style>
