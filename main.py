from dataclasses import field
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


urlResearchGroups = 'https://computacao.ufs.br/pagina/4656'
urlTest = 'https://dayvidsantana.netlify.app/'
classTest = 'txt-present'

driver = webdriver.Chrome() 

def takingData(url, classLookingFor):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    data = soup.find('div', class_=classLookingFor)
    return data



def openPage(url):
    driver.get(url)
    text = takingData(url, classTest)
    print(text)
    driver.quit()


openPage(urlTest)