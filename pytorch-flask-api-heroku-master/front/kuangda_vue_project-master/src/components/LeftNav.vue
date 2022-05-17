<template>
    <div>
        <!-- <el-container> -->
            <!-- <el-row class="tac"> -->
                <el-col :span="5" class="left-nav">
                    <el-menu
                        default-active="2"
                        class="el-menu-vertical-demo"
                        @open="handleOpen"
                        @close="handleClose"
                        background-color="#545c64"
                        text-color="#fff"
                        active-text-color="#ffd04b"
                        router>
                        <el-menu-item index="/mine">
                            <i class="el-icon-location"></i>
                            <span slot="title">采区信息</span>
                        </el-menu-item>
                   

                        <el-submenu index="2">
                            <template slot="title">
                            <i class="el-icon-menu"></i>
                            <span>工作面信息</span>
                            </template>
                            <el-menu-item-group>
                            <!-- <template slot="title"></template> -->
                            <el-menu-item index="/basic_data">基本数据</el-menu-item>
                            <el-menu-item index="/zhijia_data">支架数据</el-menu-item>
                            <el-menu-item index="/weizhen_data">微震数据</el-menu-item>
                            </el-menu-item-group>
                        </el-submenu>

                        <el-menu-item index="3">
                            <i class="el-icon-document"></i>
                            <span slot="title">模型管理</span>
                        </el-menu-item>

                    </el-menu>
                </el-col>


                
            <!-- </el-row> -->

            
        <!-- </el-container> -->
            
    </div>    
</template>

<script>
export default {
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
<style scoped>
.left-nav{
  height: 900px !important;
  background-color: rgb(84, 92, 100);
}

</style>