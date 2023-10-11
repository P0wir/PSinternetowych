import requests
import json
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


# 1
def check_url(url: str) -> bool:
    if 199 < requests.get(url).status_code < 300:
        return True
    else:
        return False


print(check_url(url='http://wmii.uwm.edu.pl/kadra'))

# 2

lista = []
lista2 = []
if check_url("https://www.meteoprog.pl/pl/weather/Olsztyn/"):
    response = requests.get("https://www.meteoprog.pl/pl/weather/Olsztyn/")
    soup = BeautifulSoup(response.content, 'html.parser')
    ul = soup.find("ul", class_="today-hourly-weather hide-scroll")
    for row in ul.find_all('span', class_="today-hourly-weather__temp"):
        lista.append(row.text)
    for row in ul.find_all('span', class_="today-hourly-weather__name"):
        lista2.append(row.text)

    temperatury = [int(temp.replace('+', '').replace('°', '')) for temp in lista]
    print(temperatury)

    hours = range(1, len(temperatury) + 1)

    plt.bar(lista2, temperatury)
    plt.ylabel('Temperatura (°C)')
    plt.title('temperatury')
    plt.show()

#3

url = f'https://api.gios.gov.pl/pjp-api/rest/data/getData/644'
response1 = requests.get(url)

if response1.status_code != 200:
  assert False

data = json.loads(response1.content.decode('utf-8'))
value = data['values'][2]
print(f'Czas: {value["date"]}, wartosc odczytu: {value["value"]}')
