import requests
import json
from bs4 import BeautifulSoup


def data_request(needed_data):
  
  all_url = needed_data["all_url"]
  unprocess_data = []
  for url in range(len(all_url)):
    print(f"    ├─[Requesting station : {url+1}]")
    station_data = []
    MAX = 2022
    for i in range(2005, MAX):
      if i == MAX - 1:
        print(f"    │    ╘═> {i} processing...")
      else:
        print(f"    │    ╞═> {i} processing...")

      data = BeautifulSoup(requests.get(f"{all_url[url]}{i}").text,
                           features="html5lib")
      l = [j.text for j in data.select("#MyTable tbody tr td")]

      year_data = []
      
      #rainfall(18, 403) 
      #sunshine(169, 309) temperature(147, 287) wind(153, 293)
      if i == MAX - 1:
        line = "    │     "
      else:
        line = "    │    │"
      print(f"{line}  └─[Loading Data...]")
      print(f"{line}      ╞═> rain_fall loading...")
      for j in range(18, 404, 35):#rain_fall
        if l[j] in ['...\xa0', 'X\xa0', 'T\xa0', '/\xa0']:
          l[j] = '-1'
        year_data.append(float(l[j].replace('\\xa0', '')))

      print(f"{line}      ╞═> Sun_shine loading...")
      for j in range(169, 310, 35):#sun_shine
        if l[j] in ['...\xa0', 'X\xa0', 'T\xa0', '/\xa0']:
          l[j] = '-1'
        year_data.append(float(l[j].replace('\\xa0', '')))

      print(f"{line}      ╞═> Temperature loading...")
      for j in range(147, 288, 35):#temperature
        if l[j] in ['...\xa0', 'X\xa0', 'T\xa0', '/\xa0']:
          l[j] = '-1'
        year_data.append(float(l[j].replace('\\xa0', '')))

      print(f"{line}      ╘═> Wind_speed loading...")
      for j in range(153, 294, 35):#wind_speed
        if l[j] in ['...\xa0', 'X\xa0', 'T\xa0', '/\xa0']:
          l[j] = '-1'
        year_data.append(float(l[j].replace('\\xa0', '')))
        
      station_data.append(year_data)
    unprocess_data.append(station_data)
    print("    │")

  return unprocess_data, 27