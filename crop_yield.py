import requests
import json
from bs4 import BeautifulSoup


def crop_yield(needed_data):
  url = "https://data.coa.gov.tw/Service/OpenData/TransService.aspx?UnitId=i5AdyGE26hcq"
  print('    ├─[Requesting...]')
  data = requests.get(url)
  region = needed_data["region"]
  r = json.loads(data.text)
  amount = []  #05~21年嘉義蓬萊的產量
  
  for i in r:
    if i["local"] == region and i["crop_item"] == "稉稻(蓬萊)":
      amount.append(float(i["output"]) / float(i['gain']))
  if len(amount) < 17:
    print("Error! Fail to fetch : ", region)
  return amount

