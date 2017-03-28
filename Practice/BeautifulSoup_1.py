#encoding='utf-8' 
#_*_ coding:utf-8 _*_  

#文件说明:熟悉并使用BeautifulSoup之抓取糗事百科
#作者:高小调
#时间:2017-03-29
import urllib2
from bs4 import BeautifulSoup
from bs4 import UnicodeDammit

#获取列表段子内容
def getListText(url):
	#直接访问糗事百科不行,需要加一个header
	header = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',}
	request = urllib2.Request(url,headers = header)
	response = urllib2.urlopen(request)  
	soup = BeautifulSoup(response.read())
	content = soup.find_all(attrs={"class":"content"})
	count = 1;
	#fp = open("F:\\Github\\Python\\test.txt","a+")
	for subcontent in content:
		ret = str(count) + "." + subcontent.get_text()
		print ret
		#fp.write(ret.encode("utf-8"))
		count = count+1
	#fp.close()

url = "http://www.qiushibaike.com/"
getListText(url)
#print "已写入文件test.txt"