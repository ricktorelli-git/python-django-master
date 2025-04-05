print('-' * 30)  # Resultado: ------------------------------
print('STRINGS NO PYTHON')  # Resultado: STRINGS NO PYTHON
print('-' * 30)  # Resultado: ------------------------------
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
print(texto.count('A'))  # Conta quantas vezes a letra 'A' aparece na string é case-sensitive
print(texto.count('a'))  # Conta quantas vezes a letra 'A' aparece na string e é case-sensitive
print(texto.count('A', 0, 3))  # Conta quantas vezes a letra 'A' aparece na string entre os índices 0 e 3
print(texto.upper())  # Converte para maiúsculas
print(texto.lower())  # Converte para minúsculas
print(texto.capitalize())  # Converte para capitalizado, ou seja, a primeira letra maiúscula e o restante minúsculo
print(texto.title())  # Converte para capitalizado, ou seja, a primeira letra de cada palavra maiúscula
print(texto.split())  # Divide a string em uma lista de palavras
lista_de_palavras = texto.split()
print(lista_de_palavras)
print('_'.join(lista_de_palavras))  # Junta a lista de palavras em uma string, usando o underscore como separador
texto = '    AULA PYCODEBR    '
print(texto.strip())  # Remove os espaços em branco do início e do final da string
print(texto.rstrip())  # Remove os espaços em branco do final da string
print(texto.lstrip())  # Remove os espaços em branco do início da string
print(texto.find('A'))  # Encontra a posição da letra 'A' na string é case-sensitive
print(texto.find('a'))  # Encontra a posição da letra 'a' na string é case-sensitive
