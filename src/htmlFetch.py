import mechanize

def GetHtml(url):
	opener = mechanize.build_opener()
	opener.addheaders = [("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0) Gecko/20100101 Firefox/4.0")]
	mechanize.install_opener(opener)
	request = mechanize.urlopen(url)
	html = request.read()
	request.close()
	return html
