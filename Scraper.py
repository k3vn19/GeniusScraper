from artist import *
from album import *


# Purpose - get the user input for artist search or album search.
def getInput():
	# prompt user to know is searching by artist or album
	return input("Artist(0) or album(1)? Please enter the corresponding number.")

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

# in the case the user entered a 1, use the album obj helper to compute output
if val == 1:
	albumHelper = AlbumHelper()
	output = albumHelper.getSongs()
else:
	artistHelper = ArtistHelper()
	output = artistHelper.getSongs()

for link in output:
	print link
