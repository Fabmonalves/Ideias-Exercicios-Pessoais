preco = float(input('Digite o preço do produto: '))
desconto = float(input('Digite o valor em desconto que a loja te ofereçe: '))
final = preco - (preco*desconto / 100) 
input(' O produto do valor {} com o desconto de {} fica {}'.format(preco, desconto, final))