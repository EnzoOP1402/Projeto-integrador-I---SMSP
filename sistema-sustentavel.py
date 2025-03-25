#Cabeçalho

print("="*5, end=' ')
print("SISTEMA DE MONITORAMENTO DE SUSTENTABILIDE PESSOAL", end=' ')
print("="*5)

#Inserção das informações iniciais

data = str(input("\nInforme a data de hoje (DD/MM/AAAA): "))

consumo_agua = float(input("\nInforme o quanto de água você consumiu hoje (Aprox., em Litros): "))

consumo_energia = float(input("\nInforme quanto de energia elétrica você consumiu hoje (em kWh): "))

residuos_nao_reciclaveis = float(input("\nInforme quantos Kg de resíduos não recicláveis você produziu hoje: ")) 

residuos_reciclaveis = float(input("\nInforme a porcentagem de resíduos recicláveis que você gerou hoje: "))

#Inserção e validação inicial dos dados de transporte

print("Indique quais meios de transporte foram utilizados por você hoje\n")

while True:
    transporte_publico = str(input("Transporte público (ônibus, metrô ou trem) [S/N]\n>> ")).upper()
    if transporte_publico == 'S' or transporte_publico == 'N':
        break
    else:
        print("Resposta inválida\n")

while True:
    bicicleta = str(input("Bicicleta [S/N]\n>> ")).upper()
    if bicicleta == 'S' or bicicleta == 'N':
        break
    else:
        print("Resposta inválida\n")
        
while True: 
    caminhada = str(input("Caminhada [S/N]\n>> ")).upper()
    if caminhada == 'S' or caminhada == 'N':
        break
    else:
        print("Resposta inválida\n")

while True:
    carro_combustivel = str(input("Carro (combustível fóssil)? [S/N]\n>> ")).upper()
    if carro_combustivel == 'S' or carro_combustivel == 'N':
        break
    else:
        print("Resposta inválida\n")

while True:
    carro_eletrico = str(input("Carro elétrico? [S/N]\n>> ")).upper()
    if carro_eletrico == 'S' or carro_eletrico == 'N':
        break
    else:
        print("Resposta inválida\n")

while True:
    carona_compartilhada = str(input("Carona compartilhada (combustível fóssil) [S/N]\n>> ")).upper()
    if carona_compartilhada == 'S' or carona_compartilhada == 'N':
        break
    else:
        print("Resposta inválida\n")


#Verificação de sustentabilidade

print("\n")
print("="*5, end=' ')
print("RESULTADOS", end=' ')
print("="*5)

#Consumo de água
if (consumo_agua >= 150):
    if (consumo_agua > 200):
        print("Consumo de água: Baixa sustentabilidade")
    else:
        print("Consumo de água: Moderada sustentabilidade")
else:
    print("Consumo de água: Alta sustentabilidade")

#Consumo de energia

if (consumo_energia >= 5): 
    if (consumo_energia > 10):
        print("Consumo de energia: Baixa sustentabilidade")
    else: 
        print("Consumo de energia: Moderada sustentabilidade")
else:
    print("Consumo de energia: Alta sustentabilidade")    

#Geração de lixos não reciclaveis

if (residuos_reciclaveis <= 50):
    if (residuos_reciclaveis < 20):
        print("Geração de resíduos recicláveis: Baixa sustentabilidade")
    else:
        print("Geração de resíduos recicláveis: Moderada sustentabilidade")
else:
    print("Geração de resíduos recicláveis: Alta sustentabilidade")

#Meiosdetransporte

if bicicleta=='S' or transporte_publico=='S' or caminhada=='S' or carro_eletrico=='S':
    if carro_combustivel=='S' or carona_compartilhada=='S':
        print('Uso de transportes: Moderada sustentabilidade')
    else:
        print('Uso de transportes: Alta sustentabilidade')
else:  
    print('Uso de transportes: Baixa sustentabilidade')
  
    