import math

angulo= float(input('Digite um angulo: '))

radianos = math.radians(angulo)

print('O ângulo digitado é {}º. Seno:{:.2f} , cosseno {:.2f}  e tang {:.2f}'.format(angulo,math.sin(radianos),math.cos(radianos), math.tan(radianos)))