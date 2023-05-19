import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.failory.com/startups/india#%E2%80%8D-300-startups-in-india"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

company_names = []
company_elements = soup.find_all('h3')
for element in company_elements:
    company_names.append(element.text.strip())

with open('company_names.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Company Name'])
    for name in company_names:
        writer.writerow([name])

print("Scraping completed and CSV file created!")
