<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
  </div>
</template>

<script>
// 对外暴露接口，接口里面的变量在自己的作用域里面有效
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Vue.js App 1'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
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
  color: #0b4bd4;
}
</style>
