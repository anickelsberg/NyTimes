from datetime import date
import csv
import requests
from collections import Counter

today = date.today()

response = requests.get('https://api.nytimes.com/svc/topstories/v2/home.json?api-key=XX')
json_data = response.json()
results = json_data["results"]


tag_counter = Counter()

for result in results:
	for tag in result["des_facet"]:
		tag_counter[tag] += 1


with open('remember_when.csv','a') as data_file:
	csv_writer = csv.writer(data_file)
	for tag,count in tag_counter.items():
		csv_writer.writerow([today, tag, count])



print(csv_writer)	
