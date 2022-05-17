import pymysql
import pandas as pd
import numpy as np

class MysqlDb():

    def __init__(self, host, port, user, passwd, db):
        # 建立数据库连接
        self.conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            passwd=passwd,
            db=db
        )
        # 通过 cursor() 创建游标对象，并让查询结果以字典格式输出
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)


    def __del__(self): # 对象资源被释放时触发，在对象即将被删除时的最后操作
        # 关闭游标
        self.cur.close()
        # 关闭数据库连接
        self.conn.close()

    def select_db(self, sql, *args):
        """查询"""
        # 检查连接是否断开，如果断开就进行重连
        self.conn.ping(reconnect=True)
        # 使用 execute() 执行sql
        self.cur.execute(sql,*args)
        # 使用 fetchall() 获取查询结果
        data = self.cur.fetchall()
        # self.conn.commit()
        return data

    def execute_db(self, sql,*args):
        """更新/插入/删除"""
        try:
            # 使用 execute() 执行sql
            self.cur.execute(sql,*args)
            # 提交事务
            self.conn.commit()
        except Exception as e:
            print("操作出现错误：{}".format(e))
            # 回滚所有更改
            self.conn.rollback()
    def executemany_db(self, sql,values):
        """更新/插入/删除"""
        try:
            # 使用 execute() 执行sql
            self.cur.executemany(sql,values)
            # 提交事务
            self.conn.commit()
        except Exception as e:
            print("批量操作出现错误：{}".format(e))
            # 回滚所有更改
            self.conn.rollback()

if __name__ == '__main__':

    db = MysqlDb("127.0.0.1", 3306, "root", "123456", "new_kuangya")

    # select_sql = 'SELECT * FROM caiqu where caiqu_id=1'

    # update_sql = 'UPDATE caiqu SET caiqu_name = "铜锌矿" WHERE caiqu_id = 1'
    # insert_sql = 'INSERT INTO caiqu(caiqu_id, caiqu_name) VALUES(2, "山西大铜矿")'
    # delete_sql = 'DELETE FROM caiqu WHERE caiqu_id = 2'

    # data = db.select_db(select_sql)
    # print(data)
    # print(data[0]['caiqu_id'])
    # print(type(data[0]))
    # db.execute_db(update_sql)
    # db.execute_db(insert_sql)
    # # db.execute_db(delete_sql)
    # select_sql = 'SELECT caiqu_id FROM caiqu '
    # # bt_sql = 'SHOW FIELDS FROM caiqu'
    # content = db.select_db(select_sql)
    # bt_data = db.select_db(bt_sql)
    # labels = [l[0] for l in bt_data]
    # a , = content[0]
    # val , = content[0].values()
    # print(content[0]['caiqu_id'])
    # print(val)



    # select_sql1 = 'SELECT caiqu_id FROM caiqu'
    # content1 = db.select_db(select_sql1)
    # select_sql2 = 'SELECT caiqu_name FROM caiqu'
    # content2 = db.select_db(select_sql2)

    # 查询 search
    # 找出所有支架表
    # select_zj = 'SHOW TABLES '
    # all_table = db.select_db(select_zj)
    # zhijia = []
    # for tb in all_table:
    #     if tb['Tables_in_new_kuangya'].startswith("zhijia"):
    #         zhijia.append(tb['Tables_in_new_kuangya'])
    # print(zhijia)



    # 前端传回work_id
    work_id = 8222
    cexian_id = 140
    select_cexian = 'SELECT * FROM zhijia_static where work_id = %s  '
    data = db.select_db(select_cexian,(work_id))
    cexian = [d['cexian_id'] for d in data]
    # print(cexian)
    # print(tuple(cexian))
    tp = tuple(cexian)
    # print(tp[0])



    # res = [{"work_id": 1000, "wz_time": "2022-05-07 15:47:21", "wz_coordinate": "(1.0,1.0,1.0)", "energy": 23.0},
    #  {"work_id": 1000, "wz_time": "2022-04-13 15:47:43", "wz_coordinate": "(2.0,2.0,2.0)", "energy": 35.0},
    #  {"work_id": 1000, "wz_time": "2022-03-16 15:48:23", "wz_coordinate": "(5.0,5.0,5.0)", "energy": 32.0},
    #  {"work_id": 1001, "wz_time": "2022-03-15 15:49:18", "wz_coordinate": "(32.0,21.0,43.0)", "energy": 32.0},
    #  {"work_id": 1001, "wz_time": "2022-03-23 15:50:15", "wz_coordinate": "(32.0,32.0,32.0)", "energy": 21.0},
    #  {"work_id": 1001, "wz_time": "2022-02-17 15:50:45", "wz_coordinate": "(21.0,54.0,76.0)", "energy": 32.0},
    #  {"work_id": 2000, "wz_time": "2022-01-11 15:51:26", "wz_coordinate": "(21.0,54.0,32.0)", "energy": 76.0},
    #  {"work_id": 2001, "wz_time": "2021-07-14 15:51:47", "wz_coordinate": "(3.0,2.0,4.0)", "energy": 21.0}]
    sample = [{'cexian_id': 30, 'circle_id': 999, 'max_f': ('0.471666667')},
     {'cexian_id':40 , 'circle_id': 999, 'max_f': ('0.470000000')}]

    # 前端固定显示某个数字，插入时候如果有一项没有会返回为Null嘛？
    temp_data = []
    for tps in sample:
        tp = (tps['cexian_id'],tps['circle_id'],tps['max_f'])
        temp_data.append(tp)
    # print(temp_data)


    # "insert into productshoes (product_id, product_desc, color, price, product_name,quantity, createDate) values ('%s', '%s','%s','%d','%s','%d', '%s')" % (
    # p_id, p_desc, color, price, p_name, q, createDate)

    # format_strings = ','.join(['%s'] * len(cexian))
    # print(format_strings)
    # 查看最近得十条记录 前端需要横坐标是循环纵坐标是测线
    # 前端可用于显示多测线得数据
    select_maxf = 'SELECT cexian_id,circle_id,max_f FROM zhijia_dyn where cexian_id in {} ORDER BY circle_id DESC, cexian_id  LIMIT 14 '.format(tuple(cexian))
    data_max_f =db.select_db(select_maxf)
    # 目前这个结果是无序得，是否需要返回有序得结果给前端？
    print(data_max_f)

    # 用于插入记录way1，用户选择以天为单位插入（批量插入） 主要记录的是，入伏哦插入不全怎么办
    # 前端传回，形式最后变成元组
    # 参考 https://blog.csdn.net/jy1690229913/article/details/79407224
    insert_sql3 = 'INSERT INTO zhijia_dyn(cexian_id, circle_id,max_f) VALUES (%s,%s,%s)'
    db.executemany_db(insert_sql3,temp_data)
    # Way2 单挑记录的插入,用format格式会好一点
    t = (50,999,0.3333)
    insert_sql = 'INSERT INTO zhijia_dyn(cexian_id, circle_id,max_f) VALUES {}'.format(t)
    db.execute_db(insert_sql)
    # t1 = (60,999,0.33333)
    # insert_sql2 = 'INSERT INTO zhijia_dyn(cexian_id, circle_id,max_f) VALUES %s'
    # db.execute_db(insert_sql2,t1)

    # 同理更新和查询


    #### 收集数据给模型
    # 一般都要对orderby ，所以mysql中需要加入索引 where circle_id = 最新的 and cexian_id in {} (加了没作用)


    select_maxf = 'SELECT cexian_id,max_f FROM zhijia_dyn where cexian_id in {}  ORDER BY circle_id DESC, cexian_id LIMIT 140  '.format(tuple(cexian))
    data_max_f =db.select_db(select_maxf)
    print(data_max_f)
    # cexian_idl= []

    cexian_idl = [d['cexian_id'] for d in data_max_f]

    # [0.471666667, 0.47, 0.471666667, 0.255, 0.473333333, 0.471666667,
    max_fl = [float(d['max_f'] )for d in data_max_f]
    print(cexian_idl)
    print(max_fl)

    max_fl = np.reshape(max_fl, (-1, len(cexian)))
    print(max_fl)


    # 目前是可以将数据库的数据一下子捞到内存的，但是如果后续数据量大了？？一个窗口一个窗口的显示？？ 是否要加入数据库的索引










