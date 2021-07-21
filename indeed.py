import requests
from bs4 import BeautifulSoup 
import re

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

def extract_job(html) :

    ### 직업 추출
    ### span 태그 속성 검색 하면 <sapn title='직업 제목'> 이고  class 는 없으므로
    ### span 속성이 title 인거와 class과 없는거 추출 
    ### 하지만 title 에 title 속성 값이 없는게 잇어서 추출 안되므로 코드 변경
    title = html.find("h2", {"class":"jobTitle"}).find('span', {'class':None})["title"];
    
    ### 회사 이름 추출
    company_span = html.find("span", class_="companyName");
    company_anchor = company_span.find('a')

    if company_anchor is not None :
        company = str(company_anchor.string) ### string 으로 변경.
    else :
        company = str(company_span.string)
    
    company = company.strip(); ### 빈 공간을 없앰. 다른 예로 strip("F") F로 된 글자 다 없애줌.

    ### 위치 추적
    # location = html.find('div', class_="companyLocation")
    location = html.select_one('div.companyLocation')

    # 추출한 태그에 자식 태그들 제거
    for tag in location.find_all():
        # tag.extract() ### extract() : 자식 태그 제거하면서 제거된 태그 값을 리턴함.
        tag.decompose() ### decompose() : 자식 태그 제거 
       
    location = location.text
    job_id = html.parent['data-jk']
    job_tk = html.parent['data-mobtk']

    return {
        'title' : title, 
        'company' : company, 
        "location" : location, 
        "link" : f"https://www.indeed.com/viewjob?jk={job_id}&tk={job_tk}&from=serp&vjs=3"}

def extract_indee_jobs(last_page) : 

    jobs = [];

    for page in range(last_page) :
        
        print(f"Scrapplin page {page+1}")

        ### 각 페이지에서 웹을 호출함.
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text,"html.parser")

        ### 각 페이지의 각 태그 <div class='jobsearch-serpJobCart'> 에서 직업들 추출. 
        ### div 태그에서 클래스는 jobsearch-serpJobCart 인 텍스트 추출  
        ### find_all : 검색하는 키워드 전부 찾음
        ### find : 검색하는 키워드 중 하나만 찾음
        results = soup.find_all("div", class_="slider_container")   

        for result in results :
            job = extract_job(result)
            jobs.append(job) 
        
    return jobs;

def get_jobs() :
    last_indeed_page = extract_indeed_pages();

    indeed_jobs = extract_indee_jobs(last_indeed_page);

    return indeed_jobs;








