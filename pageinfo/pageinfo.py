import requests
import bs4


class PageInfo(object):
	"""
	PageInfo class to obtain and store title, description strings of the
	input web url. It also checks the page's keywords which can be used as tags when
	stored in 'bookmarks'.
	"""
	def __init__ (self, url , title, desc, keywords):
		self.url = url
		self.title = ""
		self.desc = ""
		self.keywords = ""

		try:
			resp = requests.get( url )
			#print( "Elso : status=", resp.status_code )
			theSoup = bs4.BeautifulSoup( resp.text, 'lxml')
			self.title = theSoup.title.text

			metatags = theSoup.find_all('meta', attrs={'name':'description'})
			if len(metatags) > 0:
				self.desc = metatags[0]['content']
			else:
				self.desc = desc
			#for tag in metatags:
			#	print( tag )
			metatags = theSoup.find_all('meta', attrs={'name':'keywords'})
			if len(metatags) > 0 :
				self.keywords = metatags[0]['content']

		except:
			print( "Failed loading page " + url )
			self.title = url
			self.desc = desc

