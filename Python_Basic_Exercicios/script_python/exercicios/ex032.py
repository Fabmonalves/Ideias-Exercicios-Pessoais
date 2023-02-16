import datetime
ano = int(input('Digite o ano: , OBS, se digitar zeroi será analizado o ano atual '))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é um ano bissexto!'.format(ano))
else:
    print('O ano {} NÂO é um ano bisssexto!'.format(ano))

