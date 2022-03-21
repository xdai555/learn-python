<template>
    <div>
        <h2>页面不存在...</h2>
    </div>
</template>

<script>
export default {
  name: 'NotFound',
  // 路由钩子，添加进入路由前的动作，可以进行操作。例如获取数据、拦截操作等
  beforeRouteEnter (to, from, next) {
    next()
  },
  methods: {
    getData: function () {}
  }
}
</script>
