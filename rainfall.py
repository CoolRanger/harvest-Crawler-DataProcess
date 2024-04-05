import requests
import json
from bs4 import BeautifulSoup


def rainfall(needed_data):
  # all_url = [
  #   "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=C0M410&stname=%25E9%25A6%25AC%25E9%25A0%25AD%25E5%25B1%25B1&altitude=245m&datepicker=",
  #   "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=467530&stname=%25E9%2598%25BF%25E9%2587%258C%25E5%25B1%25B1&altitude=2413.4m&datepicker=",
  #   "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=C1M480&stname=%25E7%258D%25A8%25E7%25AB%258B%25E5%25B1%25B1&altitude=840m&datepicker=",
  #   "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=C1M400&stname=%25E8%258F%259C%25E7%2593%259C%25E5%259D%25AA&altitude=369m&datepicker=",
  #   "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=C1M390&stname=%25E9%25BE%258D%25E7%25BE%258E&altitude=1090m&datepicker=",
  #   "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=C1M600&stname=%25E9%25A0%25AD%25E5%2587%258D&altitude=986m&datepicker=",
  #   "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=C1M610&stname=%25E7%259F%25B3%25E7%25A3%2590%25E9%25BE%258D&altitude=1083m&datepicker=",
  #   "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=C1M620&stname=%25E7%2591%259E%25E9%2587%258C&altitude=1252m&datepicker="
  # ]
  all_url = needed_data["all_url"]
  unprocess_data = []
  processed_data = []
  for url in range(len(all_url)):
    print(f"    ├─[Requesting url : {url}]")
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
      for j in range(18, 404, 35):
        if l[j] in ['...\xa0', 'X\xa0', 'T\xa0', '/\xa0']:
          l[j] = '-1'
        year_data.append(float(l[j].replace('\\xa0', '')))
      station_data.append(year_data)
    unprocess_data.append(station_data)
    print(f"    │")

  return unprocess_data, 12
