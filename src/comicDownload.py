import goComicsParser, mechanize, htmlFetch, PyRSS2Gen, datetime
import comicsComParser, sluggyParser, cadParser, userFriendlyParser
import pennyArcadeParser, muttsParser
import datetime
import urllib2

class Comic:
	def __init__(self, name, url, parser):
		self.name = name
		self.url = url
		self.imageUrl = ""
		self.parser = parser

class ComicDownload:
	def __init__(self):
		today = datetime.date.today()
		ufDate = str(today.year) + str(today.month).zfill(2) + str(today.day).zfill(2)
		self.allComics = [Comic(name = "Pibgorn", url = "http://www.gocomics.com/pibgorn/", 
				parser = goComicsParser.GoComicsParser()),
			Comic(name = "Non Sequitur", url = "http://www.gocomics.com/nonsequitur/", 
				parser = goComicsParser.GoComicsParser()), 
			Comic(name = "For Better Or for Worse", url = "http://www.gocomics.com/forbetterorforworse/", 
				parser = goComicsParser.GoComicsParser()),
			Comic(name = "Garfield", url = "http://www.gocomics.com/garfield/", 
				parser = goComicsParser.GoComicsParser()), 
			Comic(name = "Fox Trot", url = "http://www.gocomics.com/foxtrot/", 
				parser = goComicsParser.GoComicsParser()),
			Comic(name = "Heart of the City", url = "http://www.gocomics.com/heartofthecity/", 
				parser = goComicsParser.GoComicsParser()),
			Comic(name = "Pearls before Swine", url = "http://www.comics.com/pearls_before_swine/", 
				parser = comicsComParser.ComicsComParser()),
			Comic(name = "Get Fuzzy", url = "http://www.comics.com/get_fuzzy/", 
				parser = comicsComParser.ComicsComParser()),
			Comic(name = "Luann", url = "http://www.comics.com/luann/", parser = comicsComParser.ComicsComParser()),
			Comic(name = "9 Chickweed Lane", url = "http://www.comics.com/9_chickweed_lane/", 
				parser = comicsComParser.ComicsComParser()),
			Comic(name = "Ctrl+Alt+Delete", url = "http://www.cad-comic.com/cad/", parser = cadParser.CadParser()),
			Comic(name = "Penny Arcade", url = "http://www.penny-arcade.com/comic/", 
				parser = pennyArcadeParser.PennyArcadeParser()),
			Comic(name = "Mutts",
                  url = "http://www.arcamax.com/mutts", parser = muttsParser.MuttsParser()),
			Comic(name = "The Barn", url = "http://www.comics.com/the_barn", 
				parser = comicsComParser.ComicsComParser())]
	
	def generateRSS(self):
		#self.fetchImageLocations()
		rssItems = []
		for comic in self.allComics:
			comic.parser.reset()

			try:
				html = htmlFetch.GetHtml(comic.url)
			except urllib2.HTTPError, e:
				print "    Unable to fetch html for Comic: \"%s\" - Status Code: %s" % (comic.name, e.code)
				print "    URL: %s" % e.geturl()
			except urllib2.URLError, e:
				print "    Unable to fetch html for Comic: \"%s\" - Status Code: %s" % (comic.name, e.code)
				print "    URL: %s" % e.geturl()

			comic.imageUrl = comic.parser.getImageLocation(html)
			desc = ("<a href=\"" + 
				comic.url + "\" target=\"_blank\">Comic Website</a><br/><br/><img src=\"" + comic.imageUrl + "\" />")
			rssItems.append(PyRSS2Gen.RSSItem(
				title = comic.name, 
				link = comic.imageUrl, 
				description = desc,
				pubDate = datetime.datetime.now()))

		rss = PyRSS2Gen.RSS2(
			title = "Comic RSS Feed", 
			link = "http://www.jamesralexander.com/comics/rss.xml",
			description = "Personalized feed of comics I Read", 
			items = rssItems)
		rss.write_xml(open("comicsRss.xml", "w"))
		return rss

def main():
	cd = ComicDownload()
	cd.generateRSS()

main()
