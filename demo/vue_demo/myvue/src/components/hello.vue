<template>
    <div>
        自定义的 hello 页面。<br>
        你好，{{ name }}。
    </div>
</template>

<script>
export default {
  name: 'myHello',
  data () {
    return {
      name: 'Demo'
    }
  }
}
</script>
