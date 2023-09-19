<template>
  <button type="submit" v-on:click="getMeme()">Generate Meme</button>
  <div v-if="memeUrl" style="padding-top: 100px;">
    <img :src="memeUrl" alt="" style="aspect-ratio: 1; width: 25%;">
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'HelloWorld',
  
  data(){
    return{
      memeUrl: "",
    }
  },
  methods: {
    getMeme(){
      axios.get("http://localhost:5000/meme")
      .then((response) => {
        this.memeUrl = response.data;
      })
      .catch((error) => {
        console.log(error);
      })
    }
  }
}
</script>

<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
button{
  padding: 25px;
  color: white;
  background-color: black;
  border: 1px solid black;
  border-radius: 5px;
  cursor: pointer;
  font-weight: bold;
  font-size: 20px;
  transition: 0.1s;
}
button:hover{
  background-color: white;
  color: black;
  transition: 0.1s;
}
</style>
