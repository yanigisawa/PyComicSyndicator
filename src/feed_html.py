#!/usr/bin/python

from PyRSS2Gen import RSS2, RSSItem
import cgi;
import cgitb; cgitb.enable()
from dateutil import zoneinfo

import comicSettings

from comicdb.models import *

def PrintHeaders(comicName):
    print "Content-Type: text/html" # HTML is following
    print # blank line, end of headers
    print ("<html><head><title>%s</title>" % comicName)
    print ("""
        <style>
        ul { margin: 0; padding: 0;}
        ul li { list-style: none; }

        </style>

    """)
    print ("</head><body><h1>%s</h1>" % (comicName))

def PrintFooter():
    print("</body></html>")

def main():
    form = cgi.FieldStorage()
    comicName = form.getvalue("name")
    PrintHeaders(comicName)
    rssItems = []
    rssTitle = ""

    print ("<ul>")
    desc = ""
    for rss in ComicRss.objects.filter(ComicLogId__ComicId__Name=comicName).order_by("-ComicLogId__FetchDate")[:10]:
        rssTitle = rss.ComicLogId.ComicId.Name
        utc_zone = zoneinfo.gettz('UTC')
        est_zone = zoneinfo.gettz('US/Eastern')
        utc_date = rss.ComicLogId.FetchDate.replace(tzinfo=utc_zone)
        est_date = utc_date.astimezone(est_zone)

        
        desc += """
            <li>
             <a href=\"{0}\" target=\"_blank\">Comic Website</a><br/> Publish Date: {1}<br/><img src=\"{2}\"/>
            </li>""".format(rss.ComicLogId.ComicId.Url, est_date, rss.ComicLogId.ImageUrl)

    c = Comic.objects.get(Name=comicName)
    print("%s</ul>" % desc)
    PrintFooter()


main()

