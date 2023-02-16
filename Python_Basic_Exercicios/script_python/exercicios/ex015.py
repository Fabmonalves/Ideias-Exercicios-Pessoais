dias = int(input('Quantos dias esteve com o carro? '))
km = float(input('Quantos KM rodados? '))
total = (dias * 60) + (km * 0.15)
print(' O total a pagar é de R${:.2f}'.format(total))
