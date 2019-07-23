<template>
  <div>
    <el-row type="flex" justify="center">
      <el-col :span="12">
        <el-image :src="src" class="login_image"></el-image>
      </el-col>
    </el-row>
    <el-form ref="messForm" :model="messForm" :rules="rules" label-width="80px">
      <el-row type="flex" justify="center">
        <el-col :span="12">
          <el-form-item label="留言内容" prop="content">
            <el-input type="textarea" v-model="messForm.content"></el-input>
          </el-form-item>
        </el-col>
      </el-row>
      <el-row type="flex" justify="center">
        <el-col :span="12">
          <el-form-item label="分类标签">
              <el-radio-group v-model="messForm.tag">
                <el-radio :label="0" name="type">情感</el-radio>
                <el-radio :label="1" name="type">生活</el-radio>
                <el-radio :label="2" name="type">学术</el-radio>
                <el-radio :label="3" name="type">娱乐</el-radio>
                <el-radio :label="4" name="type">体育</el-radio>
                <el-radio :label="5" name="type">科技</el-radio>
              </el-radio-group>
          </el-form-item>
      </el-col>
      </el-row>
      <el-form-item>
          <el-button type="primary" @click="submitMess('messForm')">立即发布</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
const axios = require('axios')
export default {
  data: function () {
    return {
      messForm: {
        tag: 0,
        content: ''
      },
      rules: {
        content: [
          { required: true, trigger: 'blur', message: '你还没有留言' },
          { max: 300, message: '请不要超过300个字符', trigger: 'blur' } 
        ],
      },
      src: 'https://cube.elemecdn.com/6/94/4d3ea53c084bad6931a56d5158a48jpeg.jpeg'
    }
  },
  props: {
    username: {
      type: String
    }
  },
  methods: {
    submitMess (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          let param = new URLSearchParams()
          param.append('username', this.username)
          param.append('content', this.messForm.content)
          param.append('tag', this.messForm.tag)
          param.append('created_time', (new Date()).toLocaleString())      
          axios.post('http://backend.docker.io/addMessage/', param)
            .then((res)=> {
              if (res.data == 'messagesuccess') {
                this.$notify.success({
                  title: '提示',
                  message: '留言成功！',
                  showClose: false
                });
                this.messForm.content = ''
                this.messForm.tag = 0
                this.$emit('submitMess')
              }
            })
        } else {
          return false;
        }
      });
    }
  },
}
</script>

<style scoped>
.login_image {
  border-radius: 5px;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.1);
  margin-bottom: 30px;
}
</style>

