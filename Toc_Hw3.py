#-*-coding:utf-8-*-
#學號:f74002133 ， 姓名:鐘曼芸
import urllib2
import json
import sys

if sys.getdefaultencoding() != 'utf-8':
	reload(sys)
	sys.setdefaultencoding('utf-8')

sourceURL = urllib2.urlopen(sys.argv[1])
data = json.load(sourceURL)

total_price = 0
total_num = 0
avg_price = 0
for i in range(len(data)):
	if data[i][u"鄉鎮市區"] == sys.argv[2]:
		if sys.argv[3] in data[i][u"土地區段位置或建物區門牌"]:
			if int(sys.argv[4]) <= (data[i][u"交易年月"] // 100):
				total_price += data[i][u"總價元"]
				total_num += 1
avg_price = total_price / total_num
print avg_price

