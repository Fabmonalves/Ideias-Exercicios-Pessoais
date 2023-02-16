def leiaDinheiro(msg):
    while True:
        num = str(input(msg)).strip().replace(',','.')
        while num.isalpha()  or num.strip() == '':
            print('\033[31mERRO!, digite um numero válido!\033[m')
            num = str(input(msg)).strip().replace(',','.')
        if not num.isalpha():
            num = float(num)
            break
    return num