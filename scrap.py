from bs4 import BeautifulSoup
import requests
import json

url = "https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=1"
response = requests.get(url)
content = response.content
soup = BeautifulSoup(content , 'html.parser')
titles = soup.find_all("a", class_="catalog-item-name")
titlelst = []
for title in titles:
    titlelst.append(title.get_text())
prices = soup.find_all("span", class_="price")
pricelst = []
for price in prices:
    value = price.get_text()
    pricelst.append(float(value[1:len(value)]))
status = soup.find_all("span", class_="status")
statuslst = []
for stat in status:
    value = stat.get_text()
    if value == "Out of Stock":
        statuslst.append(False)
    else:
        statuslst.append(True)

manufacturers = soup.find_all("a", class_="catalog-item-brand")
manufacturerlst =[]
for manufacturer in manufacturers:
    manufacturerlst.append(manufacturer.get_text())

output = []
for i in range(len(titlelst)):
    optdict = {
        "price" : pricelst[i],
        "title" : titlelst[i],
        "stock" : statuslst[i],
        "manufacturer" : manufacturerlst[i]
    }
    output.append(optdict)
print(json.dumps(output))