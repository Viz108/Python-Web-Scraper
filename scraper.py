import requests
from bs4 import BeautifulSoup

#Open page
scraped_page = requests.get("https://myanimelist.net/anime/35838/Shoujo_Shuumatsu_Ryokou")
parsed_page = BeautifulSoup(scraped_page.text, "html.parser")

#Save parsed output to file
outputFile = open("output.txt", 'w', encoding="utf-8")
outputFile.write(parsed_page.prettify())

#Pull anime title
title = parsed_page.find('h1',class_="title-name").string

#Pull score
score = parsed_page.find('div', class_="score-label").string

#Pull synopsis
synopsis = parsed_page.find('p', itemprop="description").strings


#Output
print(title)
print("\n")
print(score)
print("\n")
for line in synopsis:
    print(line)