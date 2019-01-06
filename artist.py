import requests
from BeautifulSoup import BeautifulSoup
from album import *

class ArtistHelper:

	def __init__(self):
		print "Created ArtistHelper object."

	# Purpose - helper method to get list of links to albums made by a given artist
	# Param - url - link to page that contains all albums by a given artist
	def getAlbums(self, url):
		output = []
	
		# standard method of using BeautifulSoup class	
		response = requests.get(url)
		html = response.content
		soup = BeautifulSoup(html)

		# from inspection the album links are all in <a> with class = "album_link"
		data = soup.findAll('a', {'class':'album_link'})

		# fromat each href and add it to list of links
		for link in data:
			output.append("https://genius.com" + link['href'])
		return output

	# Purpose - this method will search all songs by a given artist to determine the list of
	# songs on which the keyword appears in
	# Param - url - the link to the artist page on Genius
	# Param - word - the keyword to search for
	def getSongs(self, url, word):
		output = []

		# first find the list of albums for the artist
		response = requests.get(url)
		html = response.content
		soup = BeautifulSoup(html)

		link = None
		# from inspection of artist page the link to page with all albums in div 
		# with class of 'u-quarter_top_margin. Retrieve the link in this div
		divs = soup.findAll('div', attrs={'class':'u-quarter_top_margin'})
		for div in divs:		
			links = div.findAll('a')
			for a in links:
				link = "https://genius.com" + a['href']
				print link
	
		# pass link to helper method to get the list of album links	
		albumLinks = self.getAlbums(link)

		# then pass each album url into the AlbumHelper object
		albumHelper = AlbumHelper()
		for link in albumLinks:
			output.extend(albumHelper.getSongs(link, word))	

		return output





