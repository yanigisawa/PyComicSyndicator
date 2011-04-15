#!/usr/local/bin/python

from PyRSS2Gen import RSS2, RSSItem
import cgi;
import cgitb; cgitb.enable()
from dateutil import zoneinfo

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

	for rss in ComicRss.objects.filter(ComicLogId__ComicId__Name=comicName).order_by("-ComicLogId__FetchDate")[:10]:
		rssTitle = rss.ComicLogId.ComicId.Name
		utc_zone = zoneinfo.gettz('UTC')
		est_zone = zoneinfo.gettz('US/Eastern')
		utc_date = rss.ComicLogId.FetchDate.replace(tzinfo=utc_zone)
		est_date = utc_date.astimezone(est_zone)

		desc = "<a href=\"%s\" target=\"_blank\">Comic Website</a><br/> Publish Date: %s<br/><img src=\"%s\"/>" % \
			(rss.ComicLogId.ComicId.Url, est_date, rss.ComicLogId.ImageUrl)
		rssItems.append(RSSItem(title = rss.ComicLogId.ComicId.Name,
						link = rss.ComicLogId.ImageUrl,
						description = desc,
						pubDate = utc_date))

	c = Comic.objects.get(Name=comicName)
	rss = RSS2(
			title = rssTitle,
			link = c.Url,
			description = "%s image feed" % rssTitle, items = rssItems)
	print rss.to_xml()

main()

