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
import re
 
#using beautifulsoup to get the HTML of the webpage
base_url = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'
r = requests.get(base_url)
# gets the html
soup = BeautifulSoup(r.text)

word = soup.find_all(string=re.compile("student"))
print(word)




# word = soup.body.find_all(text="students")
# print(word)

# for word in soup.find_all(class_="html not-front logged-in two-sidebars page-node page-node- page-node-11581 node-type-general-page section-programs"):
# 	if word == "students":
# 		print("STUDENT")
# 		word.p.text.replace("students", "AMAZING student")

# for word in soup.find_all(class_="field field-name-body field-type-text-with-summary field-label-hidden"):
# 	print(word)

# find the image
for image in soup.find_all('img'):
	if image.get('src') == "https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_192.jpg":
		image.replace_with("IMG_9268.JPG")


for image2 in soup.find_all('img'):
	if image2.get('src')[:5] != "https":
		image2.replace_with("logo.png")


print(soup.prettify())


# lobbying is a dict
# with open("lobbying.json", "w") as writeJSON:
#     json.dump(lobbying, writeJSON)


