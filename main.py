from dataclasses import field
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


urlResearchGroups = 'https://computacao.ufs.br/pagina/4656'
driver = webdriver.Chrome() 




def openPage(url):
    driver.get(url)
    #lookingForData(url)
    time.sleep(10)
    driver.quit()


openPage(urlResearchGroups)