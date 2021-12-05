import requests  
from bs4 import BeautifulSoup
from app import main
from db.schema import NewData


entry = NewData 
base_url = "https://www.urparts.com/"
URL = "https://www.urparts.com/index.cfm/page/catalogue"

def scrape_now():
    r = requests.get(URL) 
    soup = BeautifulSoup(r.content, 'lxml') 
    table = soup.find_all('ul') 
    for li in table[1].find_all("a"):
        manufacturer = []
        man_link = []
        man_link.append(li['href'])
        manufacturer.append(li.text)
        new_url = base_url + str(man_link[0])
        r = requests.get(new_url) 
        soup = BeautifulSoup(r.content, 'lxml') 
        table = soup.find_all('ul') 
        for li in table[1].find_all("a"):
            catalog=[]
            catalog_link=[]
            catalog_link.append(li['href'])
            catalog.append(li.text)
            ne_url =  base_url + str(catalog_link[0])
            r = requests.get(ne_url) 
            soup = BeautifulSoup(r.content, 'lxml') 
            table = soup.find_all('ul')
            for li in table[2].find_all("a"):
                model_link = []
                model = []
                model_link.append(li['href'])
                model.append(li.text)
                n_url = base_url+ str(model_link[0])
                r = requests.get(n_url) 
                soup = BeautifulSoup(r.content, 'lxml') 
                table = soup.find_all('ul')
                part = []
                for li in table[1].find_all("a"):
                    part.append(li.text)
                    print(len(part))
                    for x in range(len(part)):
                        part_category =[]
                        part_new = []
                        a  = part[x].split("-")
                        part_new.append(a[0]) 
                        part_category.append(a[1])
                        # print(manufacturer,catalog,model,part_new,part_category)
                        entry.manufacturer = manufacturer[0].strip()
                        entry.category= catalog[0].strip()
                        entry.model = model[0].strip()
                        entry.part = part_new[0].strip()
                        entry.part_category = part_category[0].strip()
                        # print(entry)
                        main.add(entry)