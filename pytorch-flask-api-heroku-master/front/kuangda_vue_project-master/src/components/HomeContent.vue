<template>
    <div>
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

            
        <!-- </el-container> -->
            
    </div>    
</template>

<script>
export default {
    
}
</script>
<style scoped>
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