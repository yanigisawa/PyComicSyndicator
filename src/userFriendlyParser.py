from sgmllib import SGMLParser

class UserFriendlyParser(SGMLParser):
	def reset(self):
		SGMLParser.reset(self)
		self.img = ""
		self.comicFound = False
	def start_img(self, attrs):
		if self.comicFound:
			return
		for k, v in attrs:
			src = ""
			if k == "src":
				src = v
			if src.find("cartoons/archives") > -1:
				self.comicFound = True
				self.img = src
				
	def getImageLocation(self, html):
		self.feed(html)
		self.close()
		return self.img
		
