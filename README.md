This is a collection of scripts that will scrape popular web comic sites and will combine the links to the
comic image into a single xml file that can be put into an RSS Reader like google reader.

##REQUIREMENTS:

There are two python libraries required to run this script. One
that is used to help with parsing the html, and one that generates
the rss xml.

##HTML Parsing: 

Mechanize: http://wwwsearch.sourceforge.net/mechanize/
To include in this script, either run the python setup.p install script
or just manually add the mechanize/ directory in the src/ directory
below so that it can be included automatically by Python

##RSS Xml generation: 

PyRSS2Gen: http://www.dalkescientific.com/Python/PyRSS2Gen.html
This is a single python file that again be inclued via the setup.py script,
or just manually copy the file into the src directory to be included by Python

##COMPOSITES

There are two composite parts to the comic syndicator

1. A scheduled task that fetches the URL of the comic for that day (the comicDownload.py script)
2. A generated RSS feed that can be subscribed to by a syndication reader, like Google Reader. All the feeds are viewable from the feeds.py page

