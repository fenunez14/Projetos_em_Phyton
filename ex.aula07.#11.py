l=float(input('Largura da parede: '))
a=float(input('Altura da parede: '))
area=l*a
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(l,a,area))
tinta=area/2
print('Para pintar essa parede, você precisará de {} litros de tinta'.format(tinta))