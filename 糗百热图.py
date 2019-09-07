import time

import requests
from bs4 import BeautifulSoup


url = 'https://www.qiushibaike.com/imgrank/'
ua = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
cookie = '_ga=GA1.2.603963355.1566200239; __cur_art_index=6800; _qqq_uuid_="2|1:0|10:1566346090|10:_qqq_uuid_|56:MTU0YjdkZWY0MDUzMzg5OWNlZmNlNThlM2FiZjMxNDM3ZjQ3MDFiNQ==|74e5ea9cdd3f30308cd4d3698e8dc89782df511187f932d4e8919b10c7088cab"; _xsrf=2|1e3c0d34|9dc0b5bfea4f95acd0cbd610d85fddbb|1567843641; Hm_lvt_2670efbdd59c7e3ed3749b458cafaa37=1566200238,1566346050,1567843597; _gid=GA1.2.1202080677.1567843597; Hm_lpvt_2670efbdd59c7e3ed3749b458cafaa37=1567843698'
headers ={
	'User-Agent':ua,
	'Cookie':cookie,
	'Connection':'keep-alive',
	'Referer':'https://www.qiushibaike.com/imgrank/'

}
req =requests.get(url,headers= headers)
soup =  BeautifulSoup(req.text,'html.parser')
soup.prettify()
s = soup.find_all('img',attrs={'class':'illustration'})
print(s)
c = 0
for img_url in s:
	u = img_url.get('src')
	# print(u)
	req_img = requests.get('http:'+u)
	# print(req_img)
	pic = req_img.content
	c+=1
	with open(r'D:\Python\test\获取糗百热图\图片\{}.jpg'.format(c),'wb') as f:
		f.write(pic)
	time.sleep(2)
	print(pic)
