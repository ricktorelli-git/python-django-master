print('-' * 30)  # Resultado: ------------------------------
print('STRINGS NO PYTHON')  # Resultado: STRINGS NO PYTHON
print('-' * 30)  # Resultado: ------------------------------
texto = 'AULA PYCODEBR'
print(texto)
print(type(texto))
print(texto[0])
print(texto[5:13])  # Pega do índice 5 ao 13, desconsiderando o 13
print(texto[5:11])  # Pega do índice 5 ao 11, desconsiderando o 11
print(texto[:4]) # Pega do início até o índice 4, desconsiderando o 4
print('_' * 30)  # Resultado: ________________________________
print('FUNÇÕES DE STRINGS')  # Resultado: FUNÇÕES DE STRINGS
print('-' * 30)
print(len(texto))  # Tamanho da string
print(texto.count('A'))  # Conta quantas vezes a letra 'A' aparece na string é case-sensitive
print(texto.count('a'))  # Conta quantas vezes a letra 'A' aparece na string e é case-sensitive
print(texto.count('A', 0, 3))  # Conta quantas vezes a letra 'A' aparece na string entre os índices 0 e 3
print(texto.find('AULA'))  # Encontra a primeira ocorrência da string 'AULA' e retorna o índice
print(texto.find('PYCODEBR'))  # Encontra a primeira ocorrência da string 'PYCODEBR' e retorna o índice
print(texto.upper())  # Converte para maiúsculas
print(texto.lower())  # Converte para minúsculas
print(texto.capitalize())  # Converte para capitalizado, ou seja, a primeira letra maiúscula e o restante minúsculo
print(texto.title())  # Converte para capitalizado, ou seja, a primeira letra de cada palavra maiúscula
print(texto.split())  # Divide a string em uma lista de palavras
lista_texto = texto.split()
''.join(lista_texto)
texto2 = '   AULA PYCODEBR   '
print(texto2)
print(texto2.strip())  # Remove os espaços em branco no início e no final da string
print(texto2.rstrip())  # Remove os espaços em branco no final da string
print(texto2.lstrip())  # Remove os espaços em branco no início da string
print(texto2.replace('AULA', 'AULÃO'))  # Substitui a string 'AULA' por 'AULÃO'
print(texto2)  # A string original não é alterada


