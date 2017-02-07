


#from bs4 import BeautifulSoup
import requests


class Seri:
	def __init__(self):
		pass

class Spider:
	def __init__(self,cfgCrawler = None):
		self.cfgCrawler = cfgCrawler
		self.text = None
		pass

	def init(self,cfgCrawler):
		## http proxy info 
		##a
		pass 

	def crawl( url, params):
		r = requests.post(url)
		self.text = r.text
		



def test():


	spider = Spider()
	spider.crawl("http://movie.douban.com")

	print(spider.text)





def main():
	test()


	