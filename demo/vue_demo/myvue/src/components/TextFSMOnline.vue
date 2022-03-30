<template>
<div>
      <h1>TextFSM 在线解析</h1>
<codemirror v-model="code" :options="cmOptions"/>
</div>

</template>

<script>
// import language js
import 'codemirror/mode/javascript/javascript.js'

// import theme style
import 'codemirror/theme/lesser-dark.css'

// import more 'codemirror/some-resource...'

export default {
  data () {
    return {
      code: 'asdasdasd',
      cmOptions: {
        tabSize: 2,
        mode: 'text/javascript',
        theme: 'lesser-dark',
        lineNumbers: true,
        line: true
        // more CodeMirror options...
      }
    }
  },
  methods: {
    onCmReady (cm) {
      console.log('the editor is readied!', cm)
    },
    onCmFocus (cm) {
      console.log('the editor is focused!', cm)
    },
    onCmCodeChange (newCode) {
      console.log('this is new code', newCode)
      this.code = newCode
    }
  },
  computed: {
    codemirror () {
      return this.$refs.cmEditor.codemirror
    }
  }
}
</script>

<style>
  .el-row {
    margin-bottom: 20px;
  }
  .el-col {
    border-radius: 4px;
  }
  .grid-content {
    border-radius: 4px;
    margin: 1px;
  }
 .CodeMirror {
    border: 1px solid #eee;
    border-radius: 10px;
    padding: 5px;
    height: auto;
}
.CodeMirror-scroll {
  height: auto;
  overflow-y: hidden;
  overflow-x: auto;
}
</style>
