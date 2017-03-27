#_*_ coding:utf-8 _*_  

#文件说明:熟悉并使用BeautifulSoup
#作者:高小调
#时间:2017-03-2

import urllib
from bs4 import BeautifulSoup
def downloader(url):
	page = urllib.urlopen(url)
	return page.read()

#获取上下页链接(存在重复)
def getPageLink(url):
	html = downloader(url)
	soup = BeautifulSoup(html)
	pagebar = soup.find_all("div")[3]
	a = pagebar.find_all("a")
	links = []
	for link in a:
		links.append(link["href"])
	return links
	
#获取文章列表链接
def getListLink(url):
	html = downloader(url)
	soup = BeautifulSoup(html)
	content = soup.find("div",id="content")
	article = content.find_all("article")
	for element in article:
		article_link = element.h2.find_all("a")[1]
		article_href = article_link["href"]
		article_title = article_link.get_text();
		print article_href + "------" + article_title	

#获取所有文章链接
def getAllLink(url):
	getListLink(url)				#输出首页文章列表
	page_links = getPageLink(url)	#开始分页
	for page_link in page_links:
		getListLink(page_link)
getAllLink("http://blog.gaoxiaodiao.com")