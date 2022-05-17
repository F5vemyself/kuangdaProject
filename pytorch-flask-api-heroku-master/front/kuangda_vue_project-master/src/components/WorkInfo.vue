<template>
    <div>
        <!-- <el-container> -->
            <!-- <el-row class="tac"> -->
                <el-col :span="15" class="right-main">
                    <el-table
                    :data="tableData"
                    stripe
                    style="width: 100%">
                        <!-- <el-table-column
                            v-for="(item,index) in tableData"
                            :key="index"
                            prop="item.id"
                            label="矿井编号"
                            width="180">
                        </el-table-column> -->
                        <el-table-column
                            label="工作面编号"
                            width="300">
                            <template slot-scope="scope">
                                {{scope.row.work_id}}
                            </template>
                        </el-table-column>
                          <el-table-column
                            label="工作面名称">
                            <template slot-scope="scope">
                                {{scope.row.work_name}}
                            </template>
                        </el-table-column>

                        <!-- <el-table-column label="操作">
                             <template slot-scope="scope">
                                <el-button @click="showWorkInfo(scope.row.id)">工作面信息</el-button>
                            </template>
                        </el-table-column> -->

                    </el-table>
                </el-col>
            <!-- </el-row> -->

        
        <!-- </el-container> -->
            
    </div>    
</template>

<script>
import axios from 'axios';
export default {
    data() {
        return {
        tableData: [
        ],
    };
    },
    methods: {
        getMessage() {
            
            // console.log("hello"); 
            console.log(this.$route.params);
            const mine_id = this.$route.params;
            // 后端接口
            const path = 'http://localhost:5050/api/ShowWorkSpc/';
            axios.post(path,mine_id)
                .then((res) => {
                    this.tableData = res.data;
                    // console.log(res.data); 
                })
                .catch((error) => {
                    // eslint-disable-next-line
                    console.error(error);
                });
           
        },
    },
    created() {
        this.getMessage();
    },
}
</script>
<style scoped>
.right-nav {
  margin-bottom: 30px;
}
.right-main {
  margin-left: 40px;
  margin-top: 30px;
} 
</style>