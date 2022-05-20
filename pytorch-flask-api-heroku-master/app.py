import datetime
import decimal
import os
import json
from flask import Flask, render_template, request, redirect,url_for,jsonify

from inference import get_prediction
# from commons import format_class_name
import torch
import numpy as np
import pandas as pd
from mysqlintf import MysqlDb
# 跨域访问配置
from flask_cors import CORS
db = MysqlDb("127.0.0.1", 3306, "root", "123456", "new_kuangya")
app = Flask(__name__)
cur_path = os.path.abspath(os.path.dirname(__file__))

# CORS(app, resources={r'/*': {'origins': '*'}})
CORS(app, supports_credentials=True)

@app.route('/api/', methods=['GET', 'POST'])
def Showpage():
    if request.method == 'POST':

        # if 'file' not in request.files:
        #     return redirect(request.url)
        # file = request.files.get('file')
        # if not file:
        #     return
        # img_bytes = file.read()
        # class_id, class_name = get_prediction(image_bytes=img_bytes)
        # class_name = format_class_name(class_name)
        # return render_template('result.html', class_id=class_id,
        #                        class_name=class_name)
        # json_data = request.form.values()
        json_data = request.form.get('data')
        data = json.loads(json_data)
        file_name = data["model_name"]
        print(file_name)
        # json_data2 = request.get_data()
        # json_re = json.loads(json_data2)
        # print (json_re)
        # return 'json_re'
        x = torch.rand((1, 64, 4), dtype=torch.float32)
        res = get_prediction(file_name=file_name+'.ckpt', x=x)
        app.logger.info('%s failed to log in', json_data)
        return redirect(url_for('show_predict', file_name=file_name))  # 对应路由下函数的名字
        # return render_template('result.html', result=res)



        # data = json.loads(request.form.get('data'))
        # file_name = data['model_name']
        # file_name = request.form['model_name']


        # print(file_name)
        # app.logger.info('%s logged in successfully', file_name)
    #     file_name = "7_140.ckpt"
    #     x = torch.rand((1, 64, 4), dtype=torch.float32)
    #     res = get_prediction(file_name=file_name,x=x)
    #     # # res = 0.3473
    #     return redirect(url_for('show_predict', file_name=file_name)) # 对应路由下函数的名字
        # return render_template('result.html', result=res)
    else:
        return render_template('Model_nums.html')
#     file_name = '7_140.ckpt'
#     return redirect(url_for('show_predict', file_name=file_name)) # 对应路由下函数的名字

@app.route('/api/?<string:file_name>')
def show_predict(file_name):
    x = torch.rand((1, 64, 4), dtype=torch.float32)
    res = get_prediction(file_name=file_name+'.ckpt',x=x)
    return render_template('result.html', result=res)

@app.route('/api/mine_info', methods=['GET', 'POST'])
def showCaiqu():
    select_sql = 'SELECT * FROM mine'
    contents = db.select_db(select_sql)
    # print(contents)
    # 将一个Python数据类型列表进行json格式的编码
    mine_info_json = json.dumps(contents)
    # print(mine_info_json)
    return mine_info_json

@app.route('/api/inquire_mine', methods=['GET', 'POST'])
def showInquireMine():
    data = request.json
    name = data['searchName']
    value = data['searchValue']
    print(name,value)
    select_sql = " SELECT * FROM mine WHERE {} = '{}'".format(name,value)
    # 数据库返回得到的内容
    contents = db.select_db(select_sql)
    print(contents)
    mine_data_json = json.dumps(contents)
    return mine_data_json

@app.route('/api/insert_mine_info', methods=['GET', 'POST'])
def insertMineInfo():
    mine_data = request.json
    mine_id = str(mine_data['mine_id'])
    mine_name = str(mine_data['mine_name'])
    sql = 'INSERT INTO mine (mine_id,mine_name) values(%s ,%s)'
    # db.select_db(select_sql)
    db.cur.execute(sql,(mine_id,mine_name))
    db.conn.commit()
    return "插入信息成功"

@app.route('/api/delete_mine_info', methods=['GET', 'POST'])
def deleteMineInfo():
    mine_data = request.json
    mine_id = str(mine_data['mine_id'])
    sql = 'DELETE FROM mine WHERE mine_id = '+ mine_id
    db.execute_db(sql)
    return "删除信息成功!"

@app.route('/api/edit_mine_info', methods=['GET', 'POST'])
def editMineInfo():
    mine_data = request.json
    old_mine_id = int(mine_data['old_mine_id'])
    old_mine_name = str(mine_data['old_mine_name'])
    new_mine_id = int(mine_data['new_mine_id'])
    new_mine_name = str(mine_data['new_mine_name'])
    print(mine_data)
    sql = 'UPDATE mine SET mine_id = %s,mine_name = %s WHERE mine_id = %s AND mine_name = %s'
    db.cur.execute(sql,(new_mine_id,new_mine_name,old_mine_id,old_mine_name))
    db.conn.commit()
    return "修改信息成功!"

# 微震数据处理  写复杂了暂时不用了
def weizhenProcess2(contents,count):
    work_id = []
    wz_time = []
    wz_coordinate = []
    energy = []
    circle_id = []
    level = []

    # 拆分开来的x、y、z坐标
    ax_x = []
    ax_y = []
    ax_z = []
    # 用四个列表分别存储工作面id、微震时间、发生微震的坐标、微震能量
    for content in contents:
        work_id.append(content['work_id'])
        time = content['wz_time']

        # time.strftime函数是把datetime.dateime(year,month,day,hour,minute,second)转化为字符串类型
        # time.strftime函数是把datetime.datime(year,month,day,hour,minute,second)转化为字符串类型
        wz_time.append(time.strftime('%Y-%m-%d %H:%M:%S'))
        # 将x,y,z坐标拼接起来,得到(x,y,z)形式的数据
        ax_x.append(float(content['ax_x']))
        ax_y.append(float(content['ax_y']))
        ax_z.append(float(content['ax_z']))
        wz_xyz = '(' + str(content['ax_x']) + ',' + str(content['ax_y']) + ',' + str(content['ax_z']) + ')'
        wz_coordinate.append(wz_xyz)
        energy.append(float(content['energy']))
        circle_id.append(content['circle_id'])
        level.append(content['level'])

    weizhen_data = []
    for i in range(len(contents)):
        weizhen_dict = {}
        weizhen_dict['work_id'] = work_id[i]
        weizhen_dict['wz_time'] = wz_time[i]
        weizhen_dict['wz_coordinate'] = wz_coordinate[i]
        weizhen_dict['energy'] = float(energy[i])
        weizhen_dict['circle_id'] = circle_id[i]
        weizhen_dict['level'] = level[i]

        weizhen_dict['ax_x'] = ax_x[i]
        weizhen_dict['ax_y'] = ax_y[i]
        weizhen_dict['ax_z'] = ax_z[i]
        print(weizhen_dict)
        weizhen_data.append(weizhen_dict)
    weizhen_count = {'count':count}
    print(weizhen_count)
    weizhen_data.append(weizhen_count)
    weizhen_data_json = json.dumps(weizhen_data)
    return weizhen_data_json

# 微震数据处理 用这个
def weizhenProcess(contents,count):
    # timestamp1, timestamp2,
    # select_sql = "SELECT * FROM weizhen WHERE work_id = {} ".format(work_id)
    # select_sql = "SELECT * FROM weizhen WHERE work_id = {} AND " \
    #              "wz_time between '2020-10-16 02:00:00' and '2020-10-18 02:00:00'".format(work_id)
    # contents = db.select_db(select_sql)
    for content in contents:
        # 处理wz_time的格式
        time = content['wz_time']
        # datetime格式的数据转为字符串
        time = time.strftime('%Y-%m-%d %H:%M:%S')
        content['wz_time'] = time
        # 处理decimal数据的格式
        content['ax_x'] = float(content['ax_x'])
        content['ax_y'] = float(content['ax_y'])
        content['ax_z'] = float(content['ax_z'])
        content['energy'] = float(content['energy'])

        #在contents中增加一个xyz坐标信息
        wz_xyz = '(' + str(content['ax_x']) + ',' + str(content['ax_y']) + ',' + str(content['ax_z']) + ')'
        content['wz_coordinate'] = wz_xyz

    # 在数组最后增加一个记录条数count
    weizhen_count = {'count': count}
    contents.append(weizhen_count)

    # 将数据类型转换为json对象数组
    weizhen_data_json = json.dumps(contents)
    return weizhen_data_json


@app.route('/api/weizhen_info', methods=['GET', 'POST'])
def showWeizhen():
    data = request.json
    work_id = data['work_id']

@app.route('/api/weizhen_info', methods=['GET', 'POST'])
def showWeizhen():
    data = request.json
    page_num = data['page_num']
    page_size = data['page_size']
    limit1 = (page_num-1)*page_size
    limit2 = page_size
    sql = "SELECT count(*) FROM weizhen WHERE work_id = {} ".format(work_id)
    count_content = db.select_db(sql)
    count = count_content[0]['count(*)']
    select_sql = "SELECT * FROM weizhen WHERE work_id = {} LIMIT {},{}".format(work_id,limit1,limit2)

    # 数据库返回得到的内容
    contents = db.select_db(select_sql)
    # 对得到的数据进行处理，以json格式返回给前端
    weizhen_data_json = weizhenProcess(contents,count)
    return weizhen_data_json

@app.route('/api/inquire_weizhen', methods=['GET', 'POST'])
def showInquireWeizhen():
    data = request.json
    work_id = data['work_id']
    page_num = data['page_num']
    page_size = data['page_size']
    limit1 = (page_num - 1) * page_size
    limit2 = page_size
    name = str(data['searchName'])
    value = str(data['searchValue'])
    select_sql_all = "SELECT * FROM weizhen WHERE work_id = {} AND {} = {}".format(work_id,name,value)
    contents_all = db.select_db(select_sql_all)
    count = len(contents_all)
    select_sql = 'SELECT * FROM weizhen WHERE work_id = {} AND ' \
                 '{} = {} LIMIT {},{}'.format(work_id,name,value,limit1,limit2)

    # 数据库返回得到的内容
    contents = db.select_db(select_sql)
    # print(contents)
    # 对得到的数据进行处理，以json格式返回给前端
    weizhen_data_json = weizhenProcess(contents,count)
    print(weizhen_data_json)
    return weizhen_data_json


@app.route('/api/inquire_bytime_weizhen', methods=['GET', 'POST'])
def showInquireByTimeWeizhen():
    data = request.json
    page_num = data['page_num']
    page_size = data['page_size']
    work_id = data['work_id']
    limit1 = (page_num - 1) * page_size
    limit2 = page_size
    start_time = data['start_time']
    end_time = data['end_time']
    select_sql_all = "SELECT * FROM weizhen WHERE work_id = {} AND " \
                     "wz_time BETWEEN '{}' AND '{}'".format(work_id,start_time,end_time)
    contents_all = db.select_db(select_sql_all)
    count = len(contents_all)
    select_sql = "SELECT * FROM weizhen WHERE work_id = {} AND wz_time BETWEEN '{}' AND '{}'" \
                 "LIMIT {},{}".format(work_id,start_time,end_time,limit1,limit2)
    # 数据库返回得到的内容
    contents = db.select_db(select_sql)

    # 对得到的数据进行处理，以json格式返回给前端
    weizhen_data_json = weizhenProcess(contents,count)
    print(weizhen_data_json)
    return weizhen_data_json


@app.route('/api/insert_weizhen_info', methods=['GET', 'POST'])
def inserWeizhenInfo():
    data = request.json
    work_id = str(data['work_id'])
    circle_id = str(data['circle_id'])
    ax_x = str(data['ax_x'])
    ax_y = str(data['ax_y'])
    ax_z = str(data['ax_z'])
    wz_time = str(data['wz_time'])
    print(wz_time)
    print(type(wz_time))
    energy = str(data['energy'])
    level = str(data['level'])
    sql = 'INSERT INTO weizhen (work_id,circle_id,ax_x,ax_y,ax_z,wz_time,energy,level) values(%s,%s,%s,%s,%s,%s,%s,%s)'
    # db.select_db(select_sql)
    db.cur.execute(sql,(work_id,circle_id,ax_x,ax_y,ax_z,wz_time,energy,level))
    db.conn.commit()
    return "插入信息成功"

@app.route('/api/edit_weizhen_info', methods=['GET', 'POST'])
def editWeizhenInfo():
    data = request.json
    old_work_id = int(data['old_work_id'])
    old_circle_id = int(data['old_circle_id'])
    old_ax_x = float(data['old_ax_x'])
    old_ax_y = float(data['old_ax_y'])
    old_ax_z = float(data['old_ax_z'])
    old_wz_time = data['old_wz_time']
    old_energy = data['old_energy']
    old_level = data['old_level']
    new_work_id = int(data['new_work_id'])
    new_circle_id = int(data['new_circle_id'])
    new_ax_x = float(data['new_ax_x'])
    new_ax_y = float(data['new_ax_y'])
    new_ax_z = float(data['new_ax_z'])
    new_wz_time = str(data['new_wz_time'])
    new_energy = data['new_energy']
    new_level = data['new_level']
    sql = 'UPDATE weizhen SET work_id = %s,circle_id = %s,ax_x = %s,ax_y = %s,ax_z = %s,' \
          'wz_time = %s,energy = %s,level = %s WHERE work_id = %s AND circle_id = %s AND ' \
          'ax_x = %s AND ax_y = %s AND ax_z = %s AND wz_time = %s AND energy = %s AND level = %s'
    db.cur.execute(sql,(new_work_id,new_circle_id,new_ax_x,new_ax_y,new_ax_z,new_wz_time,new_energy,new_level,
                        old_work_id,old_circle_id,old_ax_x,old_ax_y,old_ax_z,old_wz_time,old_energy,old_level))
    db.conn.commit()
    return "修改信息成功!"

@app.route('/api/delete_weizhen_info', methods=['GET', 'POST'])
def deleteWeizhenInfo():
    data = request.json
    work_id = data['work_id']
    circle_id = data['circle_id']
    ax_x = float(data['ax_x'])
    ax_y = float(data['ax_y'])
    ax_z = float(data['ax_z'])
    wz_time = data['wz_time']
    energy = data['energy']
    level = data['level']
    sql = 'DELETE FROM weizhen WHERE work_id = %s AND circle_id = %s AND ' \
          'ax_x = %s AND ax_y = %s AND ax_z = %s AND wz_time = %s AND ' \
          'energy = %s AND level = %s'
    db.execute_db(sql,(work_id,circle_id,ax_x,ax_y,ax_z,wz_time,energy,level))
    return "删除信息成功!"

@app.route('/api/zhijia_info', methods=['GET', 'POST'])
def showZhijia():
    work_id = []
    cexian_id = []
    time = []
    circle_id = []
    init_f = []
    max_f = []
    weight_f = []

    select_sql = 'SELECT * FROM zhijia_dyn'
    # 数据库返回得到的内容
    contents = db.select_db(select_sql)
    # print(contents)

    # 用四个列表分别存储工作面id、微震时间、发生微震的坐标、微震能量
    for content in contents:
        work_id.append(content['work_id'])
        cexian_id.append(content['cexian_id'])
        # time.strftime函数是把datetime.datime(year,month,day)转化为字符串类型
        zhijia_time = content['time']
        time.append(zhijia_time.strftime('%Y-%m-%d'))
        circle_id.append(content['circle_id'])
        init_f.append(content['init_f'])
        max_f.append(content['max_f'])
        weight_f.append(content['weight_f'])

    zhijia_data = []
    for i in range(len(contents)):
        zhijia_dict = {}
        zhijia_dict['work_id'] = work_id[i]
        zhijia_dict['cexian_id'] = cexian_id[i]
        zhijia_dict['time'] = time[i]
        zhijia_dict['circle_id'] = circle_id[i]
        zhijia_dict['init_f'] = init_f[i]
        zhijia_dict['max_f'] = max_f[i]
        zhijia_dict['weight_f'] = weight_f[i]
        zhijia_data.append(zhijia_dict)
    zhijia_data_json = json.dumps(zhijia_data)
    return zhijia_data_json

# @app.route('/ShowWorkSpc/?<string:mine_id>')
@app.route('/api/ShowWorkSpc/',methods=['GET','POST'])
def ShowWorkSpc():
    data = request.json
    mine_id = str(data['mine_id'])

    # 采区id显示对应的工作面信息
    # id = "2"
    work_id = []
    work_name = []
    select_sql1 = 'SELECT work_id FROM workface WHERE mine_id =  '+mine_id
    content1 = db.select_db(select_sql1)
    print(content1)

    for i in range(len(content1)):
        # print(content1[i])
        work_id.append(content1[i]['work_id'])
    select_sql2 = 'SELECT work_name FROM workface WHERE mine_id =  ' + mine_id
    content2 = db.select_db(select_sql2)
    for i in range(len(content2)):
        work_name.append(content2[i]['work_name'])
    work_data = []
    for i in range(len(work_id)):
        # work_dict一定要放在for循环里面
        work_dict = {}
        work_dict['work_id'] = work_id[i]
        work_dict['work_name'] = work_name[i]
        work_data.append(work_dict)
    mine_data_json = json.dumps(work_data)
    return mine_data_json
    # print(workspc)
    # return "hello"
    # return  render_template('WorkSpc.html',data = zip(work_id,work_name))


@app.route('/api/pressure')
def show_pressure():
    data = pd.read_csv("./data/pressure1.csv")
    column_headers = list(data.columns.values.tolist())
    # time = data['t'].values.tolist()  # 展示数量1
    # print(time)
    xaxis = [i for i in range(0, 5)]  # 横坐标
    zj = []
    for i in range(0, 14):
        zj.append(data[column_headers[i + 1]].values.tolist())

    # 把数据传入HTML文件里面
    return render_template('hello_world.html',xaxis=xaxis,zj0=zj[0][:5],zj1=zj[1][:5],zj = zj)
    # return render_template('kuangya.html')




if __name__ == '__main__':

    app.run(debug=True, port=int(os.environ.get('PORT', 5050)))

    # app.run(debug=True)
    # data = pd.read_csv("./data/pressure1.csv")
    # column_headers = list(data.columns.values.tolist())
    # time = data['t'].values.tolist()  # 展示数量1
    # print(time)
    # xaxis = [i for i in range(0, 5)]  # 横坐标
    # zj = []
    # for i in range(0, 14):
    #     zj.append(data[column_headers[i + 1]].values.tolist())
    # print(xaxis)
    # print(zj[0][:5])
    # print(zj[1][:5])