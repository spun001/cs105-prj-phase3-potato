
# LINK TO STACKOVERFLOW: https://stackoverflow.com/questions/45070818/python-web-scraper-crawler-html-tables-to-excel-spreadsheet

import csv
import requests
import bs4

url =  'https://www.nifc.gov/fireInfo/fireInfo_stats_IgFires.html'
response = requests.get(url)
html = response.content

soup = bs4.BeautifulSoup(html, "lxml")

tables = soup.findAll("table")

tableMatrix = []
for table in tables:
    #Here you can do whatever you want with the data! You can findAll table row headers, etc...
    list_of_rows = []
    for row in table.findAll('tr')[1:]:
        list_of_cells = []
        for cell in row.findAll('td'):
            text = cell.text.replace('&nbsp;', '')
            list_of_cells.append(text)
        list_of_rows.append(list_of_cells)
    tableMatrix.append((list_of_rows, list_of_cells))
print(tableMatrix)

