import requests
from  bs4 import BeautifulSoup
import shutil

r=requests.get("https://schools.aglasem.com/ncert/ncert-books-class-11-computers-and-communication-technology-chapter-10/")
c=r.content
print(r.status_code,"Item is ok")

soup=BeautifulSoup(c,"html.parser")
filename='temp.html'
formatted_text=soup.prettify()
with open(filename,"w+") as f :
    f.write(formatted_text)


items=soup.find_all("img")

print("No of image tags",len(items))
try:

    for item in items:
        item_link =item.get('src')
        ext=item_link[item_link.rindex("."):]

        print(item_link)
        print(ext)

    
except Exception as e:
    print(e)
