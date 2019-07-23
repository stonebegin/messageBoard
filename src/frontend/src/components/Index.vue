<template>
  <div>
    <el-row>
      <el-col :span="8" v-for="(item, index) in content" :key="index" :offset="2" style="margin-bottom: 30px">
        <el-card :body-style="{ padding: '0px' }">
          <div style="padding: 14px;">
            <p>留言者：{{item.fields.author}}</p>
            <el-tag type="success" style="margin-right: 20px" effect="dark">{{tagNames[item.fields.tag]}}</el-tag>
            <el-tag style="margin-right: 20px">赞数{{item.fields.good}}</el-tag>
            <el-tag type="info">踩数{{item.fields.bad}}</el-tag>
            <div class="text" style="height: 150px; margin-top: 30px">{{item.fields.body}}</div>
            <div class="bottom clearfix">
              <time class="time">留言时间：{{ item.fields.created_time }}</time>
              <!-- <el-button type="text" v-if="isVoted" @click="addVoteTwo" class="button">赞</el-button> -->
              <el-button type="text" @click="addRefuse(item)" class="button">踩</el-button>
              <el-button type="text" class="button"></el-button>
              <el-button type="text" @click="addVote(item)" class="button">赞</el-button>
              <!-- <el-button type="text" v-if="isRefused" @click="addRefuseTwo" class="button">踩</el-button> -->
            </div>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
const axios = require('axios')
export default {
  data: function () {
    return {
      content: [],
      currentDate: new Date(),
      tagNames: ['情感', '生活', '学术', '娱乐', '体育', '科技'],
      isVoted: false,
      isRefused: false
    }
  },
  props: ['isReload'],
  watch: {
    isReload: function () {
      if (this.isReload == 'OK') {
        const vm = this;
        axios.get('http://backend.docker.io/index/')
          .then(res => {
            vm.content = res.data
          })
      }
    },
    deep: true,
    immediate: true,
  },
  mounted() {
    const vm = this;
    axios.get('http://backend.docker.io/index/')
      .then(res => {
        vm.content = res.data
      })
  },
  methods: {
    addVote (item) {
      const vm = this
      vm.isVoted = true
      let param = new URLSearchParams()
      param.append('author', item.fields.author)
      param.append('created_time', item.fields.created_time)
      param.append('good', item.fields.good + 1)
      axios.post('http://backend.docker.io/addvote/', param)
        .then(res => {
          return
        })
    },
    addRefuse (item) {
      const vm = this
      vm.isRefused = true
      let param = new URLSearchParams()
      param.append('author', item.fields.author)
      param.append('created_time', item.fields.created_time)
      param.append('bad', item.fields.bad + 1)
      axios.post('http://backend.docker.io/addrefuse/', param)
        .then(res => {
          return
        })
    },
  }
}
</script>

<style>
  .time {
    font-size: 13px;
    color: #999;
  }

  .text {
    font-size: 16px;
  }
  
  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

  .button {
    padding: 0;
    float: right;
  }

  .image {
    width: 100%;
    display: block;
  }

  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }
  
  .clearfix:after {
      clear: both
  }
</style>