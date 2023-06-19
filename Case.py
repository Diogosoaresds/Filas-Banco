import random
import statistics

clientes = random.randint(3, 11)

fila1 = []
fila2 = []
fila3 = []
fila4 = []

soma = 0

print(clientes)

while soma < (clientes / 4):
    fila1.append(int(input('Senha: ')))
    fila2.append(int(input('Senha: ')))
    fila3.append(int(input('Senha: ')))
    fila4.append(int(input('Senha: ')))
    soma = soma + 1

if (clientes / 4) == 0.75:
    fila4.clear()

if (clientes / 4) == 1.25:
    del fila2[1]
    del fila3[1]
    del fila4[1]

if (clientes / 4) == 1.5:
    del fila3[1]
    del fila4[1]

if (clientes / 4) == 1.75:
    del fila4[1]

if (clientes / 4) == 2.25:
    del fila2[2]
    del fila3[2]
    del fila4[2]

if (clientes / 4) == 2.5:
    del fila3[2]
    del fila4[2]

if (clientes / 4) == 2.75:
    del fila4[2]

soma = 0

print('Fila 1: ', fila1)
print('Fila 2: ', fila2)
print('Fila 3: ', fila3)
print('Fila 4: ', fila4)

mediaf1 = []
mediaf2 = []
mediaf3 = []
mediaf4 = []

calculof1 = 0
calculof2 = 0
calculof3 = 0
calculof4 = 0

Atendimento1 = random.randint(5, 15)
Atendimento2 = random.randint(5, 15)
Atendimento3 = random.randint(5, 15)



for x in fila1:
  mediaf1.append(Atendimento1)
if len(fila1) == 2 or len(fila1) == 3:
    mediaf1.pop(1)
    calculof1 = (Atendimento1) + (Atendimento2)
    mediaf1.append(calculof1)
if len(fila1) == 3:
    mediaf1.pop(1)
    calculof1 = (Atendimento1) + (Atendimento2) + (Atendimento3)
    mediaf1.append(calculof1)
Mmediaf1=statistics.mean(mediaf1)

print(mediaf1)
print('A media da fila 1 é: ', Mmediaf1)
print('Foram atendidos: ', len(fila1), 'Cliente(s)')

soma = 0

Atendimento4 = random.randint(5, 15)
Atendimento5 = random.randint(5, 15)
Atendimento6 = random.randint(5, 15)



for x in fila2:
  mediaf2.append(Atendimento4)

if len(fila2) == 2 or len(fila2) == 3:
    mediaf2.pop(1)
    calculof2 = (Atendimento5) + (Atendimento4)
    mediaf2.append(calculof2)

if len(fila2) == 3:
    mediaf2.pop(1)
    calculof2 = Atendimento5 + Atendimento4 + Atendimento6
    mediaf2.append(calculof2)
Mmediaf2=statistics.mean(mediaf2)

print(mediaf2)
print('A media da fila 2 é: ', Mmediaf2)
print('Foram atendidos: ', len(fila2), 'Cliente(s)')

soma = 0

Atendimento7 = random.randint(5, 15)
Atendimento8 = random.randint(5, 15)
Atendimento9 = random.randint(5, 15)



for x in fila3:
  mediaf3.append(Atendimento7)
if len(fila3) == 2 or len(fila3) == 3:
    mediaf3.pop(1)
    calculof3 = (Atendimento8) + (Atendimento7)
    mediaf3.append(calculof3)
if len(fila3) == 3:
    mediaf3.pop(1)
    calculof3 = Atendimento8 + Atendimento7 + Atendimento9
    mediaf3.append(calculof3)
Mmediaf3=statistics.mean(mediaf3)

print(mediaf3)
print('A media da fila 3 é: ', Mmediaf3)
print('Foram atendidos: ', len(fila3), 'Cliente(s)')

soma = 0

Atendimento10 = random.randint(5, 15)
Atendimento11 = random.randint(5, 15)
Atendimento12 = random.randint(5, 15)



Mmediaf4=0

for x in fila4:
  mediaf4.append(Atendimento10)
  Mmediaf4 = statistics.mean(mediaf4)

if len(fila4) == 2 or len(fila4) == 3:
    mediaf4.pop(1)
    calculof4 = (Atendimento11) + (Atendimento10)
    mediaf4.append(calculof4)
    Mmediaf4 = statistics.mean(mediaf4)

if len(fila4) == 3:
    mediaf4.pop(1)
    calculof4 = Atendimento10 + Atendimento11 + Atendimento12
    mediaf4.append(calculof4)
    Mmediaf4=statistics.mean(mediaf4)

print(mediaf4)
print('A media da fila 4 é: ', Mmediaf4)
print('Foram atendidos: ', len(fila4), 'Cliente(s)')

soma = 0