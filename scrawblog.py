import re
from webScrawer import webScrawer
from scrapy.selector import Selector
from pysql import Pysql as ySql
db = ySql({ "host": "localhost", "user": "root", "password": "root", "db_name": "my_blog" })

def startWeb():
    webscraw = webScrawer(['https://www.cnblogs.com/yexiaochai/'])
    webscraw.startCrawUrl()
    moivecontent = Selector(text=str(webscraw.backResult[0]))
    title = moivecontent.css('#centercontent .postTitle')
    desc = moivecontent.css('#centercontent .c_b_p_desc')
    blog_title = []
    for single_title in title:
        blog_title.append({
          "title": single_title.css('a::text').extract_first()
        })
    flag = 0
    for single_desc in desc:
        blog_title[flag]['desc'] = single_desc.css("::text").extract_first()
        flag += 1
    for params in blog_title:
        sql = "INSERT INTO article(title, content) VALUES ('{title}', '{content}')".format(title=params["title"], content=params["desc"])
        db.insertData(sql)
        print('成功插入{}'.format(params['title']))

if __name__ == '__main__':
    startWeb()
