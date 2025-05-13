 #Programa para classificar um triângulo quanto aos ângulos.

   #- O programa deverá solicitar 3 ângulos inteiros positivos;
   #- Para ser um triânguloa, a soma dos ângulos deve ser igual a 180;
   
   #- Retângulo: Possui um ângulo interno reto (igual a 90).
   #- Obtusângulo: Possui um ângulo interno obtuso (maior que 90).
   #- Acutângulo: Possui todos os ângulos internos agudos (menores que 90).

import sys

ang1=int(input("Digite o 1° ângulo:"))

ang2=int(input("Digite o 2° ângulo:"))

ang3=int(input("Digite o 3° ângulo:"))

if (ang1 <= 0 ) or (ang2 <= 0) or (ang3 <=0 ):
  sys.exit('ERRO: Um ou mais ãngulos não são positivos')

if ang1 + ang2 + ang3 != 180:
  sys.exit('ERRO: A soma dos ãngulos deve ser 180')

if ang1 == 90 or ang2 == 90 or ang3 == 90:
  print("O triângulo é retângulo")

elif ang1 > 90 or ang2 > 90 or ang3 > 90:
  print("O triângulo é obtusângulo")

else:
  print("Acutângulo")

