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
                    <el-button type="primary" icon="el-icon-search"  @click="inquireWeizhen()">查询</el-button>
                </el-col>
                <el-col :span="2" class="right-main">
                    <el-button type="success" icon="el-icon-success" @click="getMessage()">显示所有信息</el-button>
                </el-col>
                <el-col :span="3" class="right-main">
                    <el-button type="primary" icon="el-icon-circle-plus" @click="dialogFormVisible = true">新增</el-button>
                    <el-dialog title="新增微震信息" :visible.sync="dialogFormVisible">
                        <el-form :model="form" label-position="right">
                            <el-form-item label="工作面编号" :label-width="formLabelWidth">
                                <el-input v-model="form.work_id" autocomplete="off"></el-input>
                            </el-form-item>
                            <el-form-item label="循环编号" :label-width="formLabelWidth">
                                <el-input v-model="form.circle_id" autocomplete="off"></el-input>
                            </el-form-item>
                            <el-form-item label="日期时间" :label-width="formLabelWidth">
                            <div class="block" >
                                <span class="demonstration"></span>
                                <el-date-picker
                                    v-model="form.wz_time"
                                    type="datetime" value-format="yyyy-MM-dd HH:mm:ss"
                                    placeholder="选择日期时间">
                                </el-date-picker>
                            </div>
                             </el-form-item>
                            <el-form-item label="微震位置x坐标" :label-width="formLabelWidth">
                                <el-input v-model="form.ax_x" autocomplete="off"></el-input>
                            </el-form-item>
                            <el-form-item label="微震位置y坐标" :label-width="formLabelWidth">
                                <el-input v-model="form.ax_y" autocomplete="off"></el-input>
                            </el-form-item>
                            <el-form-item label="微震位置z坐标" :label-width="formLabelWidth">
                                <el-input v-model="form.ax_z" autocomplete="off"></el-input>
                            </el-form-item>
                            <el-form-item label="微震能量" :label-width="formLabelWidth">
                                <el-input v-model="form.energy" autocomplete="off"></el-input>
                            </el-form-item>
                            <el-form-item label="层级" :label-width="formLabelWidth">
                                <el-input v-model="form.level" autocomplete="off"></el-input>
                            </el-form-item>
                        </el-form>
                        <div slot="footer" class="dialog-footer">
                            <el-button @click="dialogFormVisible = false">取 消</el-button>
                            <el-button type="primary" @click="insertWeizhen()">确 定</el-button>
                        </div>
                    </el-dialog>
                </el-col>
                <el-col :span="16" class="right-main">
                    <el-table
                    :data="tableData"
                    stripe 
                    style="width: 100%">
                        <el-table-column
                            label="工作面编号"
                            width="150"
                            align="center">
                            <template slot-scope="scope">
                                {{scope.row.work_id}}
                            </template>
                        </el-table-column>

                        <el-table-column
                            label="循环编号"
                            width="150"
                            align="center">
                            <template slot-scope="scope">
                                {{scope.row.circle_id}}
                            </template>
                        </el-table-column>

                        <el-table-column
                            label="微震时间"
                            width="200"
                            align="center">
                            <template slot-scope="scope">
                                {{scope.row.wz_time}}
                            </template>
                        </el-table-column>

                        <el-table-column
                            label="微震位置"
                            width="300"
                            align="center">
                            <template slot-scope="scope">
                                {{scope.row.wz_coordinate}}
                            </template>
                        </el-table-column>

                        <el-table-column
                            label="微震能量"
                            width="200"
                            align="center">
                            <template slot-scope="scope">
                                {{scope.row.energy}}
                            </template>
                        </el-table-column>

                        <el-table-column
                            label="层级"
                            width="200"
                            align="center">
                            <template slot-scope="scope">
                                {{scope.row.level}}
                            </template>
                        </el-table-column>

                         <el-table-column label="操作" fixed="right" width="100">
                            <template slot-scope="scope">
                                <el-button @click="showWeizhenInfoDialog(scope.row.work_id,scope.row.circle_id,
                                scope.row.ax_x,scope.row.ax_y,scope.row.ax_z,
                                scope.row.wz_time,scope.row.energy,scope.row.level)" type="text">编辑</el-button>
                                <el-button @click="deleteWeizhenInfo(scope.row.work_id,scope.row.circle_id,
                                scope.row.ax_x,scope.row.ax_y,scope.row.ax_z,
                                scope.row.wz_time,scope.row.energy,scope.row.level)" type="text">删除</el-button>
                            </template>
                        </el-table-column>
 
                    </el-table>
                </el-col>

                 <!-- 修改微震信息的dialog -->
                <el-dialog title="修改微震信息" :visible.sync="dialogFormVisible2">
                    <el-form :model="form2">
                        <el-form-item label="工作面编号" :label-width="formLabelWidth">
                            <el-input v-model="form2.work_id" autocomplete="off"></el-input>
                        </el-form-item>
                        <el-form-item label="循环编号" :label-width="formLabelWidth">
                            <el-input v-model="form2.circle_id" autocomplete="off"></el-input>
                        </el-form-item>
                        <el-form-item label="日期时间" :label-width="formLabelWidth">
                            <div class="block" >
                                <span class="demonstration"></span>
                                <el-date-picker
                                    v-model="form2.wz_time"
                                    type="datetime" value-format="yyyy-MM-dd HH:mm:ss"
                                    placeholder="选择日期时间">
                                </el-date-picker>
                            </div>
                        </el-form-item>
                        <el-form-item label="微震位置x坐标" :label-width="formLabelWidth">
                            <el-input v-model="form2.ax_x" autocomplete="off"></el-input>
                        </el-form-item>
                        <el-form-item label="微震位置y坐标" :label-width="formLabelWidth">
                            <el-input v-model="form2.ax_y" autocomplete="off"></el-input>
                        </el-form-item>
                        <el-form-item label="微震位置z坐标" :label-width="formLabelWidth">
                            <el-input v-model="form2.ax_z" autocomplete="off"></el-input>
                        </el-form-item>
                        <el-form-item label="微震能量" :label-width="formLabelWidth">
                            <el-input v-model="form2.energy" autocomplete="off"></el-input>
                        </el-form-item>
                        <el-form-item label="层级" :label-width="formLabelWidth">
                            <el-input v-model="form2.level" autocomplete="off"></el-input>
                        </el-form-item>
                    </el-form>

                    <div slot="footer" class="dialog-footer">
                        <el-button @click="dialogFormVisible2 = false">取 消</el-button>
                        <el-button type="primary" @click="editWeizhenInfo(form2.work_id,form2.circle_id,
                        form2.ax_x,form2.ax_y,form2.ax_z,form2.wz_time,form2.energy,form2.level)">确 定</el-button>
                    </div>
                </el-dialog>

                <!-- 分页模块 -->
                <el-col :span="17" class="right-main">
                    <el-pagination
                            background
                            @size-change="handleSizeChange"
                            @current-change="handleCurrentChange"
                            :current-page.sync="currentPage"
                            :page-sizes="[5, 10]"
                            :page-size="5"
                            layout="total, sizes, prev, pager, next, jumper"
                            :total="parseInt(count)">
                    </el-pagination> 

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
            input: '',
            tableData: [],
            currentPage: 1,
            pageSize: 5,
            count : null,
            table_id: 1,

            // 下拉菜单信息
            options: [{
                value: 'work_id',
                label: '工作面编号'
            }, {
                    value: 'circle_id',
                    label: '循环编号'
            },{
                    value: 'energy',
                    label: '微震能量'
            },{
                    value: 'level',
                    label: '层级'
            }],
                value: '',

            // 新增信息dialog
            dialogFormVisible: false,
            form: {
                work_id: '',
                circle_id: '',
                ax_x: '',
                ax_y: '',
                ax_z: '',
                wz_time: '',
                energy: '',
                level: ''
            },

            // 修改微震信息的dialog数据
            dialogFormVisible2: false,
            formLabelWidth: '120px', 
            form2: {
                work_id: '',
                circle_id: '',
                ax_x: '',
                ax_y: '',
                ax_z: '',
                wz_time: '',
                energy: '',
                level: ''
            },

            // 修改微震信息前的信息
            old_work_id: '',
            old_circle_id: '',
            old_ax_x: '',
            old_ax_y: '',
            old_ax_z: '',
            old_wz_time: '',
            old_energy: '',
            old_level: ''
        };
    },
    methods: {
        getMessage() {
            // table_id = 1表示查询所有信息
            this.table_id = 1;
            const path = 'http://localhost:5050/api/weizhen_info';

            // 分页所需的数据
            var page_data = {
                'page_num': this.currentPage,    //当前页码
                'page_size': this.pageSize       //每页显示的信息数
            };
            axios.post(path,page_data)
                .then((res) => {
                    // 获取res.data数组的对象个数
                    var records_num = res.data.length;
                    // count信息包含在最后一个对象里面
                    var countObject = res.data[records_num-1];
                    this.count = countObject['count'];
                    // 删除count信息
                    res.data.pop();
                    // 显示除count以外的信息，即数据库返回的数据
                    this.tableData = res.data;
                       
                })
                .catch((error) => {
                    // eslint-disable-next-line
                    console.error(error);
                });
        },
        inquireWeizhen(){
            // table_id = 2表示根据属性查询信息
            this.table_id = 2;
            const path = 'http://localhost:5050/api/inquire_weizhen';
            var data = {
                // 下拉菜单相关的内容
                'searchName': this.value,
                'searchValue': this.input,
                // 分页查询相关的内容
                'page_num': this.currentPage,
                'page_size': this.pageSize
            };
            // 根据用户选择的属性，以及输入的属性值查询信息
            axios.post(path,data)
                .then((res) => {
                    // 修改数据条数count
                    var records_num = res.data.length;
                    var countObject = res.data[records_num-1];
                    this.count = countObject['count'];
                     // 删除count信息
                    res.data.pop();
                    this.tableData = res.data;
                })
                .catch((error) => {
                    console.error(error);
                })
        },
        // 插入微震信息
        insertWeizhen() {
            const path = 'http://localhost:5050/api/insert_weizhen_info';
            var weizhen_info = {
                'work_id':this.form.work_id,
                'circle_id':this.form.circle_id,
                'ax_x': this.form.ax_x,
                'ax_y': this.form.ax_y,
                'ax_z': this.form.ax_z,
                'wz_time': this.form.wz_time,
                'energy': this.form.energy,
                'level': this.form.level
            };
            console.log(typeof(weizhen_info['wz_time']));
            axios.post(path,weizhen_info)
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

        // 显示编辑微震信息的Dialog
        showWeizhenInfoDialog(work_id,circle_id,ax_x,ax_y,ax_z,wz_time,energy,level){
            this.dialogFormVisible2 = true;
            this.form2.work_id= work_id;
            this.old_work_id  = work_id;
            this.form2.circle_id = circle_id;
            this.old_circle_id = circle_id;
            this.form2.ax_x = ax_x;
            this.old_ax_x = ax_x;
            this.form2.ax_y = ax_y;
            this.old_ax_y = ax_y;
            this.form2.ax_z = ax_z;
            this.old_ax_z = ax_z;
            this.form2.wz_time = wz_time;
            this.old_wz_time = wz_time;
            console.log(wz_time);
            this.form2.energy = energy;
            this.old_energy = energy;
            this.form2.level = level;
            this.old_level = level;
            
        },
        editWeizhenInfo(work_id,circle_id,ax_x,ax_y,ax_z,wz_time,energy,level){
            var wz_data = {
                'old_work_id': this.old_work_id,
                'old_circle_id': this.old_circle_id,
                'old_ax_x': this.old_ax_x,
                'old_ax_y': this.old_ax_y,
                'old_ax_z': this.old_ax_z,
                'old_wz_time': this.old_wz_time,
                'old_energy': this.old_energy,
                'old_level': this.old_level,
                'new_work_id': Number(work_id),
                'new_circle_id': Number(circle_id),
                'new_ax_x': ax_x,
                'new_ax_y': ax_y,
                'new_ax_z': ax_z,
                'new_wz_time': wz_time,
                'new_energy': energy,
                'new_level': level,
                
            }
            console.log(wz_data);
            const path = 'http://localhost:5050/api/edit_weizhen_info';
            // 根据矿井的mine_id查询信息
            axios.post(path,wz_data)
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

        // 删除相应的信息
        deleteWeizhenInfo(work_id,circle_id,ax_x,ax_y,ax_z,wz_time,energy,level){
            this.$confirm('此操作将永久删除该条信息, 是否继续?', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning'
            }).then(() => {
                var mine_data = {
                    'work_id': work_id,
                    'circle_id': circle_id,
                    'ax_x': ax_x,
                    'ax_y': ax_y,
                    'ax_z': ax_z,
                    'wz_time': wz_time,
                    'energy': energy,
                    'level': level
                };
                const path = 'http://localhost:5050/api/delete_weizhen_info';
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

        handleSizeChange(val) {
            this.pageSize = val
            if(this.table_id == 1) {
                // 查询所有信息
                this.getMessage();
            }else if(this.table_id == 2) {
                // 根据用户的搜索查询信息
                this.inquireWeizhen();
            }
                
        },
        handleCurrentChange(val) {
            this.currentPage = val
            if(this.table_id == 1) {
                this.getMessage();
            }else if(this.table_id == 2) {
                this.inquireWeizhen();
            }
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