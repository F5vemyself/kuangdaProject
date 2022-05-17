<template>
    <div>
        <!-- <el-container> -->
            <!-- <el-row class="tac"> -->
                <el-col :span="3" class="right-main">
                   <el-select v-model="value" placeholder="请选择要查询的属性">
                        <el-option v-for="item in options"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value">
                        </el-option>
                    </el-select>
                </el-col> 
                <el-col :span="3" class="right-main">
                    <el-input v-model="input" placeholder="请输入具体信息"></el-input>
                </el-col>
                <el-col :span="2" class="right-main">
                    <el-button type="primary" icon="el-icon-search"  @click="inquireMine()">查询</el-button>
                </el-col>
                
                <el-col :span="2" class="right-main">
                    <el-button type="primary" @click="dialogFormVisible = true">新增</el-button>
                    <el-dialog title="新增矿井信息" :visible.sync="dialogFormVisible">
                        <el-form :model="form">
                            <el-form-item label="矿井编号" :label-width="formLabelWidth">
                                <el-input v-model="form.mine_id" autocomplete="off"></el-input>
                            </el-form-item>
                            <el-form-item label="矿井名称" :label-width="formLabelWidth">
                                <el-input v-model="form.mine_name" autocomplete="off"></el-input>
                            </el-form-item>
                        </el-form>
                        <div slot="footer" class="dialog-footer">
                            <el-button @click="dialogFormVisible = false">取 消</el-button>
                            <el-button type="primary" @click="insertMine()">确 定</el-button>
                        </div>
                    </el-dialog>
                </el-col>
                 <el-col :span="2" class="right-main">
                    <el-button type="success" icon="el-icon-success" @click="getMessage()">显示所有信息</el-button>
                </el-col>
                <el-col :span="15" class="right-main">
                    <el-table
                    :data="tableData"
                    stripe
                    style="width: 100%">
                        <el-table-column
                            fixed
                            label="矿井编号"
                            width="300">
                            <template slot-scope="scope">
                                {{scope.row.mine_id}}
                            </template>
                        </el-table-column>
                          <el-table-column
                            label="矿井名称"
                            width="300">
                            <template slot-scope="scope">
                                {{scope.row.mine_name}}
                            </template>
                        </el-table-column>
                        <el-table-column label="操作">
                            <template slot-scope="scope">
                                <el-button @click="getMineId(scope.row.mine_id)" type="text">查看工作面信息</el-button>
                                <el-button @click="showMineInfoDialog(scope.row.mine_id,scope.row.mine_name)" type="text">编辑</el-button>
                                <el-button @click="deleteMineInfo(scope.row.mine_id)" type="text">删除</el-button>
                            </template>
                        </el-table-column>
                    </el-table>
                </el-col>
                

                <!-- 修改矿井的dialog -->
                <el-dialog title="修改矿井信息" :visible.sync="dialogFormVisible2">
                    <el-form :model="form2">
                        <el-form-item label="矿井编号" :label-width="formLabelWidth2">
                            <el-input v-model="form2.mine_id" autocomplete="off"></el-input>
                        </el-form-item>
                        <el-form-item label="矿井名称" :label-width="formLabelWidth2">
                            <el-input v-model="form2.mine_name" autocomplete="off"></el-input>
                        </el-form-item>
                    </el-form>
                    <div slot="footer" class="dialog-footer">
                        <el-button @click="dialogFormVisible2 = false">取 消</el-button>
                        <el-button type="primary" @click="editMineInfo(form2.mine_id,form2.mine_name)">确 定</el-button>
                    </div>
                </el-dialog>
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
            input:'',
            // 新增信息dialog
            dialogFormVisible: false,
            form: {
                mine_id: '',
                mine_name: '',
            },
            formLabelWidth: '80px',

            //编辑信息dialog
            dialogFormVisible2: false,
            form2: {
                mine_id: '',
                mine_name: '',
            },
            formLabelWidth2: '80px',

            // 编辑矿井前的信息
            old_mine_id:'',
            old_mine_name:'',

            // 下拉菜单选项
            options: [{
                value: 'mine_id',
                label: '矿井编号'
            }, {
                    value: 'mine_name',
                    label: '矿井名称'
            }],
                value: ''
        };
    },
    methods: {

        // 查询所有矿区的信息
        getMessage() {
            const path = 'http://localhost:5050/api/mine_info';
            axios.get(path)
                .then((res) => {
                    this.tableData = res.data;    
                })
                .catch((error) => {
                    // eslint-disable-next-line
                    console.error(error);
                });
        },
        // 根据相应矿井的编号_进行页面跳转，显示对应的工作面信息
        getMineId(mine_id){
            this.$router.push({name:'work',params:{"mine_id":mine_id}})
        },

        // 插入矿井信息
        insertMine() {
            const path = 'http://localhost:5050/api/insert_mine_info';
            var mine_info = {
                'mine_id':this.form.mine_id,
                'mine_name':this.form.mine_name
            };
            // 根据矿井的mine_id查询信息
            axios.post(path,mine_info)
                .then((res) => {     
                    this.dialogFormVisible = false;      
                    this.$message({
                        message: res.data,
                        type: 'success'
                    })
                    // 刷新当前页面,更新数据
                    this.getMessage();
                })
                .catch((error) => {
                    console.error(error);
                })
        },

        // 删除相应的信息
        deleteMineInfo(mine_id){
            this.$confirm('此操作将永久删除该条信息, 是否继续?', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning'
            }).then(() => {
                var mine_data = {
                    'mine_id': mine_id
                };
                const path = 'http://localhost:5050/api/delete_mine_info';
                axios.post(path,mine_data)
                .then((res) => {
                    this.$message({
                        message: res.data,
                        type: 'success'
                    });
                    // 刷新页面信息
                    this.getMessage();
                })
                .catch((error) => {
                    // eslint-disable-next-line
                    console.error(error);
                });
            }).catch(() => {
                this.$message({
                    type: 'info',
                    message: '已取消删除'
                });          
            });
        },

        // 显示编辑矿井信息的Dialog
        showMineInfoDialog(mine_id,mine_name){
            console.log(mine_id,mine_name)
            // 修改矿井信息对应的dialog
            this.dialogFormVisible2 = true;
            this.form2.mine_id= mine_id;
            this.old_mine_id  = mine_id;
            this.form2.mine_name = mine_name;
            this.old_mine_name = mine_name;
            console.log(this.form2.mine_id,this.form2.mine_name);
            // 返回原有的mine_id和mine_name
            // return this.form2.mine_id,this.form2.mine_name;
        },
        editMineInfo(mine_id,mine_name){
            var mine_data = {
                'old_mine_id': this.old_mine_id,
                'old_mine_name': this.old_mine_name,
                'new_mine_id': Number(mine_id),
                'new_mine_name': mine_name
            }
            console.log(mine_data);
            const path = 'http://localhost:5050/api/edit_mine_info';
            // 根据矿井的mine_id查询信息
            axios.post(path,mine_data)
                .then((res) => {
                    this.dialogFormVisible2 = false; 
                    this.$message({
                        message: res.data,
                        type: 'success'
                    });
                    this.getMessage();
                    // this.tableData = res.data;
                })
                .catch((error) => {
                    console.error(error);
                })
        },

        // 根据矿井编号查询信息
        inquireMine(){
            const path = 'http://localhost:5050/api/inquire_mine';
            var mine_data = {
                'searchName': this.value,
                'searchValue': this.input,
            };
            // 根据矿井的mine_id查询信息
            axios.post(path,mine_data)
                .then((res) => {
                    this.tableData = res.data;
                })
                .catch((error) => {
                    console.error(error);
                })
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