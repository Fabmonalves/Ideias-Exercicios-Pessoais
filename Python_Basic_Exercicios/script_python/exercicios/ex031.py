km = float(input('Digite a Distancia da viagem em KM: '))
if km > 200:
    print('Viagem de {}Km rodados, total a pagar é de {:.2f}'.format(km, km * 0.45))
else:
    print('Viagem de {}Km rodados, total a pagar é de {:.2f}'.format(km, km * 0.50))
print('---FIM---')