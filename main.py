# import requests
import json
# from bs4 import BeautifulSoup
import time

##### Other Project #####
# from rainfall import rainfall#雨量
from crop_yield import crop_yield  #產量
# from sunshine import sunshine #日照
# from wind_speed import wind_speed #風速
# from temperature import temperature #溫度
from data_process import data_process  #Process Function
from data_request import data_request
#########################
_using_data = [
  {
    "region":
    "嘉義市",
    "all_url": [
      "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=C0M410&stname=%25E9%25A6%25AC%25E9%25A0%25AD%25E5%25B1%25B1&altitude=245m&datepicker=",
      "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=467530&stname=%25E9%2598%25BF%25E9%2587%258C%25E5%25B1%25B1&altitude=2413.4m&datepicker=",
      "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=C1M480&stname=%25E7%258D%25A8%25E7%25AB%258B%25E5%25B1%25B1&altitude=840m&datepicker=",
      "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=C1M400&stname=%25E8%258F%259C%25E7%2593%259C%25E5%259D%25AA&altitude=369m&datepicker=",
      "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=C1M390&stname=%25E9%25BE%258D%25E7%25BE%258E&altitude=1090m&datepicker=",
      "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=C1M600&stname=%25E9%25A0%25AD%25E5%2587%258D&altitude=986m&datepicker=",
      "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=C1M610&stname=%25E7%259F%25B3%25E7%25A3%2590%25E9%25BE%258D&altitude=1083m&datepicker=",
      "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=C1M620&stname=%25E7%2591%259E%25E9%2587%258C&altitude=1252m&datepicker="
    ]
  }
]

using_data = [
  {
    "region":
    "嘉義市",
    "all_url": [
      "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=C0M410&stname=%25E9%25A6%25AC%25E9%25A0%25AD%25E5%25B1%25B1&altitude=245m&datepicker=",
      "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=467530&stname=%25E9%2598%25BF%25E9%2587%258C%25E5%25B1%25B1&altitude=2413.4m&datepicker=",
      "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=C1M480&stname=%25E7%258D%25A8%25E7%25AB%258B%25E5%25B1%25B1&altitude=840m&datepicker=",
      "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=C1M400&stname=%25E8%258F%259C%25E7%2593%259C%25E5%259D%25AA&altitude=369m&datepicker=",
      "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=C1M390&stname=%25E9%25BE%258D%25E7%25BE%258E&altitude=1090m&datepicker=",
      "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=C1M600&stname=%25E9%25A0%25AD%25E5%2587%258D&altitude=986m&datepicker=",
      "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=C1M610&stname=%25E7%259F%25B3%25E7%25A3%2590%25E9%25BE%258D&altitude=1083m&datepicker=",
      "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=C1M620&stname=%25E7%2591%259E%25E9%2587%258C&altitude=1252m&datepicker="
    ]
  },
  {
    "region":
    "台南市",
    "all_url": [
      "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=467410&stname=%25E8%2587%25BA%25E5%258D%2597&altitude=40.8m&datepicker=",
      "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=467420&stname=%25E6%25B0%25B8%25E5%25BA%25B7&altitude=8.1m&datepicker=",
      "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=C0O840&stname=%25E7%258E%258B%25E7%2588%25BA%25E5%25AE%25AE&altitude=134.0m&datepicker=",
      "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=C0O930&stname=%25E7%258E%2589%25E4%25BA%2595&altitude=69m&datepicker=",
      "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=C0X310&stname=%25E4%25B8%2583%25E8%2582%25A1&altitude=9m&datepicker="
    ]
  },
  # { 
  #   "region":
  #   "宜蘭市",
  #   "all_url": [
  #     "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=467080&stname=%25E5%25AE%259C%25E8%2598%25AD&altitude=7.2m&datepicker=",
  #     "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=C0U860&stname=%25E9%25A0%25AD%25E5%259F%258E&altitude=5.0m&datepicker=",
  #     "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=C0U780&stname=%25E4%25BA%2594%25E7%25B5%2590&altitude=15m&datepicker=",
  #     "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=C0U890&stname=%25E4%25B8%2589%25E6%2598%259F&altitude=116m&datepicker=",
  #     "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=C0U940&stname=%25E7%25BE%2585%25E6%259D%25B1&altitude=25m&datepicker="
  #   ]
  # },
  {
    "region":
    "花蓮縣",
    "all_url": [
      "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=466990&stname=%25E8%258A%25B1%25E8%2593%25AE&altitude=16.1m&datepicker=",
      "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=C0T820&stname=%25E5%25A4%25A9%25E7%25A5%25A5&altitude=550m&datepicker=",
      "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=C0T9E0&stname=%25E5%25A4%25A7%25E5%259D%2591&altitude=415m&datepicker=",
      "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=C0T9D0&stname=%25E5%2592%258C%25E4%25B8%25AD&altitude=8m&datepicker=",
      "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=C0T9G0&stname=%25E9%25B3%25B3%25E6%259E%2597%25E5%25B1%25B1&altitude=605m&datepicker="
    ]
  },
  # {
  #   "region":
  #   "新北市",
  #   "all_url": [
  #     "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=466900&stname=%25E6%25B7%25A1%25E6%25B0%25B4&altitude=19.0m&datepicker=",
  #     "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=C0A940&stname=%25E9%2587%2591%25E5%25B1%25B1&altitude=49m&datepicker=",
  #     "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=C0AH00&stname=%25E6%25B1%2590%25E6%25AD%25A2&altitude=38.0m&datepicker=",
  #     "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=C0A530&stname=%25E5%259D%25AA%25E6%259E%2597&altitude=300m&datepicker=",
  #     "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=C0A650&stname=%25E7%2581%25AB%25E7%2587%2592%25E5%25AF%25AE&altitude=287m&datepicker="
  #   ]
  # },
  {
    "region":
    "台東縣",
    "all_url": [
      "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=467540&stname=%25E5%25A4%25A7%25E6%25AD%25A6&altitude=8.1m&datepicker=",
      "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=467610&stname=%25E6%2588%2590%25E5%258A%259F&altitude=33.5m&datepicker=",
      "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=C0S700&stname=%25E7%259F%25A5%25E6%259C%25AC&altitude=507m&datepicker=",
      "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=C0S710&stname=%25E9%25B9%25BF%25E9%2587%258E&altitude=382m&datepicker=",
      "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=C0S740&stname=%25E6%25B1%25A0%25E4%25B8%258A&altitude=289m&datepicker="
    ]
  },
  {
    "region":"苗栗縣",
    "all_url": [
      "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=C0E420&stname=%25E7%25AB%25B9%25E5%258D%2597&altitude=19m&datepicker=",
      "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=C0E730&stname=%25E9%25A0%25AD%25E4%25BB%25BD&altitude=26m&datepicker=",
      "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=C0E740&stname=%25E9%2580%25A0%25E6%25A9%258B&altitude=27m&datepicker=",
      "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=C1E601&stname=%25E5%258D%2597%25E5%258B%25A2&altitude=125m&datepicker=",
      "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=C0E540&stname=%25E5%25BE%258C%25E9%25BE%258D&altitude=32m&datepicker="
    ]
  },
  {
    "region":
    "新竹市",
    "all_url": [
      "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=C0D560&stname=%25E7%25AB%25B9%25E6%259D%25B1&altitude=147m&datepicker=",
      "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=C0D580&stname=%25E5%25AF%25B6%25E5%25B1%25B1&altitude=120.0m&datepicker=",
      "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=C0D360&stname=%25E6%25A2%2585%25E8%258A%25B1&altitude=523m&datepicker=",
      "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=C0D430&stname=%25E5%25B3%25A8%25E7%259C%2589&altitude=87m&datepicker=",
      "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=C1D410&stname=%25E7%2599%25BD%25E8%2598%25AD&altitude=1290m&datepicker=",
    ]
  },
]
# all_function = [rainfall, temperature, sunshine, wind_speed]


def data_fetcher(func, needed_data):
  print(f'Running {func.__name__}')
  start = time.time()
  data, month = func(needed_data) #here
  data = data_process(data, month, len(needed_data["all_url"]))
  end = time.time()
  print(f'Finished {func.__name__}, used {int(end - start)}s\n')
  return data


def main_process(using_data):

  final_data = []

  for needed_data in using_data:
    print(f"Searching {needed_data['region']}...\n")
    temp = [[] for i in range(17)]
    data = data_fetcher(data_request, needed_data)

    #requesting crop yield
    print('Running Crop_yield')
    start = time.time()
    crop = crop_yield(needed_data)
    end = time.time()
    print(f'Finished Crop_yield, used {int(end - start)}s\n')

    for i in range(17):
      temp[i].append(data[i])
      temp[i].append(crop[i])
    final_data.append(temp)
  return final_data


processed_data = main_process(using_data)
data_for_json = {}
data_for_json["data"] = processed_data

with open("data.json", "w") as w:
  json.dump(data_for_json, w)

