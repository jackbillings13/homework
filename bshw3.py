# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.
import requests
from bs4 import BeautifulSoup
 
#using beautifulsoup to get the HTML of the webpage
base_url = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'
r = requests.get(base_url)
# gets the html
soup = BeautifulSoup(r.text)

# finds the main image and replaces it with an image of me
for image in soup.find_all('img'):
	if image.get('src') == "https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_192.jpg":
		image['src'] = "https://scontent.fdtw1-1.fna.fbcdn.net/v/t1.0-9/12400597_1066873783363371_1187860790019637795_n.jpg?oh=b9fd085a8d7a10ffcdb0dd9ac6587d8e&oe=5891A54C"

# finds all local images and replaces it with the media image
for image2 in soup.find_all('img'):
	if image2.get('src')[:5] != "https":
		image2['src'] = "media/logo.png"


pretty = soup.prettify()
# creates the html page
filename = open("homework3.html", "w")

# replaces any occurence of student with AMAZING student
pretty = pretty.replace("student", "AMAZING student")

# writes the html page
filename.write(pretty)
filename.close()



