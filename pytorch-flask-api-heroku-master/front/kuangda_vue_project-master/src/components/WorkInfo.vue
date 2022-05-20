<template>
    <div>
        <!-- <el-container> -->
            <!-- <el-row class="tac"> -->
                <el-col :span="15" class="right-main">
                <h4>"{{mine_name}}" 工作面信息</h4>

                    <el-table
                    :data="tableData"
                    stripe
                    style="width: 100%">
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
                        <el-table-column label="操作">
                            <template slot-scope="scope">
                                <el-button @click="getWorkId(mine_name,scope.row.work_id)" type="text">微震数据</el-button>
                                <el-button @click="getZhijiaId(mine_name,scope.row.work_id)" type="text">支架数据</el-button>
                                <!-- <el-button @click="getMineId(scope.row.mine_id)" type="text">微震数据</el-button> -->
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
        mine_id: "",
        mine_name: ""
    };
    },
    methods: {
        getMessage() {
            
            // console.log("hello"); 
            console.log(this.$route.params);
            this.mine_id = this.$route.params['mine_id'];
            this.mine_name = this.$route.params['mine_name'];
           

            // 后端接口
            const path = 'http://localhost:5050/api/ShowWorkSpc/';
            axios.post(path,{"mine_id":this.mine_id})
                .then((res) => {
                    this.tableData = res.data;
                    console.log(res.data); 
                })
                .catch((error) => {
                    // eslint-disable-next-line
                    console.error(error);
                });
           
        },
        // 跳转到相应工作面的微震数据页面
        getWorkId(mine_name,work_id){
           this.$router.push({name:'weizhen_data',params:{
                "mine_name": mine_name,
                "work_id": work_id,
            }}) 
        },
        // 跳转到相应工作面的支架数据页面
        getZhijiaId(mine_name,work_id){
           this.$router.push({name:'zhijia_data',params:{
                "mine_name": mine_name,
                "work_id": work_id,
            }}) 
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