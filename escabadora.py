from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

options = webdriver.FirefoxOptions()
browser = webdriver.Firefox(options=options)
browser.get('https://en.wikipedia.org/wiki/List_of_brown_dwarfs')

time.sleep(10)

planets_data = []

def scrape():

    soup = BeautifulSoup(browser.page_source, "html.parser")

    tables = soup.find_all('table', {"class":"wikitable"})

    stars_data = []

    for table in enumerate(tables):
        field_brown_dwarfs = tables[2]
        
    table_body = field_brown_dwarfs.find('tbody')
    table_rows = table_body.find_all('tr')

    for row in table_rows:
        table_cols = row.find_all('td')

        temp_list = []

        for col_data in table_cols:
            temp_list.append(col_data.text.strip())

        stars_data.append(temp_list)

    #print(star_tables[0])

    table_head = field_brown_dwarfs.find('thead')
    table_rows = table_head.find('tr')
    table_heads = table_rows.find_all('th')

    heads = []
    for head in table_heads:
        heads.append(head.text.strip())

    starts_brown_field_csv = pd.DataFrame(stars_data, columns=heads)
    starts_brown_field_csv.to_csv('brigth_starts.csv', index=True, index_label='id')


scrape()