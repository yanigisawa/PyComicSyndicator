import mechanize, htmlFetch, datetime
from parsers import *
import time, urllib2
from django.conf import settings

import comicSettings

from comicdb.models import *

def getLatestComicLog(id):
	try:
		prevLog = ComicLog.objects.filter(ComicId=id).latest('FetchDate')
	except ComicLog.DoesNotExist:
		prevLog = None
	return prevLog

def getCurrentRss(id):
	try:
		prevRss = ComicRss.objects.filter(ComicLogId__ComicId=id).latest('ComicLogId__FetchDate')
	except ComicRss.DoesNotExist:
		prevRss = None
	return prevRss
	

def getHtml(comic):
	html = ""
	try:
		html = htmlFetch.GetHtml(comic.Url)
	except urllib2.HTTPError, e:
		print "    Unable to fetch html for Comic: \"%s\" - HTTPCode: %s" % (comic.Name, e.code)
		print "    URL: %s" % e.geturl()
	except urllib2.URLError, e:
		print "    Unable to fetch html for Comic: \"%s\" - UrlErrorReason: %s" % (comic.Name, e.reason)
		print "    URL: %s" % comic.Url
	return html

def fetchComicImageUrls():
	rssItems = []
	for comic in Comic.objects.filter(IsActive=1):
		time.sleep(1)
		parser = eval(comic.ParserConstructor)

		html = getHtml(comic)
		prevLog = getLatestComicLog(comic.id)

		foundUrlsToday = ComicLog.objects.filter(FetchDate__gte=datetime.datetime.utcnow().date(), 
				ComicId=comic.id).values('ImageUrl').distinct().count()

		log = ComicLog()
		log.ImageUrl = parser.getImageLocation(html)
		log.ComicId = comic
		log.FetchDate = datetime.datetime.utcnow()
		log.save()

		currentRss = getCurrentRss(comic.id)

		if (prevLog != None and prevLog.ImageUrl != log.ImageUrl and foundUrlsToday <= 1
				and log.ImageUrl != "") or currentRss == None:
			log = getLatestComicLog(comic.id)
			rss = ComicRss()
			rss.ComicLogId = log
			rss.save()


def main():
	fetchComicImageUrls()

main()
