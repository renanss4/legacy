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