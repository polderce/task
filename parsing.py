import requests
from bs4 import BeautifulSoup as bs4

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
}

url = 'https://itproger.com/'
session = requests.Session()

try:
    req = session.get(url, headers=headers)
    if req.status_code == 200:
        soup = bs4(req.content, "html.parser")
        divs = soup.find_all('div', attrs={'class': 'course'})
        for div in divs:
            title = div.find('span', attrs={'class': 'title_course'}).text
            href = div.find('a')['href']
            print('{} - https://itproger.com/{}'.format(title, href))
    else:
        print('Error')
except Exception:
    print('Ошибка в самом URL адресе')
