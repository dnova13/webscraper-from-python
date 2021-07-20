import requests

indeed_result = requests.get('https://www.indeed.com/jobs?as_and=python&limit=50')



# headers
# status_code

print(indeed_result)
print(indeed_result.text) # 현재 웹사이트 텍스트를 다 들고옴.

### 페이지 숫자 가져옴.
