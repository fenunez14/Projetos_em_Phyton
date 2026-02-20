from random import randint
from time import sleep
computador =randint(0,5)#Faz o computador "pensar"
print('-=-'*20)
print('Vou pensar em número de 0 a 5. *TENTE ADIVINHAR*')
print('-=-'*20)
jogador= int(input('Em que número eu pensei? '))#Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)
if jogador==computador:
    print('Parabéns, você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}'.format(computador, jogador))
