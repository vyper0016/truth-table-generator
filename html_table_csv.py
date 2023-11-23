from bs4 import BeautifulSoup
import csv

def html_to_csv(html_table, output_csv):
    soup = BeautifulSoup(html_table, 'html.parser')
    table = soup.find('table')
    rows = table.find_all('tr')
    
    data = []
    for row in rows:
        cols = row.find_all(['th', 'td'])
        cols = [col.text.strip() for col in cols]
        data.append(cols)
    
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(data)