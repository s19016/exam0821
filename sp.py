import requests
from bs4 import BeautifulSoup

req = requests.get("https://bleach-bravesouls.gamerch.com/%E5%85%A8%E3%82%AD%E3%83%A3%E3%83%A9%E5%BC%B7%E3%81%95%E3%83%A9%E3%83%B3%E3%82%AD%E3%83%B3%E3%82%B0")
bs = BeautifulSoup(req.text, 'html.parser')

file = open('text.text', 'w')

for i in bs.select("h3"):
    file.write(i.getText() + '\n')

file.close()
