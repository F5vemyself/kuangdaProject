import json
import os
from commons import get_model
import torch
# project_path =  "D://pycharmprojects//Deploy//pytorch-flask-api-heroku-master//"
curdir = os.path.dirname(os.path.abspath(__file__))
# json_path =os.path.join(curdir,"imagenet_class_index.json")
# imagenet_class_index = json.load(open(json_path))
model_path = os.path.join(curdir,"data")



#
# def get_prediction(image_bytes):
#     try:
#         tensor = transform_image(image_bytes=image_bytes)
#         outputs = model.forward(tensor)
#     except Exception:
#         return 0, 'error'
#     _, y_hat = outputs.max(1)
#     predicted_idx = str(y_hat.item())
#     return imagenet_class_index[predicted_idx]

# file_name = "7_140.ckpt"
# print(os.path.join(model_path,file_name))
# D:\pycharmprojects\Deploy\kuangda-flask-api-master\pytorch-flask-api-heroku-master\data\7_140.ckpt
def get_prediction(file_name,x):
    model = get_model(model_name=os.path.join(model_path,file_name))
    y_hat = model.forward(x)
    # print("%.4f" % (float(y_hat.data[0][0][0])))
    res = format(float(y_hat.data[0][0][0]), '.4f')
    return res
x = torch.rand((1, 64, 4), dtype=torch.float32)
# print(get_prediction(file_name=file_name,x=x))