from dataclasses import field
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json


urlGruposPesquisa = 'https://computacao.ufs.br/pagina/4656'
driver = webdriver.Chrome('')
