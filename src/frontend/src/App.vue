<template>
  <div id="app">
    <el-tabs type="border-card" @tab-click="handleClick" v-model="activeName">
      <el-tab-pane label="首页" name="index">
        <index :isReload="isReload"></index>
      </el-tab-pane>
      <el-tab-pane label="留言" name="mess" v-if="isMess">
        <board :username="username" @submitMess="submitMess"></board>
      </el-tab-pane>
      <el-tab-pane label="登录" name="login" v-if="isLogin">
        <login @submitForm="login"></login>
      </el-tab-pane>
      <el-tab-pane label="注册" name="register" v-if="isReg">
        <sign-up @submitForm="register"></sign-up>
      </el-tab-pane>
      <el-tab-pane label="退出" name="logout" v-if="isLogout">
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
import Login from './components/Login'
import SignUp from './components/SignUp'
import Board from './components/Board'
import Index from './components/Index'
export default {
  name: 'app',
  data: function () {
    return {
      username: '',
      isReload: 'No',
      isMess: false,
      isLogin: true,
      isLogout: false,
      isReg: true,
      activeName: "index",
    }
  },
  components: {
    Login,
    SignUp,
    Board,
    Index
  },
  methods: {
    handleClick (tab, event) {
      if(tab.name == 'logout'){
        this.logout()
      }
    },
    logout () {
      this.isMess = false
      this.isReg = true
      this.isLogin = true
      this.isLogout = false
      this.activeName = "login"
    },
    login (username) {
      this.username = username
      this.isMess = true
      this.isReg = false
      this.isLogin = false
      this.isLogout = true
      this.activeName = "index"
    },
    register (username) {
      this.username = username
      this.isMess = true
      this.isReg = false
      this.isLogin = false
      this.isLogout = true
      this.activeName = "index"
    },
    submitMess () {
      this.isMess = true
      this.isReg = false
      this.isLogin = false
      this.isLogout = true
      this.activeName = "index"
      this.isReload = 'OK'
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin: 60px 30px 60px 30px;
}
</style>
