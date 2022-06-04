<template>
<el-container :class="{ darkMode: isDark}">
  <div style="padding-top: 15px;text-align:center;display: inline;">
  <span>加载已有模板：</span>
  <el-select
    style="width:15%;"
    v-model="platform_value"
    filterable placeholder="选择 Platform"
    size="small"
    >
    <el-option
      v-for="item in platform_options"
      :key="item"
      :label="item"
      :value="item"
    >
    </el-option>
  </el-select>
  <el-select style="width:20%;"
   v-model="template_value"
    filterable placeholder="选择 TextFSM 模板"
    @focus="getTemplateList()"
    no-data-text="请先选择 Platform"
    size="small"
    >
    <el-option
      v-for="item in template_options"
      :key="item"
      :label="item"
      :value="item"
    >
    </el-option>
  </el-select>
  <el-button id="loadTemplate"
    type="info" plain
    size="small"
    @click="loadTemplate()" icon="el-icon-plus"></el-button>
<div style="display: inline;float: right;margin-right: 20px;">
  <el-input-number v-model="fontSize" :min="12" :max="50" size="small"></el-input-number>
</div>
</div>
<el-main>
 <el-col :span="8" id="box1">
    <div class="grid-content" :style="{ fontSize: fontSize + 'px' }">
      <codemirror v-model="raw_text" placeholder="请输入原始 CLI 内容" :options="cmOptions" @input="textFSMParser()"/>
    </div>
  </el-col>
  <el-col :span="8" id="box2">
    <div class="grid-content" :style="{ fontSize: fontSize + 'px' }">
      <codemirror v-model="template_text" placeholder="请输入 TextFSM 模板内容" :options="cmOptions" @input="textFSMParser()"/>
    </div>
  </el-col>
  <el-col :span="8" id="box3">
    <div class="grid-content">
      <codemirror :style="{ fontSize: fontSize + 'px' }" placeholder="尚未匹配到结果..." :value="result" :options="cmOptions"/>
    </div>
  </el-col>
</el-main>
<el-footer>
  <el-switch style="padding:0 10px 0 10px;" active-color="#999" inactive-color="#1e1e1e" v-model="isDark" @change="changeTheme"></el-switch>
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
// import FilterableSelect from '../components/FilterableSelect.vue'

export default {
  data () {
    return {
      fontSize: 14,
      raw_text: '',
      template_text: '',
      result: '',
      isDark: false,
      cmOptions: {
        theme: 'idea',
        mode: 'javascript',
        lineNumbers: true,
        line: true
      },
      platform_options: [],
      platform_value: '',
      template_options: [],
      template_value: ''
    }
  },
  created () { this.getPlatformList() },
  methods: {
    textFSMParser () {
      // 这里上线的时候需要改一下，防止跨域问题
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
    getPlatformList () {
      axios.get('/parser/getPlatformList')
        .then(response => {
          this.platform_options = response.data.data.platform_list
        })
        .catch((error) => {
          console.log('Loding platform failed: ', error)
        })
    },
    getTemplateList () {
      const platform = this.platform_value
      axios.get('/parser/getTemplateList', {
        params: {
          platform: platform
        }
      })
        .then(response => {
          this.template_options = response.data.data.template_list
        })
        .catch((error) => {
          console.log('Loding template failed: ', error)
        })
    },
    loadTemplate () {
      const template = this.template_value
      axios.get('/parser/loadTemplate', {
        params: {
          template: template
        }
      })
        .then(response => {
          this.template_text = response.data.data.content
        })
        .catch((error) => {
          console.log('Loding template failed: ', error)
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
  },
  components: {
    // 'filter-select': FilterableSelect
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
  .darkMode span {
      color: #999;
  }
  .darkMode .el-select .el-input__inner {
      background-color: #1e1e1e;
  }
  .darkMode .el-button {
      background-color: #1e1e1e !important;
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
  }
  .vue-codemirror {
    height: 100%;
  }
  .CodeMirror-scroll {
    height: 100%;
  }
  .el-select{
    margin-right: 15px;
  }
</style>
