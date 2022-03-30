<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import myHello from './components/hello.vue'
import Index from './components/Index.vue'
import TodoList from './components/TodoList.vue'
import TextFSMOnlile from './components/TextFSMOnline.vue'

/*
添加组件的流程：
1. 在对应目录下新建组件，如 components/hello.vue
2. 在 APP.vue 中引入组件，并且 export 出去
3. 在 router/index.js 中引入组件，为组件添加路由信息

===
工作流程：
main.js 中从 APP.vue 引入了 name 为 'App' 的组件并且注册了 router 组件，并把内容返回到了 index.heml 中 id="app" 的 div 里面，APP.vue 中模板部分使用 router-view 注册了所有的 url，这样前端可以通过不同的 url 进行页面的跳转。

main.js 和 index.html 一般情况下是不用做改动的。
 */

export default {
  components: { HelloWorld, myHello, Index, TodoList, TextFSMOnlile },
  name: 'App'
}
</script>

<!--
<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
-->
