import mechanize
def GetHtml(url):
	opener = mechanize.build_opener()
	opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8")]
	mechanize.install_opener(opener)
	#print "URL, from Fetcher: " + url
	request = mechanize.urlopen(url)
	html = request.read()
	request.close()
	return html
