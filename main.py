import requests
from bs4 import BeautifulSoup
import time
import csv

def search():
    html=requests.get("https://uraf.harvard.edu/browse/pages?admin_panel=1&f%5B0%5D=sm_og_vocabulary%3Ataxonomy_term%3A123484&f%5B1%5D=sm_og_vocabulary%3Ataxonomy_term%3A123496").text

    soup=BeautifulSoup(html,'html.parser')
    jobs=soup.find_all('article',class_="node node-page node-teaser article clearfix")
    with open("data.csv","a") as f:
        wr=csv.writer(f)
        header=["RESEARCH OPPUTUNITY","DEADLINE","DESCRIPTION","READ MORE"]
        wr.writerow(header)
        for job in jobs:
            name=job.header.h1.a.text
            para=job.find("div",class_="field-item even")
            for p in para.find_all('p',recursive=False):
                if("DEADLINE:" in p.text):
                    dead=p.text[10: ]
                else:
                    info=p.text
            more= job.header.h1.a['href']
            data=[name.strip(),dead.strip(),info.strip(),more.strip()]
            wr.writerow(data)
                
            print("RESEARCH OPPUTUNITY:",name.strip())
            print( "DEADLINE:" ,dead.strip())
            print(info.strip())
            print("READ MORE AT:",more)
            print("____________________________________________________________________________ ")
            print(" ")
    f.close()


search()
        