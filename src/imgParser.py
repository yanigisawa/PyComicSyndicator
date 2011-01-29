from sgmllib import SGMLParser

class ImageParser(SGMLParser):
	def reset(self):
		SGMLParser.reset(self)
		self.imgs = []
	def start_img(self, attrs):
		src = [v for k, v in attrs if k == "src"]
		if src:
			self.imgs.extend(src)



