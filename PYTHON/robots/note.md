# Web Scraping in Python with BeautiuflSoup, Selenium, and Scrapy!

## 1 Introduction

### What is the best web scraping library? BS4 vs Selenium vs Scrapy

#### Beautiful Soup

1. Easy to learn
2. No JavaScript Support
3. Inefficiente

#### Selenium

1. Works with JavaScript
2. Easier to lear then Scrapy
3. Slow

#### Scrapy

1. Harder to learn
2. Fast
3. Most complete framework 

## 2 Introduction to BeautifulSoup 4 (BS4)

### How to Install BeautifulSoup 4 and Requests?

#### BeautifulSoup 4

```python
pip install beautifulsoup4
```

#### Requests

```python
pip install requests
``` 

### Example

```python
from bs4 import BeautifulSoup  # Importa a classe BeautifulSoup para fazer a análise do HTML
import requests  # Importa a biblioteca requests para fazer requisições HTTP

# Define a URL do website que será acessado
website = 'https://subslikescript.com/movie/Titanic-120338'

# Faz uma requisição GET para obter o conteúdo HTML da página
response = requests.get(website)

# Extrai o conteúdo HTML da resposta da requisição
content = response.text

# Cria um objeto BeautifulSoup para analisar o conteúdo HTML
soup = BeautifulSoup(content, 'lxml')

# Encontra o elemento <article> com a classe 'main-article'
box = soup.find('article', class_='main-article')

# Extrai o texto do primeiro elemento <h1> dentro do elemento 'box'
title = box.find('h1').get_text()

# Imprime o título na tela
# print(title)

# Encontra o primeiro elemento <div> com a classe 'full-script' dentro do elemento 'box'
# Extrai todo o texto desse elemento, removendo espaços em branco extras
# Utiliza um espaço como separador entre as palavras
transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

# Imprime o texto do script na tela
# print(transcript)

with open(f'{title}.txt', 'w') as file:
    file.write(transcript)
```

## 3 Project#1 Scraping multiple pages with Bs4

```python
from bs4 import BeautifulSoup
import requests

#####################################################
# Extracting links from pagination bar
#####################################################

# How To Get The HTML
root = 'https://subslikescript.com'  # this is the homepage of the website
website = f'{root}/movies_letter-X'  # concatenating the homepage with the movies "letter-X" section. You can choose any section (e.g., letter-A, letter-B, ...)
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')

# Locate the box that contains the pagination bar
pagination = soup.find('ul', class_='pagination')
pages = pagination.find_all('li', class_='page-item')
last_page = pages[-2].text  # this is the number of pages that the website has inside the movies "letter X" section

##################################################################################
# Extracting the links of multiple movie transcripts inside each page listed
##################################################################################

# Loop through all tbe pages and sending a request to each link
for page in range(1, int(last_page)+1):
    result = requests.get(f'{website}?page={page}')  # structure --> https://subslikescript.com/movies_letter-X?page=2
    content = result.text
    soup = BeautifulSoup(content, 'lxml')

    # Locate the box that contains a list of movies
    box = soup.find('article', class_='main-article')

    # Store each link in "links" list (href doesn't consider root aka "homepage", so we have to concatenate it later)
    links = []
    for link in box.find_all('a', href=True):  # find_all returns a list
        links.append(link['href'])

    #################################################
    # Extracting the movie transcript
    #################################################

    for link in links:
        try:  # "try the code below. if something goes wrong, go to the "except" block"
            result = requests.get(f'{root}/{link}')  # structure --> https://subslikescript.com/movie/X-Men_2-290334
            content = result.text
            soup = BeautifulSoup(content, 'lxml')

            # Locate the box that contains title and transcript
            box = soup.find('article', class_='main-article')
            # Locate title and transcript
            title = box.find('h1').get_text()
            transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

            # Exporting data in a text file with the "title" name
            with open(f'{title}.txt', 'w') as file:
                file.write(transcript)
        except:
            print('------ Link not working -------')
            print(link)
```

## 4 XPath

