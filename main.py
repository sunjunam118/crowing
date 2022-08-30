# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import csv
#
# html = urlopen("https://m.ssg.com/disp/category.ssg?dispCtgId=6000201498")
#
# bsObject = BeautifulSoup(html, "html.parser")
#
# # for link in bsObject.find_all('em'):
# #    print(link.text.strip(), link.get('class'))
#
#
# soup = bsObject.find_all(name="a")
# #print(name)
#
#
# heading = soup.find(name="span")
# section_heading = soup.find(name="em", class_="ssg_price")
# print(section_heading.getText())
#
#
# # 링크만 가져 올 수 있다.
# #for tag in name:
# #    print(tag.get("href"))
#
#
# # 모든 txt 구문을 불러오고 싶을때
# #for tag in name:
# #    print(tag.getText())
