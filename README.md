# GeniusScraper
GeniusScraper is a web scraper to determine if an artist has used a word in any of their songs. Lyrics are retrieved from [Genius](https://genius.com) and the user can either search a specific album or check all albums by a given artist.

## Usage
### Getting Started
Download the files Scraper.py, artist.py and album.py and using the terminal navigate to the directory they are downloaded to. 

### Running Scraper.py
Run the following command in the terminal.
```
python Scraper.py
```

Next specify if search is to be done by artist or album by entering the integer 0 or 1, respectively. Once search type is determined specify the url to begin search from. If search is by artist enter the url of the artist page on [Genius](https://genius.com). If search is by album enter the url of the album page. In both cases add double quotes around the url. Finally, enter the keyword to search for surrounded by double quotes.

### Example Search by Artist
Suppose you want to determine if [Michael Jackson](https://genius.com/artists/Michael-jackson) has ever used the word "apple" in any of his songs. Begin by going to [Genius](https://genius.com) and search Michael Jackson to find his artist page. (You can click the hyperlink in his name above to see his artist page to see what this refers to.) Copy the url to the artist page. 

Run Scraper.py as described above. Enter  0 in the first prompt, no quotes. The next prompt is to enter the artist page url. Enter the following, with the double quotes:
```
"https://genius.com/artists/Michael-jackson"
```
The final prompt will ask for the keyword, enter the following with quotes:
```
"apple"
```

### Example Search by Album
Suppose you want to determine if the word "Patek" was ever said on the album [Culture II](https://genius.com/albums/Migos/Culture-ii) by Migos. Begin by going to [Genius](https://genius.com) and search for the album, it is hyperlinked above for this example. Copy the url to the album page. 

Run Scraper.py as described above. Enter 1 in the first prompt, no quotes. The next prompt is to enter the album page url. Enter the following, with the double quptes:
```
"https://genius.com/albums/Migos/Culture-ii"
```
The final prompt will ask for the keyword, enter the following with quotes:
```
"Patek"
```

## Limitations
### Strictness of Input
The biggest limitation in this project is that it only works if the correct urls are provided from [Genius](https://genius.com), at this time no other lyric websites are supported. 

### Runtime
This was developed and tested using a Raspberry Pi 3 and on average runtime on the device was about 1.5 seconds per song in both types of searches. The limitation is runtime is that it is dependent on runtime of the libraries used, mainly BeautifulSoup which handles the web scraping. This poor runtime could also be attributed to the hardware limitations of the RPi so it is possible that runtimes are faster on other Unix/Linux devices.
