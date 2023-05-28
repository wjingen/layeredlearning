<template>
  <div class="main">
    <div class="top">
      <h1>LayeredLearning</h1>
      <p>Learning at your own level, at your own pace.</p>
    </div>
    <div class="bottom">
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
      <div class="search">
        <v-card title="Search by Query" class="query-card">
          <v-text-field
            v-model="userQuery"
            placeholder="Enter your topic"
            style="width: 400px"
            :append-icon="icon"
            @click:append="speechRecognition"
          ></v-text-field>
        </v-card>
        <v-card title="Search using File" class="query-card"
          ><v-file-input
            chips
            multiple
            label="File upload"
            style="width: 500px"
            v-model="uploadedFiles"
            :rules="rules"
            prepend-icon=""
            append-inner-icon="mdi-file"
            @change="handleFileUpload"
          ></v-file-input
        ></v-card>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
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
          text: "Community Based",
        },
      ],
    };
  },
};
</script>
<style scoped>
.main {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.top {
  background: linear-gradient(to bottom, #dddddd, #27374d);
  color: white;
  /* Add other styles as needed */
  min-height: 300px;
  display: flex;
  flex-direction: column;
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
}
.search .query-card {
  width: 600px;
}
</style>
