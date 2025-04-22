import mysql.connector

# Criando a conexão -> adicionar as infromações do seu banco de dados
connection = mysql.connector.connect(
    host = '',
    user='',
    password='',
    database=''
)
cursor = connection.cursor()

# Criando a tabela utilizada nas consultas
# comando = CREATE TABLE `pi_entradas_sustentabilidade` ('id' int NOT NULL AUTO_INCREMENT, 'data_registro' date NOT NULL, 'consumo_agua' float NOT NULL, 'consumo_energia' float NOT NULL, 'pct_lixo' float NOT NULL, 'transporte_publico' varchar(1) NOT NULL, 'bicicleta' varchar(1) NOT NULL, 'caminhada' varchar(1) NOT NULL, 'carro_comb_fossil' varchar(1) NOT NULL, 'carro_eletrico' varchar(1) NOT NULL, 'carona' varchar(1) NOT NULL, PRIMARY KEY ('id'))
# cursor.execute(comando)
# connection.commit()

# Exibição dos dados armazenados
comando = 'SELECT * FROM pi_entradas_sustentabilidade'
cursor.execute(comando)
resultado = []
resultado = cursor.fetchall() # lê o banco de dados -> apenas para selects
print('\nExibição dos dados de inserção:\n')
print('-'*162)
print('| ID | Data de registro | Consumo de água | Consumo de energia | Quantidade de lixo gerado | % de lixo reciclável gerado | Transportes utilizados\t\t |')
print('-'*162)
for i in range(len(resultado)):
    print(f'  {resultado[i][0]}', end='\t')
    print(resultado[i][1], end='\t   ')
    print(f'{resultado[i][2]} L', end='\t\t')
    print(f'{resultado[i][3]} KwH', end='\t\t\t')
    print(f'{resultado[i][4]} Kg', end='\t\t\t')
    print(f'{resultado[i][5]}%', end='\t\t\t\t')
    print(resultado[i][6:12])
print('-'*162)

# Exibição da classificação dos registros
comando = 'SELECT * FROM pi_classificacoes_sustentabilidade'
cursor.execute(comando)
resultado_class = []
resultado_class = cursor.fetchall()
print('\nExibição da classificação dos dados armazenados:\n')
print('-'*162)
print('| ID | Consumo de água\t\t| Consumo de energia\t\t| % de lixo reciclável gerado\t| Transportes utilizados\t|')
print('-'*162)
for i in range(len(resultado_class)):
    print(f'  {resultado_class[i][0]}', end='\t')
    print(resultado_class[i][1], end='\t   ')
    print(resultado_class[i][2], end='\t   ')
    print(resultado_class[i][3], end='\t   ')
    print(resultado_class[i][4])
print('-'*162)

# Processamento dos dados armazenados
print('\nProcessamento dos dados armazenados:\n')
print('-'*162)
print('Média dos dados coletados')
print('-'*162)

# Água
comando = 'SELECT avg(consumo_agua) FROM pi_entradas_sustentabilidade'
cursor.execute(comando)
media_agua = cursor.fetchone()
print(f'Média do consumo de água: {media_agua[0]:.2f} L')

if (media_agua[0] >= 150):
    if (media_agua[0] > 200):
        print("Classificação do consumo de água: Baixa sustentabilidade")
    else:
        print("Classificação do consumo de água: Moderada sustentabilidade")
else:
    print("Classificação do consumo de água: Alta sustentabilidade")
print('\n')

# Energia
comando = 'SELECT avg(consumo_energia) FROM pi_entradas_sustentabilidade'
cursor.execute(comando)
media_energia = cursor.fetchone()

print(f'Média do consumo de energia: {media_energia[0]:.2f} kwH')
if (media_energia[0] >= 5): 
    if (media_energia[0] > 10):
        print("Classificação do consumo de energia: Baixa sustentabilidade")
    else: 
        print("Classificação do consumo de energia: Moderada sustentabilidade")
else:
    print("Classificação do consumo de energia: Alta sustentabilidade")   
print('\n')

#Porcentagem
comando = 'SELECT avg(pct_lixo) FROM pi_entradas_sustentabilidade'
cursor.execute(comando)
media_lixo = cursor.fetchone()
print(f'Média da porcentagem de lixo reciclável gerado: {media_lixo[0]:.2f}%')

if (media_lixo[0] <= 50):
    if (media_lixo[0] < 20):
        print("Classificação da geração de resíduos recicláveis: Baixa sustentabilidade")
    else:
        print("Classificação da geração de resíduos recicláveis: Moderada sustentabilidade")
else:
    print("Classificação da geração de resíduos recicláveis: Alta sustentabilidade")
print('\n')

# Tipos de transporte
comando = 'SELECT transporte_publico, bicicleta, caminhada, carro_comb_fossil, carro_eletrico, carona FROM pi_entradas_sustentabilidade'
cursor.execute(comando)
dados_transporte = class_transporte = []
dados_transporte = cursor.fetchall()
# Conversão das letras de cada linha em classificação (1 - alta; 2 - moderada; 3 - baixa)
for i in range(2, len(dados_transporte)-1):
    if dados_transporte[i][0] == 'S' or dados_transporte[i][1] == 'S' or dados_transporte[i][2] == 'S' or dados_transporte[i][4] == 'S':
        if dados_transporte[i][3] == 'S' or dados_transporte[i][5] == 'S':
            class_transporte.append(2)
        else:
            class_transporte.append(1)
    else:
            class_transporte.append(3)

print('Média da classificação de transportes: ', end='')
# Análise dos dados convertidos
if (not 3 in class_transporte) and (not 2 in class_transporte):
    print('Alta sustentabilidade')
elif (not 1 in class_transporte) and (not 2 in class_transporte):
    print('Baixa sustentabilidade')
else:
    print('Moderada sustentabilidade')
print('-'*162)

cursor.close()
connection.close()