<template>
  <div class="main">
    <div class="button-container">
      <v-btn-toggle v-model="difficultyButton" mandatory divided="">
        <v-btn :color="difficultyButton === 0 ? 'blue' : ''">Beginner</v-btn>
        <v-btn :color="difficultyButton === 1 ? 'yellow' : ''"
          >Intermediate</v-btn
        >
        <v-btn :color="difficultyButton === 2 ? 'orange' : ''">Advanced</v-btn>
        <v-btn :color="difficultyButton === 3 ? 'red' : ''">Expert</v-btn>
      </v-btn-toggle>
    </div>
    <div class="explanation">
      REST (Representational State Transfer) API (Application Programming
      Interface) is an architectural style and set of guidelines used for
      designing and interacting with web services. It provides a standardized
      way for systems to communicate over the internet. REST APIs are widely
      used in modern web development to enable communication between client
      applications, such as web browsers or mobile apps, and server-side
      applications. At its core, a REST API is built on the principles of the
      HTTP (Hypertext Transfer Protocol) protocol, which is the foundation of
      the World Wide Web. REST APIs use HTTP methods, such as GET, POST, PUT,
      DELETE, to perform various operations on resources (data) hosted on a
      server. Key Concepts of REST API: Resources: In a REST API, resources
      represent the data entities or objects that can be accessed and
      manipulated. Resources are identified by unique URLs (Uniform Resource
      Locators) or endpoints. HTTP Verbs (Methods): REST APIs use different HTTP
      verbs to specify the type of operation to be performed on a resource. The
      commonly used HTTP methods in REST are: GET: Retrieves a representation of
      a resource. POST: Creates a new resource. PUT: Updates or replaces an
      existing resource. DELETE: Removes a resource. Uniform Interface: REST
      APIs follow a uniform and consistent interface design. They utilize
      standard HTTP methods, adhere to specific URL patterns, and use standard
      media types, such as JSON (JavaScript Object Notation) or XML (eXtensible
      Markup Language), for data exchange. Stateless: REST APIs are stateless,
      meaning that each request from a client to a server contains all the
      necessary information to process that request. The server does not
      maintain any session or context information between requests.
      Representation: Resources in a REST API are represented in a specific
      format, typically JSON or XML, to facilitate data exchange between the
      client and the server. Benefits of REST API: Simplicity: REST APIs are
      easy to understand, implement, and consume due to their simplicity and
      adherence to widely adopted standards like HTTP. Scalability: REST APIs
      can be designed to be highly scalable, as they are stateless and can
      handle a large number of concurrent requests. Platform Independence: REST
      APIs are not tied to any specific platform or programming language, making
      them versatile and accessible from a wide range of client applications.
      Flexibility: REST APIs allow for flexible data formats, such as JSON,
      enabling easy integration with various systems and devices. Caching and
      Performance: REST APIs leverage the HTTP caching mechanisms, allowing
      clients to cache responses and improve performance by reducing the need
      for repeated requests. Overall, REST APIs provide a flexible and
      standardized approach for building web services that can be consumed by a
      variety of clients. They promote loose coupling, interoperability, and
      scalability, making them a popular choice for modern web application
      development.
    </div>
    <div class="quiz"><h1>Quiz Section</h1></div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      difficultyButton: null,
    };
  },
};
</script>

<style scoped>
.main {
  background-color: white;
}
.explanation {
  width: 60%;
}
</style>
