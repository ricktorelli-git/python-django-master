# Django Master

## Projeto de estudo do framework Django

### 01 - Introdução e Informações Importantes

#### O que é o Django?

Django é um framework web de alto nível escrito em Python que incentiva o desenvolvimento rápido e limpo. Desenvolvido
por uma equipe experiente, Django leva cuidado com a segurança de seus desenvolvedores e oferece muitas ferramentas
para construir sites seguros.

#### O que é um framework?

Um framework é um conjunto de códigos que facilita o desenvolvimento de aplicações web. Ele fornece uma estrutura
para o desenvolvimento de aplicações web, permitindo que os desenvolvedores gastem menos tempo escrevendo códigos
repetitivos e mais tempo escrevendo códigos de aplicação.

#### Arquitetura MVT  (Model-View-Template).

- Model - O Model é a camada de dados. Esta camada é responsável por manter a lógica de negócios e interagir com o
  banco.
- View - A View é a camada de controller do Django. Esta camada é responsável por processar as requisições do usuário e
  retornar as respostas.
- Template - O Template é a camada de apresentação. Seria o front-end da aplicação.

#### Django é Full Stack?

Sim, Django é um framework full stack. Ele é um framework full stack porque ele fornece todas as ferramentas necessárias
para criar um site completo, incluindo um banco de dados, um servidor web e um sistema de templates.

#### O que podemos fazer com Django?

1. [x] Criar um site completo.
2. [x] Criar um blog.
3. [x] Criar um sistema de gerenciamento de conteúdo.
4. [x] Criar ERP`s.
5. [x] Criar CRM`s.
6. [x] Criar PDV`s.
7. [x] Criar API`s.

### 02 - Bases e Conceitos Importantes

#### Sistema Desktop x Sistema Web

- Sistema Desktop: É um software que é instalado no computador do usuário e é executado localmente.
- Sistema Web: É um software executado em um servidor web e é acessado por meio de um navegador.
- Vantagens de um Sistema Web:
    - Acessível de qualquer lugar.
    - Não precisa de instalação.
    - Fácil de atualizar.
    - Fácil de escalar.
    - Fácil de integrar com outros sistemas.

#### Protocolo HTTP e HTTPS

- HTTP: É um protocolo de comunicação que permite a transferência de informações na web. O HTTP é a base da web. HTTP
  significa Hypertext Transfer Protocol. O HTTP reconhece HTML, CSS e JavaScript. E no caso de APIs, o HTTP reconhece
  JSON, XML e outras terminações.
- HTTPS: É uma versão segura do HTTP que criptografa as informações transferidas entre o cliente e o servidor.
- Vantagens do HTTPS:
    - Mais seguro.
    - Melhor para SEO.
    - Melhor para a reputação do site.
    - Melhor para a confiança do usuário.
    - Melhor para a privacidade do usuário.
    - Melhor para a proteção de dados.
    - Melhor para a proteção contra hackers.
    - Melhor para a proteção contra ataques de phishing.
- Como Funciona o protocolo HTTP:
    - O cliente envia uma requisição para o servidor.
    - O servidor processa a requisição e envia uma resposta para o cliente.
    - O cliente recebe a resposta e exibe o conteúdo no navegador.
    - O ciclo se repete até que o usuário feche o navegador.
    - Exemplo de requisição HTTP:
      ```
      GET / HTTP/1.1
      Host: www.example.com
      User-Agent: Mozilla/5.0
      Accept: text/html
      ```
    - Exemplo de resposta HTTP:
        ```
        HTTP/1.1 200 OK
        Content-Type: text/html
        Content-Length: 1234
        <html>
        <head>
        <title>Example</title>
        </head>
        <body>
        <h1>Hello, World!</h1>
        </body>
        </html>
        ```
- Conceito de Client Side e Server Side:
    - Client Side: É o lado do cliente. É o lado do navegador. É o lado do usuário.
        - Só entente HTML, CSS e JavaScript.
    - Server Side: É o lado do servidor. É o lado do servidor web. É o lado do desenvolvedor.

- Conceito de URL e URI:
    - URL: É um endereço da web. URL significa Uniform Resource Locator. Exemplo: https://www.example.com.
    - URI: É um identificador de recurso. URI significa Uniform Resource Identifier. Exemplo: /index.html.

#### O que é PIP ?

- PIP é um gerenciador de pacotes para projetos Python. Ele permite instalar, remover e atualizar pacotes Python
  facilmente. É similar ao NPM do Node.js e ao Composer do PHP. O PIP possui um repositório oficial chamado PyPI (Python
  Package Index), que podemos acessar no site https://pypi.org.
- Comandos Básicos do PIP:
    - Instalar um pacote: `pip install nome_do_pacote`.
    - Remover um pacote: `pip uninstall nome_do_pacote`.
    - Atualizar um pacote: `pip install --upgrade nome_do_pacote`.
    - Listar pacotes instalados: `pip list`.
    - Listar pacotes desatualizados: `pip list --outdated`.
    - Instalar pacotes a partir de um arquivo: `pip install -r requirements.txt`.
    - Gerar um arquivo de dependências: `pip freeze > requirements.txt`.

#### O que ambiente virtual Python (Virtualenv)?

- Um ambiente virtual Python é um ambiente isolado que permite instalar pacote Python sem interferir no sistema
  operacional. Um ambiente virtual Python é útil para manter as dependências de um projeto organizadas e separadas.
- Isso é importante porque um projeto Python pode ter várias dependências e essas dependências podem ter versões
  diferentes. Se instalarmos todas as dependências no sistema operacional, podemos ter conflitos de versões.
- Com um ambiente virtual Python, podemos instalar as dependências de um projeto em um ambiente isolado. Isso evita
  conflitos de versões e mantém as dependências organizadas.
- O ambiente virtual Python é uma ferramenta muito útil para desenvolvedores, Python. Ele é amplamente utilizado na
  comunidade Python.
- Comandos Básicos do Ambiente Virtual:
    - Criar um ambiente virtual: `python -m venv venv`.
    - Ativar um ambiente virtual:
        - Windows: `venv\Scripts\activate`.
        - Linux: `source venv/bin/activate`.
        - macOS: `source venv/bin/activate`.
    - Desativar um ambiente virtual: `deactivate`.
- Quando se usa PyCharm Community não é necessário criar um ambiente virtual, pois o PyCharm cria um ambiente virtual
  para cada projeto automaticamente, ao criar um novo projeto Django. PyCharm é uma IDE desenvolvida pela JetBrains, que
  é muito popular.
- Desta forma, o PyCharm isola as dependências de cada projeto, evitando, conflitos de versões.

#### Exemplo básico de utilização do ambiente virtual e pip:

- Cria o diretório do projeto: `mkdir projeto`.
- Entra no diretório do projeto: `cd projeto`.
- Criar um ambiente virtual: `python -m venv venv`.
- Cria um arquivo main.py: `touch main.py`.
- Dentro do arquivo main.py, escreva o seguinte código:`from selenium import webdriver`
- Mas para usar o pacote selenium, precisamos instalar o pacote. Para isso, execute o comando: `pip install selenium`.
- Geralmente um projeto Python possui várias dependências. Para manter essas dependências organizadas, podemos criar um
- arquivo chamado requirements.txt na raiz do projeto.
- Poderia ser qualquer nome, mas é uma convenção usar requirements.txt na comunidade Python.
- pip freeze: Lista todas as dependências instaladas no ambiente virtual.
- Para gerar esse arquivo, execute o comando:
  `pip freeze > requirements.txt`. Esse comando irá gerar um arquivo chamado requirements.txt com todas as dependências
- Para instalar as dependências a partir do arquivo requirements.txt, execute o comando:
  `pip install -r requirements.txt`.

### 03 - Ambientação e Instalação (MacOS)

#### Instalação de Python -Django no MacOS
- O MacOS já vem com o Python instalado. Para verificar a versão do Python instalada, execute o comando:
  `python3 --version`.
- Para instalar o Django, execute o comando:
  `pip3 install django`.
- Para verificar a versão do Django instalada, execute o comando:
  `python3 -m django --version`.
- Para criar um projeto Django, execute o comando:
  `django-admin startproject nome_do_projeto`.
- Para criar um aplicativo Django, execute o comando:
  `python3 manage.py startapp nome_do_app`.
- Para rodar o servidor Django, execute o comando:
  `python3 manage.py runserver`.
- Para rodar o servidor Django em uma porta diferente, execute o comando:
  `python3 manage.py runserver 8080`.

#### Como usar o PyCharm Community para criar um projeto Django

- Abra o PyCharm Community.
- Clique em "Create New Project".
- Selecione "Django" na lista de templates.
- Selecione o diretório onde deseja criar o projeto.
- Selecione o ambiente virtual que deseja usar.
- Clique em "Create".


### 04 - Começando pelo começo

#### STRINGS EM PYTHON E SEUS MÉTODOS
- Strings são sequências de caracteres (cadeia de caracteres). Elas podem ser criadas usando aspas simples ou duplas.
  -   A   U   L   A     P  Y  C  O  D  E  B  R
  -   0   1   2   3  4  5  6  7  8  9  10 11 12
  - -13 -12 -11 -10 -9 -8 -7 -6 -5 -4  -3 -2 -1
```python
print('-'*30) # Resultado: ------------------------------
print('STRINGS NO PYTHON') # Resultado: STRINGS NO PYTHON
print('-'*30) # Resultado: ------------------------------
texto = 'AULA PYCODEBR'
print(texto)
print(type(texto))
print(texto[0])
print(texto[5:11]) # Pega do índice 5 ao 11, desconsiderando o 11
print(texto[0:3])  # Pega do índice 0 ao 3, desconsiderando o 3
print(texto[0:4])  # Pega do índice 0 ao 4, desconsiderando o 4
print(texto[5:])   # Pega do índice 5 até o final
print(texto[:5])   # Pega do início até o índice 5, desconsiderando o 5
```
- Funções úteis para strings:
```python
texto = 'AULA PYCODEBR'
print(texto)
print(type(texto))
print(texto[0])
print(texto[5:11])  # Pega do índice 5 ao 11, desconsiderando o 11
print(texto[0:3])  # Pega do índice 0 ao 3, desconsiderando o 3
print(texto[0:4])  # Pega do índice 0 ao 4, desconsiderando o 4
print(texto[5:])  # Pega do índice 5 até o final
print(texto[:5])  # Pega do início até o índice 5, desconsiderando o 5
print(len(texto))  # Tamanho da string
print(texto.count('A')) # Conta quantas vezes a letra 'A' aparece na string é case-sensitive
print(texto.count('a')) # Conta quantas vezes a letra 'A' aparece na string e é case-sensitive
print(texto.count('A', 0, 3)) # Conta quantas vezes a letra 'A' aparece na string entre os índices 0 e 3
print(texto.upper())  # Converte para maiúsculas
print(texto.lower())  # Converte para minúsculas
print(texto.capitalize())  # Converte para capitalizado, ou seja, a primeira letra maiúscula e o restante minúsculo
print(texto.title())  # Converte para capitalizado, ou seja, a primeira letra de cada palavra maiúscula
print(texto.split())  # Divide a string em uma lista de palavras
lista_de_palavras = texto.split()
print(lista_de_palavras)
print('_' .join(lista_de_palavras)) # Junta a lista de palavras em uma string, usando o underscore como separador
texto = '    AULA PYCODEBR    '
print(texto.strip())  # Remove os espaços em branco do início e do final da string
print(texto.rstrip())  # Remove os espaços em branco do final da string
print(texto.lstrip())  # Remove os espaços em branco do início da string
```








