<template>
<div>
  <el-row type="flex" justify="center">
    <el-col :span="8">
      <el-image :src="src" class="login_image"></el-image>
    </el-col>
  </el-row>
  <el-form :label-position="labelPosition" label-width="80px" :model="formLabelAlign">
    <el-row type="flex" justify="center">
      <el-col :span="8">
        <el-form-item label="用户名">
          <el-input v-model="formLabelAlign.username" placeholder="请输入用户名"></el-input>
        </el-form-item>
      </el-col>
    </el-row>
    <el-row type="flex" justify="center">
      <el-col :span="8">
        <el-form-item label="密码">
          <el-input v-model="formLabelAlign.passwd" placeholder="请输入密码"></el-input>
        </el-form-item>
      </el-col>
    </el-row>
    <el-form-item>
      <el-button type="primary" @click="submitForm">登录</el-button>
    </el-form-item>
  </el-form>
</div>
</template>

<script>
import Signup from './SignUp.vue'
const axios = require('axios')
export default {
  data: function() {
    return {
      labelPosition: 'left',
      formLabelAlign: {
        username: '',
        passwd: '',
      },
      src: 'https://cube.elemecdn.com/6/94/4d3ea53c084bad6931a56d5158a48jpeg.jpeg'
    }
  },
  methods: {
    submitForm () {
      let param = new URLSearchParams()
      param.append('username', this.formLabelAlign.username)
      param.append('passwd', this.formLabelAlign.passwd)
      axios.post('http://backend.docker.io/login/', param)
        .then(res => {
          if(res.data == 'userpass') {
            this.$notify.success({
              title: '提示',
              message: '登录成功！',
              showClose: false
            });
            this.$emit('submitForm', this.formLabelAlign.username)
          }
        })
    }
  },
  components: {
    Signup
  }
}
</script>

<style scoped>
.login_image {
  border-radius: 5px;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.1);
  margin-bottom: 30px;
}
</style>
