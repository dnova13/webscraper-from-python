import requests
from bs4 import BeautifulSoup
import re

URL = f'https://stackoverflow.com/jobs?q=python'


def extract_last_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", class_="s-pagination").find_all('a')

    last_page = pages[-2].get_text(strip=True)  ### #soup get_text(strip)

    return int(last_page)


def extract_job(html):

    title = html.find("h2",class_="fc-black-800").find("a")["title"]

    """ 
    company_row = html.find("h3",class_="fc-black-700").find_all("span", recursive=False) 
    # recursive=False : 더 깊게 찾지 않도록 방지 해줌. 
    #                 즉 <span>1<span>2</span><span)  첫 단계의 <sapn>1</span>만 가져오도록함.

    company = company_row[0]
    location = company_row[1]
    """

    ### python 기법 배열에서 가져오는 변수 종류가 확실할때
    company, location = html.find("h3",class_="fc-black-700").find_all("span", recursive=False) 
    # recursive=False : 더 깊게 찾지 않도록 방지 해줌. 
    #                 즉 <span>1<span>2</span><span)  첫 단계의 <sapn>1</span>만 가져오도록함.

    company = company.get_text(strip=True).strip("\r").strip("\n")
    location = location.get_text(strip=True).strip("\r").strip("\n")
    job_id = html["data-jobid"]

    return {
        'title': title,
        'company': company,
        "location": location,
        "link": f"https://stackoverflow.com/jobs/{job_id}"
    }


def extract_jobs(last_page):
    jobs = []

    for page in range(last_page):
        print(f"Scrapping SO page {page+1}")

        ### 각 페이지에서 웹을 호출함.
        result = requests.get(f"{URL}&pg={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "-job"})

        for result in results:
            job = extract_job(result)
            jobs.append(job)

    return jobs


def get_jobs():
    last_indeed_page = extract_last_pages()
    jobs = extract_jobs(last_indeed_page)

    return jobs
