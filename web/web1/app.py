from flask import Flask,url_for,render_template
from markupsafe import escape
import random
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    name = "AraRen"
    dataFrame = get_dataFrame()
    return render_template('index.html',name=name,dataFrame=dataFrame)

def get_dataFrame()->pd.DataFrame:
    data = [['AraRen',87,87,87],
            ['AAAAAA',78,78,78],
            ['BBBBBB',87,78,87]]

    return pd.DataFrame(data,columns=["姓名","國文","英文","數學"])