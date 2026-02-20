salario=float(input('Qual é o salário do funcionário? R$'))
aumento1=salario+(salario*15/100)
aumento2= salario+(salario*10/100)
if salario == aumento1:
    print('O aumento do seu salário foi de {:.2f}'. format(aumento1))
else:
    print('O aumento do seu salário foi de {:.2f}'.format(aumento2))