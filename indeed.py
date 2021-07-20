import requests
from bs4 import BeautifulSoup 

LIMIT = 50;
URL='https://www.indeed.com/jobs?as_and=python&limit=50'

def extract_indeed_pages() :
    result = requests.get(URL)### requests 사용법
    soup = BeautifulSoup(result.text,"html.parser")
    pagination2 = soup.find("div", class_="pagination")
    pages = pagination2.find_all('li')

    pageList = [];
    i = 1;

    ### ex1) 태그를 포함해서 출력
    for page in pages : 
        if (i == 1) :
            pageList.append(page.find('b'))
            i+= 1
        else :
            pageList.append(page.find('span'))
        
    ### ex2) 태그를 포함하지 않고 출력
    pages = pageList[:-1];
    pageList = [];

    for page in pages : 
        pageList.append(int(page.string))


    maxPage = pageList[-1]

    return maxPage;

def extract_indee_jobs(last_page) : 
    for page in range(last_page) :
        
        jobs = [];

        ### 각 페이지에서 웹을 호출함.
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text,"html.parser")

        ### 각 페이지의 각 태그 <div class='jobsearch-serpJobCart'> 에서 직업들 추출. 
        ### div 태그에서 클래스는 jobsearch-serpJobCart 인 텍스트 추출  
        results = soup.find_all("div", class_="job_seen_beacon")
        
        for result in results :
            title = result.find("h2", {"class":"jobTitle"})
            # print(title);
            
            ### span 태그 속성 검색 하면 <sapn title='직업 제목'> 이고  class 는 없으므로
            ### span 속성이 title 인거와 class과 없는거 추출 
            ### 하지만 title 에 title 속성 값이 없는게 잇어서 추출 안되므로 코드 변경
            span = title.find('span', {'class':None})["title"];
            print(span)
            
            jobs.append(span)
        
    return jobs;










