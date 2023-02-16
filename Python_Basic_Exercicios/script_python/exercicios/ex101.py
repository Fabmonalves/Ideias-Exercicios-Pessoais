def voto(anos):
    """_summary_
    Args:
        anos (number): colocar idade para calcular se pode votart ou não
    """
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - nasc
    print('-=' *30)
    if  18 <= idade < 65 :
        return f'Com  {idade} anos, VOTO OBRIGATORIO!'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos, VOTO OPCIONAL!'
    elif idade < 16:
        return f'Com {idade} anos, NÂO VOTA.'
        
   
while True:
    nasc = int(input('Em que ano você nasceu? '))
    print(voto(nasc))
    resp = str(input('Deseja corrigir o ano? [S/N] ')).upper().strip()[0]
    while True:
        if resp not in 'SN':
            resp = str(input('Por favor, responder com S ou N: ')).upper().strip()[0]
        else:
            break
    
    if resp == 'N':
        print('-=' *30)
        print('FIM do programa!...')
        break
