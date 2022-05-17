<template>
    <div>
        <!-- <el-container> -->
            <!-- <el-row class="tac"> -->
                <el-col :span="17" class="right-main">
                    <el-table
                    :data="tableData"
                    stripe
                    style="width: 100%">
                        
                        <el-table-column
                            label="工作面编号"
                            width="200">
                            <template slot-scope="scope">
                                {{scope.row.work_id}}
                            </template>
                        </el-table-column>

                        <el-table-column
                            label="测线编号"
                            width="200">
                            <template slot-scope="scope">
                                {{scope.row.cexian_id}}
                            </template>
                        </el-table-column>

                        <el-table-column
                            label="时间"
                            width="200">
                            <template slot-scope="scope">
                                {{scope.row.time}}
                            </template>
                        </el-table-column>

                        <el-table-column
                            label="循环编号"
                            width="200">
                            <template slot-scope="scope">
                                {{scope.row.circle_id}}
                            </template>
                        </el-table-column>

                        <el-table-column
                            label="初撑力值"
                            width="200">
                            <template slot-scope="scope">
                                {{scope.row.init_f}}
                            </template>
                        </el-table-column>

                        <el-table-column
                            label="循环末最大阻力"
                            width="200">
                            <template slot-scope="scope">
                                {{scope.row.max_f}}
                            </template>
                        </el-table-column>

                        <el-table-column
                            label="循环时间加权阻力"
                            width="200">
                            <template slot-scope="scope">
                                {{scope.row.weight_f}}
                            </template>
                        </el-table-column>
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
            const path = 'http://localhost:5050/api/zhijia_info';
            axios.get(path)
                .then((res) => {
                    this.tableData = res.data;
                    console.log(this.tableData);
                    
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