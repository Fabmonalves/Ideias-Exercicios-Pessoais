def format_real(valor):
    tc_format = f"{float(valor):_.2f}".replace(".",",").replace("_",".")
    
    # a = f"{float(valor):,.2f}"
    # b = a.replace(",", "v")
    # c = b.replace(".", ",")
    return tc_format



valor1 = 6564165121356
valor2 = 76816614846

total = valor1 + valor2

print(format_real(total))