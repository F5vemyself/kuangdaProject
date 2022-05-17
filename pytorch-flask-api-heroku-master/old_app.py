import os
import json
from flask import Flask, render_template, request, redirect,url_for

from inference import get_prediction
# from commons import format_class_name
import torch
import numpy as np
import pandas as pd

app = Flask(__name__)

cur_path = os.path.abspath(os.path.dirname(__file__))


#
@app.route('/', methods=['GET', 'POST'])
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


@app.route('/?<string:file_name>')
def show_predict(file_name):
    # data = json.loads(request.form.get('data'))
    # file_name = data['model_name']
    x = torch.rand((1, 64, 4), dtype=torch.float32)
    res = get_prediction(file_name=file_name+'.ckpt',x=x)
    # res = 0.3473
    return render_template('result.html', result=res)

@app.route('/workface')
def show_workface():

    return render_template('workface.html')

@app.route('/bracket')
def show_bracket():

    return render_template('bracket.html')

# @app.route('/', methods=['GET', 'POST'])
# def upload_file():
#     # if request.method =='GET':
#     #
#     #     model_path = os.path.join(cur_path,"data/")
#     #     cnt = 0
#     #     model_name = []
#     #     for file in  os.listdir(model_path):
#     #         if file.split('.')[1]=="ckpt":
#     #             cnt+=1
#     #             model_name.append(file)
#
#
#     if request.method == 'POST':
#
#         #get是获取服务器的参数，post是更新服务器参数
#         # if 'file' not in request.files:
#         #     return redirect(request.url)
#         # file = request.files.get('file')
#         # if not file:
#         #     return
#         # img_bytes = file.read()
#         # class_id, class_name = get_prediction(image_bytes=img_bytes)
#         # class_name = format_class_name(class_name)
#         # return render_template('result.html', class_id=class_id,
#         #                        class_name=class_name)
#
#         x = torch.rand((1, 64, 4), dtype=torch.float32)
#         res = get_prediction(x)
#         return render_template('result.html', result=res)
#
#     return render_template('index.html')


@app.route('/pressure')
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