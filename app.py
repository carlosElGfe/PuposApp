from flask import Flask, redirect, url_for, render_template, Response,jsonify,current_app,render_template_string,request
from flask_cors import CORS, cross_origin 
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import os
import json
import io
from api_utils import *
import openpyxl

app = Flask(__name__)
CORS(app)
@app.route('/',methods=['GET', 'POST'])
@cross_origin()
def search():
    if request.method == 'GET':
        df = parse_excel('static/buffer.xlsx')
        #print(df.columns)
        data = get_count(df)
        return render_template(
            "base.html",data=data
            )
    elif request.method == 'POST':
        file = request.files['exc']
        file_path = os.path.join("static","buffer.xlsx")
        file.save(file_path)
        #print(df.columns)
        #data = get_count(df)
        #return render_template(
        #    "base.html",data=data
        #    )
        df = parse_excel('static/buffer.xlsx')
        #print(df.columns)
        data = get_count(df)
        return render_template(
            "base.html",data=data
            )


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")