import io

from dsanet.model import DSANet

def get_model(model_name):
    model = DSANet.load_from_metrics(
        (model_name),
        tags_csv=r'D:\\desktop\\kuangda-flask-api-master\\pytorch-flask-api-heroku-master\\data\\7_meta_tags.csv',
        on_gpu=[0])


    return model

# 'D:\\pycharmprojects\\Deploy\\kuangda-flask-api-master\\pytorch-flask-api-heroku-master\\data\\7_140.ckpt'
# def transform_image(image_bytes):
#
#     image = Image.open(io.BytesIO(image_bytes))
#     return
#
#
#
# def format_class_name(class_name):
#     class_name = class_name.replace('_', ' ')
#     class_name = class_name.title()
#     return class_name
