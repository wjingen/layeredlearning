const functions = require("firebase-functions");
const axios = require("axios");

exports.queryExplainer = functions.https.onRequest(async (req, res) => {
  try {
    const response = await axios.get("https://xuanming.pythonanywhere.com/explainer/");
    res.send(response.data);
  } catch (error) {
    console.error(error);
    res.status(500).send("An error occurred while querying the URL.");
  }
});


