a = float(input('Digite a medida do lado A do triangulo em cm: '))
b = float(input('Digite a medida do lado B do triangulo em cm: '))
c = float(input('Digite a medida do lado C do triangulo em cm: '))

if a < b + c and b < a + c and c < a + b:
        print('Os lador formam um Triangulo')     
else: 
    print('Os lados não formam um Triangulo')
print ('---FIM---')
