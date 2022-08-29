<script>
import { ref } from 'vue'
import axios from 'axios'

export default {
  data() {
    return { 
      data: null,
      form: {
        client: null,
        server: "pptpd",
        secret: null,
        ip: "*"
      }
    }
  },
  methods: {
    generateTables() {
      axios.get(
          'http://localhost:8000/api/v1/ppp/'  // { "3": { "client": "login", "server": "pptpd", "secret": "password", "ip": "*" }, "4": { "client": "login2", "server": "pptpd", "secret": "password2", "ip": "*" } }
          ).then(
              response => this.data = response.data
          ).catch(err => {console.log(err)});
    },
    addUser() {
      axios.post(
        'http://localhost:8000/api/v1/ppp/', {
          "client": this.form.client,
          "server": this.form.server,
          "secret": this.form.secret,
          "ip": this.form.ip
        }).then(responce => {
          this.generateTables()
          console.log(responce)
          }).catch(err => {console.log(err)})
    }
  },
  created() {
    this.generateTables()
    }
}

</script>

<template>
  <table>
    <tr>
      <th></th>
      <th>Client</th>
      <th>Server</th>
      <th>Secret</th>
      <th>Ip</th>
    </tr>
    <tr v-for="model in data" v-bind:key="model">
      <td></td>
      <td>{{model.client}}</td>
      <td>{{model.server}}</td>
      <td>{{model.secret}}</td>
      <td>{{model.ip}}</td>
    </tr>
    <tr>
      <div class="add-button" @click="addUser">
        <img src="../assets/add.svg" alt="add row">
      </div>
      <td><input type="text" v-model="form.client"></td>
      <td><input type="text" v-model="form.server"></td>
      <td><input type="text" v-model="form.secret"></td>
      <td><input type="text" v-model="form.ip"></td>
    </tr>
  </table>
</template>

<style lang="less">

table {

  border-collapse: collapse;

  th, td { 
    border: 1px solid black;
    height: 1rem;
  }

  th:first-child, td:first-child {
    border: none;
    width: 2%;
  }
}

input {
  width: 96%;
}

.add-button {

  img {
    position: relative;
    top: 0.2rem;
    height: 1rem;
  }
}
</style>
