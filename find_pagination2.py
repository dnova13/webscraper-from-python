######################################################
# 사이트    디자인 변경으로 인해 방식 변경.

import requests
from bs4 import BeautifulSoup 

indeed_result = requests.get('https://www.indeed.com/jobs?as_and=python&limit=50')

### requests 사용법
# headers
# status_code

""" 
print(indeed_result)

print(indeed_result.status_code) # 상태 코드 가져옴
print(indeed_result.text) # 현재 웹사이트 텍스트를 다 들고옴. 
"""

### BeautifulSoup4 - indeed 웹 스크래핑 

### 텍스 html 로 파싱
indeed_soup = BeautifulSoup(indeed_result.text,"html.parser")

""" 
print(indeed_soup);
print(indeed_soup.title); 
"""

### html 태그 div 태크에서 class 가  pagination 인 애들 뽑음
pagination2 = indeed_soup.find("div", class_="pagination")


### div 태크에서 class 가  pagination a 태그 전부 뽑음
pages = pagination2.find_all('li')
# print(pages)


### 페이지는 리스트 이므로
pageList = [];
i = 1;

### ex1) 태그를 포함해서 출력
for page in pages : 
    if (i == 1) :
        pageList.append(page.find('b'))
        i+= 1
    else :
        pageList.append(page.find('span'))
    
# print(pageList);
print()
print(pageList[:-1]); # 마지막에서 첫번째 리스트 가져옴


### ex2) 태그를 포함하지 않고 출력
pages = pageList[:-1];
pageList = [];

for page in pages : 
    pageList.append(int(page.string))

    
print()
print(pageList); # 마지막에서 첫번째 리스트 가져옴

maxPage = pageList[-1]
print(maxPage);



