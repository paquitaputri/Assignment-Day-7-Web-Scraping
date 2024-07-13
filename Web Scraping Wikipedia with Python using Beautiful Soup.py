import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


url = 'https://en.wikipedia.org/wiki/List_of_highest-grossing_films'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
table_name = 'wikitable sortable plainrowheaders sticky-header col4right col5center col6center' 
soup_table = soup.find('table', {'class':table_name})

# Cari class table 
tables = soup.find_all('table')

# Ambil data table dan masukan kedalam list
list = []  # 
for table in tables:
    list.append(pd.read_html(str(table))[0])


table_ranking_movie = list[0]
table_ranking_movie = table_ranking_movie.drop(columns=["Ref"])
table_ranking_movie.to_csv("List-of-highest-grossing-films.csv", index=False)