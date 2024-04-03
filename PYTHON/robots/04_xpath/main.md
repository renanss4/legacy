# README: XPath

## Introdução

XPath é uma linguagem de seleção de nós em documentos XML. É frequentemente usado em conjunto com linguagens de consulta como XSLT e XQuery para filtrar e selecionar elementos de documentos XML.

## Conceitos Básicos

### Nós (Nodes)

- Em XML, tudo é considerado um nó. Isso inclui elementos, atributos, texto, comentários e instruções de processamento.
- Os tipos de nós mais comuns em XPath são:
  - Elementos
  - Atributos
  - Texto
  - Comentários

### Expressões de Caminho (Path Expressions)

- As expressões de caminho são usadas para navegar através da estrutura hierárquica de um documento XML.
- Uma expressão de caminho começa com uma barra (/) e descreve o caminho de um nó raiz para o nó desejado.

### Funções

- XPath oferece uma variedade de funções para realizar operações em nós e valores.
- Algumas funções comuns incluem `contains()`, `starts-with()`, `concat()`, `substring()`, entre outras.

## Exemplos

Suponha que temos o seguinte documento XML:

```xml
<bookstore>
  <book category="fiction">
    <title lang="en">Harry Potter</title>
    <author>J.K. Rowling</author>
  </book>
  <book category="non-fiction">
    <title lang="en">The Elements of Style</title>
    <author>William Strunk Jr.</author>
  </book>
</bookstore>
```

### Exemplo 1: Selecionar todos os elementos `title`:

```xpath
//title
```

### Exemplo 2: Selecionar o atributo `lang` do elemento `title`:

```xpath
//title/@lang
```

### Exemplo 3: Selecionar o texto do elemento `author` do segundo livro:

```xpath
//book[2]/author/text()
```

### Exemplo 4: Selecionar todos os livros cujo título contém a palavra "Harry":

```xpath
//book[contains(title, 'Harry')]
```

### Exemplo 5: Selecionar todos os livros cujo título começa com a palavra "The":

```xpath
//book[starts-with(title, 'The')]
```

## Recursos Adicionais

Para mais informações sobre XPath, consulte a documentação oficial do XPath:

- [W3C XPath Specification](https://www.w3.org/TR/xpath/)
