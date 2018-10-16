# -*- coding: utf-8 -*-
from flask import Flask, jsonify, render_template
from pysql import Pysql as ySql
from webScrawer import webScrawer
import time
import re
# 起动服务器
app = Flask(__name__)
# 数据库
db = ySql({ "host": "localhost", "user": "root", "password": "root", "db_name": "myscraw" })


@app.route('/list')
def list():
   sql = "select * from video"
   result = db.selectData(sql)
   return render_template('list.html', result=result)
@app.route('/scraw')
def scraw():
    # print('resultresult', result)
    # finalResult = re.search('<div id\s=\s"main">(.*)</div>', result)
    # print('中要要要要', finalResult)
    # return str(finalResult.group(1))
    # # return str(webscraw.backResult)

if __name__ == '__main__':
   app.run(port=4646, debug=True)
