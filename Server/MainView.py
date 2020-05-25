from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

res = req.urlopen("https://weather.naver.com/")

soup = BeautifulSoup(res,'html.parser')
tmp = soup.find(class_='m_zone2')
print(tmp)
