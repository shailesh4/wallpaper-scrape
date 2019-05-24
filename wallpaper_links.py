import requests
from bs4 import BeautifulSoup
import re


def getGoodLink(bad_link):
	pattern = '\'\)\;'
	result = re.sub(pattern,'', bad_link)
	result = result.replace('prevframe_show(\'','')
	result = result.replace('wallite','download')
	return result
	# print(bad_link)
	
def getBestSize(result):
	sizes = ["-5120x2880","-3840x2160","-3554x1999","-2400x1350","-1920x1080","-1280x768"]
	idx = result.index('.html')
	for size in sizes:
		url = result[:idx] + size + result[idx:]
		name = url[url.index('download/')+9:url.index('.html')]
		h = requests.head(url, allow_redirects = True).headers.get('content-type')
		flag = True
		if 'text' in h:
			flag = False	
		elif 'html' in h:
			flag = False
		if(flag):
			r = requests.get(url, allow_redirects= True)
			open(f'Photos1/{name}.jpeg','wb').write(r.content)
			break
		
	

def getLinks(web_link):
	file = open("link_page", "w+", encoding ="utf-8")
	file.write(requests.get(web_link, verify = False).text)
	file.close()


	file = open("link_page", "r", encoding ="utf-8")

	soup = BeautifulSoup(file.read(),'html.parser')
	file.close()

	
	for link in soup.find_all(id ="huddown"):
		url = getGoodLink(link.get('onclick'))
		getBestSize(url)
		
		
	
	
	
for i in range(1,180):
		link = f"http://wallpaperswide.com/girls-desktop-wallpapers/page/{i}"
		getLinks(link)
		













