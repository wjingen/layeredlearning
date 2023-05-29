<!-- <template>
  <div>
    <input type="file" @change="handleFileChange" accept=".pdf" />
    <button @click="extractText" :disabled="!pdfLoaded">Extract Text</button>
    <div v-if="textExtracted">
      <h2>Extracted Text:</h2>
      <pre>{{ extractedText }}</pre>
    </div>
  </div>
</template>

<script>
import pdfjsLib from "pdfjs-dist";
// import getDocument from "pdfjs-dist/webpack";

import { load } from "mime";

export default {
  data() {
    return {
      pdfFile: null,
      pdfLoaded: false,
      textExtracted: false,
      extractedText: "",
    };
  },
  methods: {
    handleFileChange(event) {
      this.pdfFile = event.target.files[0];
      this.pdfLoaded = true;
    },
    async extractText() {
      try {
        const pdfData = new Uint8Array(await this.pdfFile.arrayBuffer());
        // const loadingTask = getDocument({ data: pdfData });
        // const pdf = await loadingTask.promise;
        // const numPages = pdf.numPages;
        // let extractedText = "";
        // console.log(numPages);
        console.log(pdfData);
        console.log(pdfjsLib.getDocument);
        // for (let i = 1; i <= numPages; i++) {
        //   const page = await pdf.getPage(i);
        //   const textContent = await page.getTextContent();
        //   const pageText = textContent.items.map((item) => item.str).join(" ");
        //   extractedText += pageText + "\n";
        // }

        // this.extractedText = extractedText;
        // this.textExtracted = true;
      } catch (error) {
        console.error("Error extracting text:", error);
      }
    },
  },
};
</script> -->
<template>
  <div></div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped></style>
