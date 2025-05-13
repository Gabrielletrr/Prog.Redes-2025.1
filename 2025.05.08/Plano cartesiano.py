#Programa para informar em qual quadrante cartesiano o ponto está.

  # - O programa deverá solicitar as duas coordenadas (x,y) de um ponto;

   #- O ponto está no 1º quadrante quando X e Y forem positivos;
   #- O ponto está no 2º quadrante quando X for negativo e Y for positivo;
   #- O ponto está no 3º quadrante quando X e Y forem negativos;
   #- O ponto está no 4º quadrante quando X for positivo e Y for negativo;

x=input("Digite o ponto X:")
y=input("Digite o ponto y:")

if float(x)>0 and float(y) > 0:
    print("Os pontos estão no 1° quadrante")

elif float(x)<0 and float(y) > 0:
    print("Os pontos estão no 2° quadrante")

elif float(x) < 0 and float(y) < 0:
    print("Os pontos estão no 3° quadrante")

else:
    print("Os pontos estão no 4° quadrante")

 
