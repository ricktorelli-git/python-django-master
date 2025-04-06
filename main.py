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
print('-' * 30)  # Resultado: ------------------------------
print('OPERADORES LÓGICOS NO PYTHON')   # Resultado: OPERADORES LÓGICOS NO PYTHON
print('-' * 30)  # Resultado: ------------------------------
a = True
b = False

if a and b:
    print('A e B são verdadeiros')
else:
    print('Não atende a condição')

if a or b:
    print('A ou B são verdadeiros')
else:
    print('Não atende a condição')
print('-' * 30)  # Resultado: ------------------------------
a = True
b = True

if a and b:
    print('A e B são verdadeiros')
else:
    print('Não atende a condição')
if a or b:
    print('A ou B são verdadeiros')
else:
    print('Não atende a condição')

print('-' * 30)  # Resultado: ------------------------------
idade = 25
nome = 'Felipe'

if idade >= 18 and nome == 'Felipe':
    print('Você é maior de idade e se chama Felipe')
else:
    print('Você não atende a condição')
if idade >= 18 or nome == 'Felipe':
    print('Você é maior de idade ou se chama Felipe')
else:
    print('Você não atende a condição')
print('-' * 30)  # Resultado: ------------------------------
if idade == 25: # Verifica se a idade é igual a 25
    print('Você tem 25 anos')
else:
    print('Você não tem 25 anos')
print('-' * 30)  # Resultado: ------------------------------

if idade != 25: # Verifica se a idade é diferente de 25
    print('Você não tem 25 anos')
else:
    print('Você tem 25 anos')
print('-' * 30)  # Resultado: ------------------------------
if nome == 'Felipe' and idade == 25: # Verifica se o nome é Felipe e a idade é 25
    print('Você se chama Felipe e tem 25 anos')
else:
    print('Você não se chama Felipe ou não tem 25 anos')
print('-' * 30)  # Resultado: ------------------------------
peso = 90
if (nome == 'Felipe' or idade == 25) and peso == 90: # Verifica se o nome é Felipe ou a idade é 25 e o peso é 90
    print('Você se chama Felipe ou tem 25 anos e pesa 90 kg')
else:
    print('Você não se chama Felipe ou não tem 25 anos ou não pesa 90 kg')
print('-' * 30)  # Resultado: ------------------------------
print('OPERADORES ARITMÉTICOS EM PYTHON')  # Resultado: OPERADORES ARITMÉTICOS EM PYTHON
print('-' * 30)  # Resultado: ------------------------------
a = 10
b = 5
print(a + b)  # Soma
print(a - b)  # Subtração
print(a * b)  # Multiplicação
print(a / b)  # Divisão
print(a // b)  # Divisão inteira
print(a % b)  # Resto da divisão
print(a ** b)  # Potência
print('-' * 30)  # Resultado: ------------------------------
print('CALCULADORA')  # Resultado: CALCULADORA
print('-' * 30)  # Resultado: ------------------------------
print('Escolha uma operação:')  # Resultado: Escolha uma operação:
print('1 - Soma')  # Resultado: 1 - Soma
print('2 - Subtração')  # Resultado: 2 - Subtração
print('3 - Multiplicação')  # Resultado: 3 - Multiplicação
print('4 - Divisão')  # Resultado: 4 - Divisão
print('5 - Divisão inteira')  # Resultado: 5 - Divisão inteira
print('6 - Resto da divisão')  # Resultado: 6 - Resto da divisão
print('7 - Potência')  # Resultado: 7 - Potência
print('8 - Sair')  # Resultado: 8 - Sair
opcao = int(input('Escolha uma opção: '))  # Resultado: Escolha uma opção:
if opcao == 1:
    print('Você escolheu soma')
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))
    print(f'O resultado da soma é {a + b}')
elif opcao == 2:
    print('Você escolheu subtração')
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))
    print(f'O resultado da subtração é {a - b}')
elif opcao == 3:
    print('Você escolheu multiplicação')
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))
    print(f'O resultado da multiplicação é {a * b}')
elif opcao == 4:
    print('Você escolheu divisão')
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))
    print(f'O resultado da divisão é {a / b}')
elif opcao == 5:
    print('Você escolheu divisão inteira')
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))
    print(f'O resultado da divisão inteira é {a // b}')
elif opcao == 6:
    print('Você escolheu resto da divisão')
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))
    print(f'O resultado do resto da divisão é {a % b}')
elif opcao == 7:
    print('Você escolheu potência')
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))
    print(f'O resultado da potência é {a ** b}')
elif opcao == 8:
    print('Você escolheu sair')
else:
    print('Opção inválida')
print('-' * 30)  # Resultado: ------------------------------
print('FIM DO PROGRAMA')  # Resultado: FIM DO PROGRAMA
print('-' * 30)  # Resultado: ------------------------------



