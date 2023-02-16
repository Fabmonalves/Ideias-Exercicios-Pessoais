palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for i in palavras:
    print(f'\nNa palavra {i} temos ', end = '' )
    for vogais in i:
        if vogais.lower() in 'aeiou':
            print(vogais.lower(), end = ' ')