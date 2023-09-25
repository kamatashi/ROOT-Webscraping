# ROOT-Webscraping
Script para captura de dados usando Webscraping.
<br><br>
Para começar, instale:
````bash
pip install beautifulsoup4 selenium openpyxl requests
````

## Como está organizado
Todas as funções estão no arquivo no arquivo getData.py, elas são importadas para o arquivo principal (main.py) onde criamos testes e scripts  utilizando as funções importadas do getData.py. 
Todas as funções estão no arquivo getData.py e são importadas para o main.py, onde criamos testes e scripts utilizando essas funções importadas do getData.py.
<br>
<br>
O objetivo dos scripts no arquivo principal deve ser o de manipular as informações, apenas.


## Das funções
**OBS:** As unicas funções que serão utilizadas no main.py são createDatabase() e openPage()
### createDatabase
Cria a base de dados em planilhas.
<br>

**Dos parametros:**

- filename: nome do arquivo junto a extenção, por exemplo: dados.csv
- sheetname: nome do sheet que será criado na planilha
- headers: nome das colunas
- rowns: os dados que seram colocados nas listas
<br>
Um exemplo de uso seria:

````py
createDatabase('pessoas.xlsx', 'Sheet1', ['Nome', 'Idade', 'Genero'], [['João', 30, 'Masculino'], ['Jane', 25, 'Feminino']])
````


### openPage
Responsável por abrir o navegador. A função utiliza takingData para captura dos dados e retorna esses dados.
<br>

**Dos paramentros:**

- url: url do site onde estamos buscando as informações
- classLookingFor: a classe que estamos buscando dentro das tags
- tagHTM: o tipo de tag que estamos buscando a class
