import requests
import bs4


class PageInfo(object):
	"""
	PageInfo class to obtain and store title, description strings of the
	input web url. It also checks the page's keywords that can be used as tags when
	stored in 'bookmarks'.
	"""
	def __init__ (self, url, title=None, desc=None, keywords=None):
		self.url = url or ''
		self.title = title or ''
		self.desc = desc or ''
		self.keywords = keywords or ''

		try:
			if url is not None:
				resp = requests.get( url )
				theSoup = bs4.BeautifulSoup( resp.text, 'lxml')
				if theSoup.title.text != None and theSoup.title.text != '':
					self.title = theSoup.title.text

				metatags = theSoup.find_all('meta', attrs={'name':'description'})
				if len(metatags) > 0:
					self.desc = metatags[0]['content']
				else:
					self.desc = self.title
				#for tag in metatags:
				#	print( tag )
				metatags = theSoup.find_all('meta', attrs={'name':'keywords'})
				if len(metatags) > 0 :
					self.keywords = metatags[0]['content']
		except:
			print( "Failed loading page " + url )
			self.title = url or ''
