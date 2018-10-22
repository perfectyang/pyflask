import re
from webScrawer import webScrawer
from scrapy.selector import Selector
webscraw = webScrawer(['https://www.cnblogs.com/yexiaochai/'])
webscraw.startCrawUrl()
moivecontent = Selector(text=str(webscraw.backResult[0]))
# result = re.search(r'<div id\s*=\s*"centercontent">(.*)</div>', moivecontent, re.S)
# allLi = re.search(r'<li (.*?)>(.*)</li>', result.group(1), re.S)

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
print('blog_titleblog_title', blog_title)
