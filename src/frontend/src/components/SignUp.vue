<template>
<div>
  <el-row type="flex" justify="center">
    <el-col :span="8">
      <el-image :src="src" class="login_image"></el-image>
    </el-col>
  </el-row>
  <el-form :model="ruleForm" :label-position="labelPosition" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
  <el-row type="flex" justify="center">
    <el-col :span="8">
      <el-form-item label="用户名" prop="username">
        <el-input type="text" v-model="ruleForm.username" autocomplete="on"></el-input>
      </el-form-item>
    </el-col>
  </el-row>
  <el-row type="flex" justify="center">
    <el-col :span="8">
      <el-form-item label="邮箱" prop="email">
        <el-input type="email" v-model="ruleForm.email" autocomplete="off"></el-input>
      </el-form-item>
    </el-col>
  </el-row>
  <el-row type="flex" justify="center">
    <el-col :span="8">
      <el-form-item label="密码" prop="pass">
        <el-input type="password" v-model="ruleForm.pass" autocomplete="off"></el-input>
      </el-form-item>
    </el-col>
  </el-row>
  <el-row type="flex" justify="center">
    <el-col :span="8">
      <el-form-item label="确认密码" prop="checkPass">
        <el-input type="password" v-model="ruleForm.checkPass" autocomplete="off"></el-input>
      </el-form-item>
    </el-col>
  </el-row>
  <el-form-item>
    <el-button type="primary" @click="submitForm('ruleForm')">提交</el-button>
  </el-form-item>
  </el-form>
</div>
</template>

<script>
const axios = require('axios')
export default {
  name: 'signup',
  data: function () {
    var validatePass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入密码'));
      } else {
        if (this.ruleForm.checkPass !== '') {
          this.$refs.ruleForm.validateField('checkPass');
        }
        callback();
      }
    };
    var validatePass2 = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'));
      } else if (value !== this.ruleForm.pass) {
        callback(new Error('两次输入密码不一致!'));
      } else {
        callback();
      }
    };
    return {
      src: 'https://cube.elemecdn.com/6/94/4d3ea53c084bad6931a56d5158a48jpeg.jpeg',
      labelPosition: 'left',
      ruleForm: {
        username: '',
        email: '',
        pass: '',
        checkPass: ''
      },
      rules: {
        username: [
          { required: true, trigger: 'blur', message: '请输入用户名' },
          { max: 12, message: '请不要超过12个字符', trigger: 'blur' } 
        ],
        email: [
          { required: true, message: '请输入邮箱地址', trigger: 'blur' },
          { type: 'email', message: '请输入正确的邮箱地址', trigger: ['blur', 'change'] }
        ],
        pass: [
          { validator: validatePass, trigger: 'blur', required: true}
        ],
        checkPass: [
          { validator: validatePass2, trigger: 'blur', required: true }
        ]
      }
    };
  },
  methods: {
    submitForm (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          let data = {
            username: '',
            email: '',
            pass: '',
          }
          let param = new URLSearchParams()
          param.append('username', this.ruleForm.username)
          param.append('pass', this.ruleForm.pass)
          param.append('email', this.ruleForm.email)
          axios.post('http://backend.docker.io/register/', param)
            .then((res)=> {
              if (res.data == 'registersuccess') {
                this.$notify.success({
                  title: '提示',
                  message: '注册成功！',
                  showClose: false
                });
                this.$emit('submitForm', this.ruleForm.username)
              }
            })
        } else {
          return false;
        }
      });
    }
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
