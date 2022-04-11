<template>
<el-container v-bind:class="{ darkMode: isDark}">
<el-main>
 <el-col :span="8">
    <div class="grid-content">
   <codemirror v-model="raw_text"
    placeholder="请输入原始 CLI 内容"
    :options="cmOptions"
    @input="textFSMParser()"/>
    </div>
  </el-col>
  <el-col :span="8">
    <div class="grid-content">
  <codemirror v-model="template_text"
    placeholder="请输入 TextFSM 模板内容"
    :options="cmOptions"
    @input="textFSMParser()"
  />
    </div>
  </el-col>
  <el-col :span="8">
    <div class="grid-content">
  <codemirror
    placeholder="尚未匹配到结果..."
    :value="result"
    :options="cmOptions"
  />
    </div>
  </el-col>
</el-main>
<el-footer>
  <el-switch style="padding:0 10px 0 10px;"
    active-color="#999"
    inactive-color="#1e1e1e"
    v-model="isDark"
    @change="changeTheme"
    >
  </el-switch>
  <a href="https://beian.miit.gov.cn/" target="_blank">京ICP备2022010024号</a>
  <a href="https://github.com/xdai555/" target="_blank">@xdai555</a>
</el-footer>
</el-container>
</template>

<script>
import axios from 'axios'
import 'codemirror/lib/codemirror.css'
import 'codemirror/mode/javascript/javascript'
import 'codemirror/addon/display/placeholder.js'
import 'codemirror/theme/idea.css'
import 'codemirror/theme/darcula.css'

export default {
  data () {
    return {
      raw_text: '',
      template_text: '',
      result: '',
      isDark: false,
      cmOptions: {
        theme: 'idea',
        mode: 'javascript',
        lineNumbers: true,
        line: true
      }
    }
  },
  methods: {
    textFSMParser () {
      axios.post('/parser', {
        raw_text: this.raw_text,
        template_text: this.template_text
      })
        .then(response => {
          this.result = this.jsonFormat(JSON.stringify(response.data))
        })
        .catch(error => {
          this.result = this.jsonFormat(JSON.stringify(error))
        })
    },
    jsonFormat (jsonStr) {
      const beautifyJS = require('js-beautify').js_beautify
      const formattedJSON = beautifyJS(jsonStr, { indent_size: 2, brace_style: 'expand' })
      return formattedJSON
    },
    changeTheme () {
      if (this.isDark === true) {
        this.cmOptions.theme = 'darcula'
      } else { this.cmOptions.theme = 'idea' }
    }
  }
}
</script>

<style>
  .darkMode {
    background: #1e1e1e;
  }
  .darkMode svg path {
      stroke: #999;
  }
  .darkMode a {
      color: #999;
  }
  a {
    color: #1e1e1e;
    margin-right: 5px
  }
  svg path {
      stroke: #333;
  }
  .el-container {
    height: 100%;
  }
  .el-footer {
    height: 23px !important;
    text-align: center;
    font-size: 90%;
    margin-bottom: 5px
  }
  .el-col {
    border-radius: 4px;
    height: 100%;
  }
  .grid-content {
    border-radius: 4px;
    margin: 1px;
    height: 100%;
  }
  .CodeMirror {
      border: 1px solid;
      border-radius: 10px;
      padding: 5px;
      height: 100%; /* viewport height */
      font-size: 14px;
  }
  .vue-codemirror {
    height: 100%;
  }
  .CodeMirror-scroll {
    height: 100%;
  }
</style>
