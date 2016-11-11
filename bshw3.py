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
import json
 
#using beautifulsoup to get the HTML of the webpage
base_url = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'
r = requests.get(base_url)
# gets the html
soup = BeautifulSoup(r.text)

for word in soup.find_all(class_="field field-name-body field-type-text-with-summary field-label-hidden"):
	if word == "students":
		word.text.replace("student", "AMAZING student")
	print(word)

# find the image
for image in soup.find_all("img"):
	if image.get('src') == "https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_192.jpg":
		image.replace(image.get('src'), "IMG_9268.JPG")





# lobbying is a dict
# with open("lobbying.json", "w") as writeJSON:
#     json.dump(lobbying, writeJSON)


