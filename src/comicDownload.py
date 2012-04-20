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
    count = 0
    while html == "" and count < 4:
        time.sleep(0.5)
        try:
            html = htmlFetch.GetHtml(comic.Url)
        except urllib2.HTTPError, e:
            if count == 3:
                print "    Unable to fetch html for Comic: \"%s\" - HTTPCode: %s" % (comic.Name, e.code)
                print "    URL: %s" % e.geturl()
        except urllib2.URLError, e:
            if count == 3:
                print "    Unable to fetch html for Comic: \"%s\" - UrlErrorReason: %s" % (comic.Name, e.args)
                print "    URL: %s" % comic.Url
        except:
            if count == 3:
                print "    Unable to fetch html for Comic: \"%s\" - Unkown Exception: %s" % \
                    (comic.Name, sys.exc_info()[0])
        count = count + 1

    return html

def fetchComicImageUrls():
    comics = Comic.objects.filter(IsActive=1)
    for comic in comics:
        parser = eval(comic.ParserConstructor)

        html = getHtml(comic)

        if html == "":
            continue    

        prevLog = getLatestComicLog(comic.id)

        foundUrlsToday = ComicLog.objects.filter(FetchDate__gte=datetime.datetime.utcnow().date(), 
                ComicId=comic.id).values('ImageUrl').distinct().count()

        log = ComicLog()
        log.ImageUrl = parser.getImageLocation(html)
        log.ComicId = comic
        log.FetchDate = datetime.datetime.utcnow()
        if log.ImageUrl != "":
            log.save()
        else:
            print "Unable to find image for Comic - %s" % comic.Name
        
        parser.reset()

        currentRss = getCurrentRss(comic.id)

        if (prevLog != None and prevLog.ImageUrl != log.ImageUrl and foundUrlsToday <= 1
                and log.ImageUrl != "") or currentRss == None:
            log = getLatestComicLog(comic.id)
            rss = ComicRss()
            rss.ComicLogId = log
            rss.save()

def clearOldLogs():
    oldLogs = ComicLog.objects.all()
    for cl in oldLogs:
        rssItems = ComicRss.objects.filter(ComicLogId=cl.id)
        if rssItems.count() == 0:
            cl.delete()

    comics = Comic.objects.all()
    for c in comics:
        logList = ComicLog.objects.filter(ComicId=c.id)
        while logList.count() > 100:
            oldestLog = ComicLog.objects.filter(ComicId=c.id).order_by('FetchDate')
            for cl in oldestLog:
                rssItems = ComicRss.objects.filter(ComicLogId=cl.id)
                if rssItems.count() > 0:
                    for rss in rssItems:
                        rss.delete()
                cl.delete()
                break



def main():
    fetchComicImageUrls()
    clearOldLogs()

main()
