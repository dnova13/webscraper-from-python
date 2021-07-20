from indeed import extract_indeed_pages, extract_indee_jobs

max_indeed_page = extract_indeed_pages();
print(max_indeed_page)

jobs = extract_indee_jobs(max_indeed_page);

print(jobs);

