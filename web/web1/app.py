from flask import Flask,url_for,render_template
import pandas as pd
from auth import auth
from bs import bootstrap


app = Flask(__name__)
app.register_blueprint(auth.bp)
app.register_blueprint(bootstrap.bp)

@app.route('/')
def index():
    name = "REN"
    dataFrame = get_dataFrame()
    return render_template('index.html',name=name,dataFrame=dataFrame)

def get_dataFrame()->pd.DataFrame:
    data = [['REN',67,92,85],
            ['Jacky Chen',78,97,65],
            ['Monica Chen',92, 79, 85]]
    return pd.DataFrame(data,columns=["姓名","國文","英文","數學"])

@app.route('/aaa')
def aaa():
    return render_template('aaa.html')  
