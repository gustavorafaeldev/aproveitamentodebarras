todasmedidas = []
medidas = list()
listaaproveitamento = dict()
listaaproveitamento2 = list()

def calculaaproveitamento():
    maior = 0
    saldo = 6000
    while len(todasmedidas) > 0:
        continua = False
        for med in todasmedidas:
            if med > maior and med <= saldo:
                maior = med
        if maior > 0:
            medidas.append(maior)
            todasmedidas.remove(maior)
            saldo -= maior
            maior = 0
            continua = True
        if continua == False or len(todasmedidas) == 0:
            listaaproveitamento['medidas'] = (medidas.copy())
            listaaproveitamento['soma'] = 6000 - (sum(medidas))
            listaaproveitamento2.append(listaaproveitamento.copy())
            medidas.clear()
            saldo = 6000


while True:
    medida = int(input('Digite a medida: '))
    todasmedidas.append(medida)
    resp = str(input('Deseja informar outra medida? S/N ')).upper()[0]
    if resp in 'N':
        break

calculaaproveitamento()
print('-' * 40)
print('CÁLCULO DE APROVEITAMENTO DE BARRA')
print('-' * 40)

cont = 0
for item in listaaproveitamento2:
    cont += 1
    medidas, sobra = item.values()
    print(f'{cont}° Barra, medidas para corte => {medidas}, sobra do alumínio {sobra}mm')