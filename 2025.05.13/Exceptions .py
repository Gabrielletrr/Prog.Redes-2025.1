from logging import exception

import sys;

try:
    intDividendo= int(input("Digite o dividendo:"))
    intDivisor = int(input("Digite o divisor:"))
    fltResultado = intDividendo/intDivisor

except ValueError:
    print("ERRO:: informe um valor que possa ser convertido em inteiro")
except ZeroDivisionError:
    print("ERRO:Não existe divisão por 0.")
except:
    print(f'ERRO: {sys.exc_info()}')
else:
    print(fltResultado)
