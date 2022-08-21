import requests
from bs4 import BeautifulSoup   # bs4 Package에서 beautifulSoup 모듈만 가져오도록 한다

url = 'https://movie.naver.com/movie/bi/mi/basic.naver?code=191597'
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')

title = soup.select_one('meta[property="og:title"]')['content']
image = soup.select_one('meta[property="og:image"]')['content']
desc = soup.select_one('meta[property="og:description"]')['content']