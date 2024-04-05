import requests
import json
from bs4 import BeautifulSoup

def sunshine(needed_data):
  
  all_url = needed_data["all_url"]
  unprocess_data = []
  for url in range(len(all_url)):
    print(f"    ├─[Requesting url : {url}]")
    station_data = []
    MAX = 2022
    for i in range(2005, MAX):
      if i == MAX - 1:
        print(f"    │    ╘═> {i} processing...")
      else:
        print(f"    │    ╞═> {i} processing...")
        
      data = BeautifulSoup(requests.get(f"{all_url[url]}{i}").text, features="html5lib")
      l = [j.text for j in data.select("#MyTable tbody tr td")]
  
      year_data = []
      for j in range(169, 310, 35):
        if l[j] in ['...\xa0', 'X\xa0', 'T\xa0', '/\xa0']:
          l[j] = '-1'
        year_data.append(float(l[j].replace('\\xa0', '')))
      station_data.append(year_data)
    unprocess_data.append(station_data)
    print(f"    │")

  return unprocess_data, 5