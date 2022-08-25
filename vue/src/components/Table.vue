<script>
import { ref } from 'vue'
import axios from 'axios'

export default {
  data() {
    return { 
      data: null  
    }
  },
  methods: {
    generateTables() {
      axios.get(
          'http://localhost:8000/api/v1/ppp/'  // { "3": { "client": "login", "server": "pptpd", "secret": "password", "ip": "*" }, "4": { "client": "login2", "server": "pptpd", "secret": "password2", "ip": "*" } }
          ).then(
              response => this.data = response.data
          ).catch(err => {console.log(err)});
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
      <th>Client</th>
      <th>Server</th>
      <th>Secret</th>
      <th>Ip</th>
    </tr>
    <tr v-for="model in data" v-bind:key="model">
      <td>{{model.client}}</td>
      <td>{{model.server}}</td>
      <td>{{model.secret}}</td>
      <td>{{model.ip}}</td>
    </tr>
    <tr>
      <td><input type="text"></td>
      <td><input type="text"></td>
      <td><input type="text"></td>
      <td><input type="text"></td>
    </tr>
  </table>
</template>

<style lang="less">

table {

  border-collapse: collapse;
  border: 1px solid black;

  th, td { 
    border: 1px solid black;
  }
}

</style>
