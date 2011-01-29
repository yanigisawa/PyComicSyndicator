#This file represents the basic framework used for parsing the HTML to
#return the src of the img tag used on the comic website. This file is
#not actually included in any of the other scripts

from sgmllib import SGMLParser

class ImageParser(SGMLParser):
	def reset(self):
		SGMLParser.reset(self)
		self.imgs = []
	def start_img(self, attrs):
		src = [v for k, v in attrs if k == "src"]
		if src:
			self.imgs.extend(src)
