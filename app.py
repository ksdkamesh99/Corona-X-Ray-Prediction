from flask import Flask,render_template,request,send_file
import numpy as np

import cv2
import tensorflow
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
from skimage import transform
import webscraper as www 

app = Flask(__name__,static_folder='static',template_folder='templates')
model=load_model("model.h5")


def processesing(arr):
  for i in arr:
    if(i[0]>i[1]):
      return 0
    else:
      return 1
def images(img):
    image_read=[]
    image1=image.load_img(img)
    image2=image.img_to_array(image1)
    image3=transform.resize(image2,(200,200,3),anti_aliasing=True)
    image4=image3/255
    image_read.append(image4)
    img_array=np.asarray(image_read)
    return img_array

@app.route('/')
def home():
      lis=www.web()
      total=lis[0]
      cure=lis[1]
      death=lis[2]
      return render_template("index.html",total=total,cure=cure,death=death)
@app.route('/a.png')
def return_files_tut():
	try:
		return send_file('static/images/a.png', attachment_filename='a.png')
	except Exception as e:
		return str(e)
@app.route('/b.png')
def return_files():
	try:
		return send_file('static/images/b.png', attachment_filename='b.png')
	except Exception as e:
		return str(e)

@app.route('/xray',methods=['POST','GET'])
def xray():
      lis=www.web()
      total=lis[0]
      cure=lis[1]
      death=lis[2]
      if request.method=='POST':
        img=request.files['ima'].read()
        print(img)
        npimg = np.fromstring(img, np.uint8)
        # convert numpy array to image
        img = cv2.imdecode(npimg,cv2.IMREAD_COLOR)
        image3=cv2.resize(img,(200,200))
        image = np.expand_dims(image3, axis=0)
        imgarray=image/255
        print(imgarray)
        u=model.predict(imgarray)
        pre=processesing(u)
        if pre==1:
            print(0)
            return render_template("index.html",predict="You are confirmed as Covid positive",total=total,cure=cure,death=death)
        if pre==0:
            print(1)
            return render_template("index.html",predict="You are confirmed as Covid negetive",total=total,cure=cure,death=death)
      if request.method=='GET':
          return render_template("index.html",total=total,cure=cure,death=death)
      
if __name__=='__main__':
    app.run(host='0.0.0.0',debug=False)
