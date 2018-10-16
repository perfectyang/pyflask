import re
from webScrawer import webScrawer
webscraw = webScrawer(['http://www.hao6v.com/'], {
  'encoding': 'gbk'
})
webscraw.startCrawUrl()
moivecontent = str(webscraw.backResult[0])
result = re.search(r'<div id\s*=\s*"main">(.*)</div>', moivecontent, re.S)
allLi = re.search(r'<li (.*?)>(.*)</li>', result.group(1), re.S)
print('allLiallLi', allLi.group())
