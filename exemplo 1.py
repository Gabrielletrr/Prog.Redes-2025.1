'''
   Fazer um programa que:
   
      1) Solicite ao usuário um valor inteiro N positivo (valor máximo para N -> 100);

      2) Gere uma lista com N valores inteiros aleatórios entre -100 e +100;
   
      3) A partir da lista gerada, gere uma segunda uma lista apenas com os 
         números pares da lista;
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
lista_par = []

for _ in range(n):
    sorteio = random.randint(-100, 100)
    lista_sorteio.append(sorteio)
    if sorteio % 2 == 0:
        lista_par.append(sorteio)
print(f'Numeros sorteados {lista_sorteio}')
print(f'Numeros pares do sorteio {lista_par}')
