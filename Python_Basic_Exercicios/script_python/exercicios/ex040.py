print('-=-' * 20)
print('Boletim escolar')
print('-=-' * 20)

p = float(input('Digite sua nota de Português: '))
m = float(input('Digite sua nota de Matemática: '))
media = (p + m) / 2

if media < 5:
    print('Lamento, sua média é {:.1f}, esta \033[31mREPROVADO\033[m'.format(media))
elif media >= 5 and media <= 6.9:
    print('Sua média é {:.1f}, esta de \033[33mRECUPERAÇÂO\033[m'.format(media))
elif media >= 7:
    print('Parabéns, sua média é {:.1f}, você esta \033[32mAPROVADO\033[m'.format(media))
