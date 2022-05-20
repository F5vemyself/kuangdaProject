import Vue from "vue";
import Router from "vue-router";
Vue.use(Router);

const routes = [
  { path: "/", component: () => import("../view/HomePage.vue") },
  { path: "/mine", component: () => import("../view/MinePage.vue") },
  {
    path: "/work/:mine_id",
    component: () => import("../view/WorkPage.vue"),
    name: "work",
  },
  {
    path: "/zhijia_data/:work_id",
    component: () => import("../view/ZhijiaPage.vue"),
    name: "zhijia_data",
  },
  {
    path: "/weizhen_data/:work_id",
    component: () => import("../view/WeizhenPage.vue"),
    name: "weizhen_data",
  },

  // 路由配置
  {
    // 如果找不到路由，跳到根目录
    path: "*",
    redirect: "/",
  },
];

const router = new Router({
  routes,
  mode: "hash", //mode=hash，home页面就是/#/的形式，mode=history，home页面就是/的形式
});

export default router;
