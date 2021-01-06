from flask import Flask, redirect, url_for, render_template, Response,jsonify,current_app,render_template_string, request
from flask_cors import CORS, cross_origin 
import json
import io
from api_utils import *
import os

app = Flask(__name__)
CORS(app)
@app.route('/',methods=['GET', 'POST'])
@cross_origin()
def search():
    if request.method == 'GET':
        df = parse_excel('buffer.xlsx')
        #print(df.columns)
        data = get_count(df)
        return render_template(
            "base.html",data=data
            )
    elif request.method == 'POST':
        file = request.files.get('file').read()
        print(type(file))
        print(file)
        #data = get_count(df)
        if file and allowed_file(file.filename):
            df = parse_excel('buffer.xlsx')
            #print(df.columns)
            data = get_count(df)
            return render_template(
                "base.html",data=data
                )
    return "Hello Wolrd"

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")