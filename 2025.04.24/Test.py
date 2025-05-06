a=input("digite um valor para a:")
b=input("digite um valor para b:")

try:
    result=int(a)/int(b)

except ZeroDivisionError:
    print("ERRO: não é possível dividir por zero")

else:
    print(result)
    