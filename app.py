from flask import Flask,render_template,request
from common import get_tensor
from inference import get_flower_name
import os

app =  Flask(__name__)
@app.route("/",methods = ['GET','POST'])
def hello():
    if request.method == 'GET':
        return render_template("index.html",value="hello")
    if request.method == 'POST':
        if 'file' not in request.files:
            return '<h3>File Not Uploaded</h3>'
        file = request.files['file']
        image = file.read()
        category = get_flower_name(image_bytes=image)
        return render_template('result.html',flower=category)
    
if __name__ == "__main__":
    app.run(debug=True,port=(os.getenv('PORT',5000)))