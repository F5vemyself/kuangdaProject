<template>
  <div id="app">
    


    <el-container>
      <el-header class="header-style">
        <h1>矿大信息管理系统</h1>
      </el-header>
      <!-- <el-container> -->
        <el-row class="tac">
          <el-col :span="5" class="left-nav">
            <el-menu
              default-active="2"
              class="el-menu-vertical-demo"
              @open="handleOpen"
              @close="handleClose"
              background-color="#545c64"
              text-color="#fff"
              active-text-color="#ffd04b">
              <el-menu-item index="1">
                <i class="el-icon-location"></i>
                <span slot="title"><a src="">采区信息</a></span>
              </el-menu-item>

              <el-submenu index="2">
                <template slot="title">
                  <i class="el-icon-menu"></i>
                  <span>工作面信息</span>
                </template>
                <el-menu-item-group>
                  <!-- <template slot="title"></template> -->
                  <el-menu-item index="1-1">基本数据</el-menu-item>
                  <el-menu-item index="1-2">支架数据</el-menu-item>
                  <el-menu-item index="1-3">微震数据</el-menu-item>
                </el-menu-item-group>
              </el-submenu>

              <el-menu-item index="3">
                <i class="el-icon-document"></i>
                <span slot="title">模型管理</span>
              </el-menu-item>

            </el-menu>
          </el-col>
          <el-col :span="16" class="right-main">

            <!-- 上方的导航栏 -->
            <!-- <el-breadcrumb separator="/" class="right-nav">
              <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
              <el-breadcrumb-item><a href="/imgdata">基本数据</a></el-breadcrumb-item>
              <el-breadcrumb-item><a href="/linedata">支架数据</a></el-breadcrumb-item>
              <el-breadcrumb-item><a href="/microdata">微震数据</a></el-breadcrumb-item>
              <el-breadcrumb-item></el-breadcrumb-item>
            </el-breadcrumb> -->
           
            <el-table
              :data="tableData"
              stripe
              style="width: 100%">
              <el-table-column
                prop="number"
                label="测线编号"
                width="180">
              </el-table-column>
              <el-table-column
                prop="date"
                label="日期"
                width="180">
              </el-table-column>
              <el-table-column
                prop="init_support"
                label="初撑力值"
                width="180">
              </el-table-column>
              <el-table-column
                prop="resistance_value"
                label="额定工作阻力值"
                width="180">
              </el-table-column>
              <el-table-column
                prop="support_strength"
                label="支护强度">
              </el-table-column>
            </el-table>
          </el-col>
        </el-row>
        

      <!-- <el-aside :span="24" class="left-nav">
      </el-aside>
      <el-main :span="18">
      </el-main> -->
      <!-- </el-container> -->
     
    </el-container>
    <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    // HelloWorld
  },
  data() {
      return {
        tableData: [{
          number: '1000',
          date: '2020-05-02 14:00',
          init_support: 230.2,
          resistance_value: 20.2,
          support_strength: 30
        }, {
          number: '1001',
          date: '2021-05-02 14:00',
          init_support: 130.2,
          resistance_value: 10.2,
          support_strength: 10
        }, {
          number: '1002',
          date: '2021-10-31 17:05',
          init_support: 21,
          resistance_value: 18,
          support_strength: 92
        }, {
          number: '1003',
          date: '2021-09-30 21:05',
          init_support: 334,
          resistance_value: 45,
          support_strength: 35
        }]
      }
  },
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /* margin-top: 60px; */
}
.header-style {
  height: 200px !important;
  text-align: center;
  line-height: 150px;
  background-color: #EBEEF5;
}
.left-nav{
  height: 600px !important;
  background-color: rgb(84, 92, 100);
}

.right-nav {
  margin-bottom: 30px;
}
.right-main {
  margin-left: 40px;
  margin-top: 30px;
}
</style>
