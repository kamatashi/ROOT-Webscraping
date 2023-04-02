from dataclasses import field
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


urlResearchGroups = 'https://computacao.ufs.br/pagina/4656'
driver = webdriver.Chrome() 


driver.get(urlResearchGroups)

time.sleep(10)

driver.quit()