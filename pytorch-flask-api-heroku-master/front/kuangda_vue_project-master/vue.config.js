// 打包相关的配置

const { defineConfig } = require("@vue/cli-service");
module.exports = defineConfig({
  transpileDependencies: true,

  // 解决vue项目打包后找不到静态资源的问题
  publicPath: "./",
  // 解决跨域问题新增的
  // devServer: {
  //   proxy: {
  //     "/": {
  //       target: "http://localhsot:5050",
  //       changeOrigin: true,
  //     },
  //   },
  // },
});
