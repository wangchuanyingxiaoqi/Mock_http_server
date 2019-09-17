#coding:utf-8

from flask  import Flask ,request
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello world"

@app.route('/send',methods=['GET','POST'])
def register():
    print(request.get_data())
    return 'welcome'

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080,debug=True)