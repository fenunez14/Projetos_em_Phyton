s=float(input('Qual o seu salário? R$'))
novo=s+(s*15/100)
print('O salário anterior que era de R${:.2f}, com o aumento de 15%, passou a ser de R${:.2f}'.format(s,novo))