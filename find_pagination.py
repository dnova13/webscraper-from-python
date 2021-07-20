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
pagination1 = indeed_soup.find("div", {"class" : "pagination"})
pagination2 = indeed_soup.find("div", class_="pagination")
pagination3 = indeed_soup.find("span", class_="pn")

# print(pagination1)

### div 태크에서 class 가  pagination a 태그 전부 뽑음
pages = pagination1.find_all('a')
# print(pages)

### 태그 리스트에서 anchor<a>의 span 을 찾도로 함. 
### 페이지는 리스트 이므로


## ex1) 태그를 포함해서 출력

spans = [];

for page in pages : 
    spans.append(page.find('span'))


print(spans);
print()
print(spans[:-1]); # 마지막에서 첫번째 리스트 가져옴
print()
print(spans[0:-1]); # 마지막에서 첫번째 리스트 가져옴
### pageList[0:-1] = pageList[:-1]


### ex2) 태그를 포함하지 않고 문자열만 출력

spans = [];

for page in pages : 
    spans.append(page.find('span').string)
    ### string 태그 안에 문자열을 출력


print(spans);
print()
print(spans[:-1]); # 마지막에서 첫번째 리스트 가져옴


### ex3) 예2 코드 간략화

spans = [];

for page in pages : 
    spans.append(page.string)


print(spans);
print()
print(spans[:-1]); # 마지막에서 첫번째 리스트 가져옴


### ex4) 예3 string -> int 로

spans = [];

for page in pages[:-1] : 
    spans.append(int(page.string))


print(spans);

maxPage = spans[-1]
print(maxPage);