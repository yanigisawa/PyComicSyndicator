from sgmllib import SGMLParser

class CadParser(SGMLParser):
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
			if src.find("comics/") > -1:
				self.comicFound = True
				self.img = src
				
	def getImageLocation(self, html):
		self.feed(html)
		self.close()
		return self.img

class ComicsComParser(SGMLParser):
	def reset(self):
		SGMLParser.reset(self)
		self.img = ""
		self.comicFound = False
	def start_img(self, attrs):
		src = ""
		alt = ""
		if self.comicFound:
			return
		for k, v in attrs:
			if k == "src":
				src = v
			if src.find("cloudfiles") > -1 and src.find("full") > -1:
				self.comicFound = True
				self.img = src
				
	def getImageLocation(self, html):
		self.feed(html)
		self.close()
		return self.img

class GoComicsParser(SGMLParser):
	def reset(self):
		SGMLParser.reset(self)
		self.img = ""
		self.comicFound = False
	def start_img(self, attrs):
		src = ""
		alt = ""
		if self.comicFound:
			return
		for k, v in attrs:
			if k == "src":
				src = v
			if src.find("cdn.svcs") > -1:
				self.comicFound = True
				self.img = src
				
	def getImageLocation(self, html):
		self.feed(html)
		self.close()
		return self.img

class MuttsParser(SGMLParser):
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
			if src.find("newspics") > -1:
				self.comicFound = True
				self.img = src
				
	def getImageLocation(self, html):
		self.feed(html)
		self.close()
		return "http://www.arcamax.com/" + self.img
		
class PennyArcadeParser(SGMLParser):
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
			if src.find("photos") > -1:
				self.comicFound = True
				self.img = src
				
	def getImageLocation(self, html):
		self.feed(html)
		self.close()
		return self.img

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
