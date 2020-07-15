# import requests
# from bs4 import BeautifulSoup
# from urllib.request import urlopen
# # 'features="lxml"'
# URL = 'https://inkbox.com/products/all-tattoos'
# page = requests.get(URL)
# # uREQ = urlopen(url)
# # pageC = uREQ.read()
# # uREQ.close()
# soup = BeautifulSoup(page.content,'html.parser') 

# results = soup.find(id="site-content")

# print(results.prettify())

# tattoo_elems = results.find_all('div', class_='container shopLanding_pageHeader')
# for tattoo_elem in tattoo_elems:
#     print(tattoo_elem, end='\n'*2)

# animal_elem = results.find_all('h3', string='animal')
# print(animal_elem)
# pet_elem = results.find_all('li', string=lambda text: 'pet' in text())
# print(pet_elem)                            

# Each tattoo_elem is a new BeautifulSoup object.
# I use the same methods on it as before.

# alltattoo_elem = tattoo_elem.find('h2', class_='product-main-title"')
# productlist_elem = tattoo_elem.find('div', class_='product_list accountInfo')
# category_elem = tattoo_elem.find('div', class_='filter__section-header')
# animal_elem = tattoo_elem.find('div', class_='custom-check filter__tags filter__tags__animal')
# infotattoo_elem = tattoo_elem.find('div', class_='pd-headerInfo-group')

# if None in (title_elem, company_elem, location_elem):
#         continue
#     print(title_elem.text.strip())
#     print(company_elem.text.strip())
#     print(location_elem.text.strip())
#     print()
# print(alltattoo_elem)
# print(productlist_elem)
# print(category_elem)
# print(animal_elem)
# print(infotattoo_elem)
# print()
# print(results.prettify())

import requests
from bs4 import BeautifulSoup


URL = "https://www.monster.com/jobs/search/?q=Software-Developer\
        &where=Australia"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")

# Look for Python jobs
python_jobs = results.find_all("h2", string=lambda t: "python" in t.lower())
for p_job in python_jobs:
    link = p_job.find("a")["href"]
    print(p_job.text.strip())
    print(f"Apply here: {link}\n")

# Print out all available jobs from the scraped webpage
job_elems = results.find_all("section", class_="card-content")
for job_elem in job_elems:
    title_elem = job_elem.find("h2", class_="title")
    company_elem = job_elem.find("div", class_="company")
    location_elem = job_elem.find("div", class_="location")
    if None in (title_elem, company_elem, location_elem):
        continue
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print()

