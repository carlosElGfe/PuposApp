from flask import Flask, redirect, url_for, render_template, Response,jsonify,current_app,render_template_string
from flask_cors import CORS, cross_origin 
import json
import io
from api_utils import *


app = Flask(__name__)
CORS(app)
@app.route('/',methods=['GET', 'OPTIONS'])
@cross_origin()
def search():
    df = parse_excel('buffer.xlsx')
    #print(df.columns)
    data = get_count(df)
    return render_template(
        "base.html",data=data
        )



if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")