#Programa para calcular a distância entre dois pontos no plano cartesiano.

 # - O programa deverá solicitar as duas coordenadas (xA,yA) do ponto A;
 # - O programa deverá solicitar as duas coordenadas (xB,yB) do ponto B;

 # - Calcular a distância entre os pontos (qual fórmula usar????)

  #d = √((x2 - x1)² + (y2 - y1)²)

x1=float(input("Digite o ponto x1:"))
y1=float(input("Digite o ponto y1:"))
x2=float(input("Digite o ponto x2:"))
y2=float(input("Digite o ponto y2:"))

Distancia = ((x2 - x1)**2 + (y2 - y1)**2) ** (1/2)

print(f'A distância entre os pontos são de {Distancia:.2f}')