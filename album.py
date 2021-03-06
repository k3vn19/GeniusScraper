import requests
from BeautifulSoup import BeautifulSoup


class AlbumHelper:

	def __init__(self):
		print "Created AlbumHelper object." 

	def getSongs(self, url, word):
		output = []

		# get the html code from the given url
		# for this implementation make the url the link to a given album
		#url = 'https://genius.com/albums/Migos/Culture-ii'
		response = requests.get(url)
		html = response.content

		# make use of the BeautifulSoup library for scraping through html
		soup = BeautifulSoup(html)


		# this list will hold the links to all songs in the given album
		songLinks = []

		# from inspection of html I know links to songs are in div with class
		# 'chart_row-content', so find these div classes and extract the links in them
		data = soup.findAll('div', attrs={'class':'chart_row-content'})
		for div in data:
        		# get the link in the div class
        		links = div.findAll('a')
        		for a in links:
                		# save the link into a data structure
                		songLinks.append(a['href'])

		#keyword = "Patek"
		# now with all links to songs in the given album use BeautifulSoup
		# to search for keyword in each link.
		for link in songLinks:
		        responseF = requests.get(link)
		        htmlF = responseF.content

		        # this approach is confirmed to work but is slow
		        if word in htmlF:
		                output.append(link)
		return output
