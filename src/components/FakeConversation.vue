<template>
  <div>
    <input type="file" @change="handleFileChange" accept=".pdf" />
    <div v-if="text">
      <h2>Extracted Text:</h2>
      <pre>{{ text }}</pre>
    </div>
  </div>
</template>

<script>
import pdfjsLib from "pdfjs-dist";
pdfjsLib.GlobalWorkerOptions.workerSrc =
  "layered_learning/node_modules/pdfjs-dist/build/pdf.worker.js"; // Adjust the path accordingly
import { getDocument } from "pdfjs-dist";

export default {
  data() {
    return {
      text: null,
    };
  },
  methods: {
    handleFileChange(event) {
      const file = event.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = () => {
          const typedArray = new Uint8Array(reader.result);
          this.extractTextFromPDF(typedArray);
        };
        reader.readAsArrayBuffer(file);
      }
    },
    extractTextFromPDF(typedArray) {
      //   alert(typedArray);
      //   console.log(getDocument);
      //   console.log(pdfjsLib);
      getDocument(typedArray).promise.then((pdf) => {
        const totalPages = pdf.numPages;
        let extractedText = "";
        console.log("DEBUG");
        const getPageText = (pageNumber) => {
          return pdf.getPage(pageNumber).then((page) => {
            return page.getTextContent().then((content) => {
              let pageText = "";
              content.items.forEach((item) => {
                pageText += item.str + " ";
              });
              return pageText.trim();
            });
          });
        };

        const promises = [];
        for (let i = 1; i <= totalPages; i++) {
          promises.push(getPageText(i));
        }

        Promise.all(promises).then((texts) => {
          extractedText = texts.join("\n");
          this.text = extractedText;
        });
      });
    },
  },
};
</script>
