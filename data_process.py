def data_process(data, num_month, station_count):
  print(f"    └─[Processing data...]")
  processed_data = []
  for i in range(17):
    mom = [station_count for t in range(num_month)]
    month = [0 for t in range(num_month)]
    year = []

    for j in range(station_count):
      for k in range(num_month):
        try:
          if data[j][i][k] == -1:
            mom[k] -= 1
          else:
            month[k] += data[j][i][k]
        except:
          pass

    for s in range(num_month):
        year.append(month[s] / mom[s])
      
    processed_data.append(year)
  return processed_dataS
      