<template>
  <div id="app">

    <!-- 渲染router组件 -->
    <router-view></router-view>
    
  </div>
</template>

<script>
// import HeaderInfo from './components/HeaderInfo.vue'
// import HomeContent from './components/HomeContent.vue'
// import MineInfo from './components/MineInfo.vue'
export default {
  name: 'App',
  components: {
      // MineInfo,
      // HomeContent
  },
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

</style>
