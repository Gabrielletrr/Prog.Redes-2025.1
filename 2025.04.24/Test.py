#Teste

a = input("Digite valor de a:")
b = input("Digite valor de b:")

try: 
    resultado = int(a)/int(b)

except ZerodivisionErro:
    print('erro')

except Excepition as e:
    print(f'erro:{e}')

else:
    print("result",resultado)
