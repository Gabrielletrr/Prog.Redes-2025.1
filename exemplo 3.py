'''
   Fazer um programa que:
   
      1) Solicite ao usuário um valor inteiro N positivo (valor máximo para N -> 100);

      2) Gere uma lista com N valores inteiros aleatórios entre -100 e +100;
   
      3) A partir da lista gerada, gere uma segunda uma lista onde cada posição será 
         uma sub-lista com 3 posições:

         a) A primeira posição será o número anterior ao número da lista inicial;
         b) A segunda posição será o número da lista inicial; 
         c) A terceira posição será o número seguinte ao númerio da lista inicial.
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

lista_sorteio = []
lista_antecessor_sucessor = []

for _ in range(n):
    sorteio = random.randint(-100, 100)
    lista_sorteio.append(sorteio)
    antecessor_sucessor = [sorteio - 1, sorteio, sorteio + 1]
    lista_antecessor_sucessor.append(antecessor_sucessor)
print(f'Numeros sorteados {lista_sorteio}')
print(f'Numeros sorteados {lista_antecessor_sucessor}')
    
