import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/sport/football"

response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")

headlines = soup.find(name="ul", class_="ssrcss-sysfn1-Grid e12imr580").find_all(
    name="a"
)
with open("headlines.txt", "w") as file:
    for items in headlines:
        p_element = items.find(name="p")
        if p_element:
            headline = p_element.get_text()
            print(f"{headline}\n")
            file.write(f"{headline}\n")
