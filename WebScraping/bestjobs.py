import requests
from bs4 import BeautifulSoup
import json


headers_param = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0"}
glassdor = requests.get("https://www.glassdoor.com/List/Best-Jobs-in-America-2019-LST_KQ0,25.htm",headers=headers_param)

# status code 200 means you can get data.
print("Status code : ",glassdor.status_code)

# content-> html source code
#print(glassdor.content)

# Setting up soup.
jobs = glassdor.content
soup = BeautifulSoup(jobs, "html.parser")

# title of the page
#print(soup.title)

#.text means i only want to get the text, not the spans, class etc.
#find_all
#print(soup.find("h1").text)

# want to get job titles in the site

jobs = soup.find_all("p", {"class":"h2 m-0 entryWinner pb-std pb-md-0"})

job_names = []

for job in jobs :
    job_names.append(job.a.text)


datas = soup.find_all("div",{"class":"col-6 col-lg-4 dataPoint"})
job_datas = []
for data in datas:
    job_datas.append(data.text)

job_dict = {}

i = 0
j = 0

for job in jobs:
    job_dict[job_names[i]] = (job_datas[j],job_datas[j+1], job_datas[j+2])
    i += 1
    j += 3

# Exporting Data to json file.
with open("jobs.json", "w") as outfile:
    json.dump(job_dict, outfile, indent=3)