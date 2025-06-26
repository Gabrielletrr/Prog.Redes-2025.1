'''
   Fazer um programa que:
   
      1) Solicite ao usuário um valor inteiro N positivo (valor máximo para N -> 100);
   
      2) Gere uma lista com N valores inteiros aleatórios entre 0 e 1.000 (inclusive)
         sem repetições;

      3) A partir da lista gerada, gere uma segunda uma lista com as raízes quadradas 
         dos valores da lista anterior;
'''

import sys, random

try:

    n = int(input('Digite um número positivo, inteiro e até 100: '))

except ValueError:
    sys.exit('Você digitou um caractere!')
except Exception as e:
   sys.exit(f'ERRO: {e}')

else:
    if n < 0 and n > 100:
        sys.exit('Digite um numero maior que 0 e que seja até 100...')

lista_sorteio = list()
lista_raiz = list()

i = 1
while i <= n:
   sorteio = random.randint(0, 1000)
   if sorteio not in lista_sorteio:
      lista_sorteio.append(sorteio)
      i += 1
      raiz_quadrada = sorteio ** 0.5
      lista_raiz.append(raiz_quadrada)
print(f'Números sorteados {lista_sorteio}')
print(f'Raiz quadrada dos números {lista_raiz}')
