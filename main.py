from dataclasses import field
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver


urlResearchGroups = 'https://computacao.ufs.br/pagina/4656'
urlTest = 'https://dayvidsantana.netlify.app/'
classTest = 'txt-present'

driver = webdriver.Chrome() 

def takingData(url, classLookingFor, tagHTML = 'div'):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    data = soup.find(tagHTML, class_=classLookingFor)
    return data.get_text()



def openPage(url, classLookingFor, tagHTML ='div'):
    driver.get(url)
    data = takingData(url, classLookingFor, tagHTML)
    driver.quit()
    return data


print(openPage(urlTest, classTest, 'p'))