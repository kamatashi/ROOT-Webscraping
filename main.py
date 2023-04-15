from dataclasses import field
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


urlResearchGroups = 'https://computacao.ufs.br/pagina/4656'
driver = webdriver.Chrome() 


def createDataBase(way):
    values = []
    df = pd.DataFrame({'Values': values})
    df.to_csv('data.csv', index=False)

    # necessário caminho das DIVs no data, o way é o DATA
    for item in way.find_all('li'):
        values.append(item.text)


def lookingForData():
    soup = BeautifulSoup(driver.content, 'html.parser')
    data = soup.find('div', class_='data')
    return data


def openPage(url):
    driver.get(url)
    time.sleep(10)
    driver.quit()


openPage(urlResearchGroups)