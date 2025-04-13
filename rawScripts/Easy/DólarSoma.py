Valores = [6.03, 6.07, 6.14, 6.02, 6.01, 6.07, 6.09, 6.18, 6.20, 6.21, 6.23, 6.30, 6.31, 6.32, 6.09, 6.13]
ComprasEVendas = [202.25, -2.50, -3, 5.50, 827.44, -5, -3, -23, -1, -2, -3, -10, -11, -2, 60, -30]
counter = 0
ValoresDolar = []
for Dolar in Valores:
    counter += 1
    Exchange = ComprasEVendas[counter -1]
    ValoresDolar.append(Exchange / Dolar)
print(ValoresDolar)
DolarAtual = float(input('Insira o valor atual do dólar: '))
Somatório = 0
for i in ValoresDolar:
    Somatório += i
ValorFinalDoReal = Somatório * DolarAtual
print(f'O valor final(Reais) é: {ValorFinalDoReal}.')