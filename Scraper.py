from artist import *
from album import *


# Purpose - get the user input for artist search or album search.
def getInput():
	# prompt user to know is searching by artist or album
	return input("Artist(0) or album(1)? Please enter the corresponding number.")

# Purpose - get the URL to begin search from
def getURL():
	return input("Enter URL to begin search from.")

#Purpose - get the keyword to search for
def getWord():
	return input("Enter the keyword to search for.")


# determine what action the user wants to take
val = -1
while( val == -1):
	try:
		val = int(getInput())
		if( val == 0 or val == 1):
			print "thank you"
		else:
			val = -1
	except ValueError:
		print "That's not an integer."
	except NameError:
		print "That's not an integer."


# output list will be used in either case, declare it outside the scope of if statements
output = []

# get parameters to search with
url = getURL()
word = getWord()

# in the case the user entered a 1, use the album obj helper to compute output
if val == 1:
	albumHelper = AlbumHelper()
	output = albumHelper.getSongs(url, word)
else:
	artistHelper = ArtistHelper()
	output = artistHelper.getSongs(url, word)

for link in output:
	print link
