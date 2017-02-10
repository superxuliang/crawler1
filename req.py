

from xlutils import *
from bs4 import BeautifulSoup
import requests
import sys


class Seri:
	def __init__(self):
		pass

class Spider:
	def __init__(self,cfgCrawler = None):
		self.cfgCrawler = cfgCrawler
		self.text = None
		self.url = None
		self.encoding = None
		self.r = None
		pass

	def init(self,cfgCrawler):
		## http proxy info 
		##a
		pass 

	def crawl(self, url, params = None):
		log("url:")
		log(url)

		self.r = requests.get(url)

		self.text = self.r.text
		self.url = self.r.url
		self.encoding = self.r.encoding

	def json():
		return (self.r.json())

	def getChildPages():
		pass


def test(argv):


	spider = Spider()
	spider.crawl(argv[1])
	#print(spider)
	log("=========")
	log(spider.text)

	f = open(argv[2],"w")

	f.write(spider.text.encode("utf-8"))
	f.close()


def test1(argv):
	bs = BeautifulSoup("\n".join(open("a.txt").readlines()), "lxml")
	links = bs.find_all(attrs={"href":re.compile("subject")})
	##>>> type(links[0])
	##<class 'bs4.element.Tag'>
	#links[1].attrs["href"]


def main(argv):
	print(argv)
	test(argv)


main(sys.argv)


