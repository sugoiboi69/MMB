import requests
from bs4 import BeautifulSoup

link = "https://www.google.com/searchbyimage?&image_url=https://cdn.discordapp.com/attachments/425662853958336513/426320431151317015/800px-Masjid_Angullia_Sep_06.JPG"

html = requests.get(link).text

#If you do not want to use requests then you can use the following code below with urllib (the snippet above). It should not cause any issue.
soup = BeautifulSoup(html, "lxml")
res = soup.findAll("article", {"class": "listingItem"})
for r in res:
    print("Company Name: " + r.find('a').text)
    print("Address: " + r.find("div", {'class': 'address'}).text)
    print("Website: " + r.find_all("div", {'class': 'pageMeta-item'})[3].text)