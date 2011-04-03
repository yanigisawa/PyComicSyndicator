#!/usr/local/bin/python

from PyRSS2Gen import RSS2, RSSItem
import cgi;
import cgitb; cgitb.enable()

import comicSettings

from comicdb.models import *

def PrintHeaders():
	print "Content-Type: text/html" # HTML is following
	print # blank line, end of headers

def main():
	PrintHeaders()
	form = cgi.FieldStorage()
	comicName = form.getvalue("name")
	rssItems = []
	rssTitle = ""

	for rss in ComicRss.objects.filter(ComicLogId__ComicId__Name=comicName)[:10]:
		rssTitle = rss.ComicLogId.ComicId.Name
		desc = "<a href=\"%s\" target=\"_blank\">Comic Website</a><br/> Publish Date: %s<br/><img src=\"%s\"/>" % \
			(rss.ComicLogId.ComicId.Url, rss.ComicLogId.FetchDate, rss.ComicLogId.ImageUrl)
		rssItems.append(RSSItem(title = rss.ComicLogId.ComicId.Name,
						link = rss.ComicLogId.ImageUrl,
						description = desc,
						pubDate = rss.ComicLogId.FetchDate))

	rss = RSS2(
			title = rssTitle,
			link = "http://www.jamesralexander.com/comics/%s/" % (comicName),
			description = "%s image feed" % rssTitle, items = rssItems)
	print rss.to_xml()

main()

