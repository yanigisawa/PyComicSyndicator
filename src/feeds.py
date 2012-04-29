#!/usr/bin/python

import cgi;
import cgitb; cgitb.enable()
import os;

import comicSettings

from comicdb.models import *

def printHeaders():
    print "Content-Type: text/html" # HTML is following
    print # blank line, end of headers  
    print("<html><head><title>Comics</title>")
    print("""
        <style>
            tr.alt td{ background: #e6e6e6; }

        </style>

    """)
    print("<script src='http://code.jquery.com/jquery-latest.min.js' type='text/javascript'></script>")
    print("""
        <script type="text/javascript")>
            $(document).ready(function() {
                $(".stripeMe tr:even").addClass("alt");
            });
        </script>
    """)
    print("</head><body>")

def printFooter():
    print ("</table></body></html>")

def main():
    printHeaders()
    print ("""<table border=1 cellpadding=2 cellspacing=2 class="stripeMe"> 
        <thead><tr><th>Comic Name</th><th>Comic Url</th><th>Comic (last 10)</th>
        <th>Comic (All)</th></tr>""")
    for comic in Comic.objects.filter(IsActive=True).order_by("Name"):
        row = """<tr><td>{0}</td><td><a href=\"{1}\" target=\"_blank\">{1}</td>
            <td><a href=\"http://jamesralexander.com/comics/{0}/" target=\"_blank\">RSS</a>&nbsp;
            <a href=\"http://jamesralexander.com/comics/feed_html.py?name={0}" target=\"_blank\">HTML</a>
            <td>
                <a href="http://jamesralexander.com/comics/{0}/all" target="_blank">HTML</a>
            </td></tr>""".format (comic.Name, comic.Url)
        print(row)

    printFooter()

main()
