from sgmllib import SGMLParser

class SluggyParser(SGMLParser):
	def reset(self):
		SGMLParser.reset(self)
		self.img = ""
		self.comicFound = False
	def start_img(self, attrs):
		src = ""
		if self.comicFound:
			return
		for k, v in attrs:
			if k == "src":
				src = v
			if src.find("images/comics/") > -1:
				self.comicFound = True
				self.img = src
				
	def getImageLocation(self, html):
		self.feed(html)
		self.close()
		return "http://www.sluggy.com" + self.img
		