#step:0 install requirements like bs4 requests and all packages
import contextlib
import requests
from bs4 import BeautifulSoup as bs
# url="http://codewithharry.com"

# #step:1 get the html
# r = requests.get(url)

# #for html content
# htmlcontent = r.content
# print(htmlcontent)D:\Web_Scraping\main.py



# #step:2 parse the html
# soup = BeautifulSoup(htmlcontent,'html.parser')
# #print(soup)
# #print(soup.prettify())



# #step:3 html tree traversal
# title=soup.title

# print(title)
# print(type(title))#tag
# print(type(title.string))#navigablestring
# print(type(soup))#beautifulsoup

# #commonly used types of objects:
# #tag, navigablestring, beautifulsoup, comment

# #get all the paragraphs from the page
# paras = soup.find_all('p')
# #print(paras)

# #get all the anchors from the page
# an = soup.find_all('a')
# #print(an)

# #get all the links on the page
# all_links=set()
# for link in an:
#     #print(link.get('href'))
#     if(link!='#'):
#         link="https://codewithharry.com"+link.get("href")
#         all_links.add(link)
#         print(link)

# #get first paragraph from the page
# paras = soup.find('p')
# #print(paras)


# #get classes of any element in the html page
# paras = soup.find('p')['class']
# #print(paras)


# #get any element of class lead
# #print(soup.find_all("p",class_="leading-relaxed"))


# #get the text from the tags/soup
# #print(soup.find('p').getText())
# #print(soup.getText())



# #Get content by id
# idc = soup.find(id='__next')
# for ele in idc.contents:
#     print(ele)
    
#     # https://data-flair.training/blogs/online-job-portal-python-project/
#     # https://data-flair.training/blogs/online-job-portal-python-project/
#     # https://gauthamsanthosh.medium.com/ml-jobs-list-452094da414e
#     # https://towardsdatascience.com/building-a-job-recommender-for-non-technical-business-roles-via-nlp-and-machine-learning-626c4039931e
    
#     # https://learning.shine.com/talenteconomy/trends/features-every-online-job-portal-should-consist/
#     # https://techvidvan.com/tutorials/online-job-portal-python-django/

url = 'https://www.techgig.com/jobs/accounts' 
req = requests.get(url)
#soup = bs(req.text, "html.parser")
soup=bs(contextlib,'html.parser');
# print(soup.prettify);
titles=soup.find_all('div',class_="details full-width")
#print(titles);
job_title=[];
job_url_g=[];
company_logo=[];
alldata = soup.find_all('div', class_ = "content-block-extra")
for i, data in enumerate(alldata):
    job_title_g = data.div.div.div.div.div.div.h3
    job_title.append(job_title_g)
    
print(job_title)
