#!/usr/local/bin/python

import cgi;
import cgitb; cgitb.enable()

import comicSettings

from comicdb.models import *

def printHeaders():
	print "Content-Type: text/html" # HTML is following
	print # blank line, end of headers	

def main():
	printHeaders()
	print "<html><body><table border=1 cellpadding=2 cellspacing=2> \
		<thead><tr><td>Comic Name</td><td>Comic Url</td><td>Comic Rss</td></tr>"
	for comic in Comic.objects.filter(IsActive=True).order_by("Name"):
		print "<tr><td>%s</td><td><a href=\"%s\" target=\"_blank\">%s</td><td><a href=\"http://jamesralexander.com/comics/%s/\" \
			target=\"_blank\">%s</a></td></tr>" % \
			(comic.Name, comic.Url, comic.Url, comic.Name, comic.Name)
	
	print "</table></body></html"

main()
