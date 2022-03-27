<template>
<div>
    <h1>hello {{ name }}</h1>
    <div>
      <input type="text" v-model="info">
      <button @click="handleClick">添加</button>
    </div>
    <li class="item" v-for="item in list" :key="item" :param="item">{{ item }}</li>
</div>
</template>

<script>
export default {
  props: ['param'],
  data () {
    return {
      name: 'test',
      info: '',
      list: []
    }
  },
  methods: {
    handleClick () {
      console.log(this.info)
      this.list.push(this.info)
      this.info = ''
    }
  }
}
</script>

<style scoped>
.item {
  color: red;
  font-size: 20px;
}
</style>
