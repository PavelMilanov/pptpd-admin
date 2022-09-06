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
    },
    removeUser(client) {
      axios.delete(
        `http://localhost:8000/api/v1/ppp/${client}/`, {}).then(responce => {
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
      <th></th> <!--Заглушка-->
      <th>Client</th>
      <th>Server</th>
      <th>Secret</th>
      <th>Ip</th>
      <th></th> <!--Заглушка-->
    </tr>
    <tr v-for="model in data" v-bind:key="model">
      <td></td> <!--Заглушка-->
      <td>{{model.client}}</td>
      <td>{{model.server}}</td>
      <td>{{model.secret}}</td>
      <td>{{model.ip}}</td>
      <td>
        <div class="remove-button" @click="removeUser(model.client)">
          <img src="../assets/delete.svg" alt="delete row">  
        </div>
      </td>
    </tr>
    <tr>
      <div class="add-button" @click="addUser">
        <img src="../assets/add.svg" alt="add row">
      </div>
      <td><input type="text" v-model="form.client"></td>
      <td><input type="text" v-model="form.server"></td>
      <td><input type="text" v-model="form.secret"></td>
      <td><input type="text" v-model="form.ip"></td>
      <td></td> <!--Заглушка-->
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

  th:first-child,
  th:last-child,
  td:first-child,
  td:last-child {
    border: none;
    width: 2%;
  }
}

input {
  width: 96%;
}

.add-button,
.remove-button {

  img {
    position: relative;
    top: 0.2rem;
    height: 1rem;
  }
}
</style>
