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
print("Exibição dos dados das tabelas: ")
print('-'*121)
print('| ID | Data de registro | Consumo de água | Consumo de energia | % de lixo reciclável gerado | Transportes utilizados   |')
print('-'*121)
for i in range(len(resultado)):
    print(f'  {resultado[i][0]}', end='\t')
    print(resultado[i][1], end='\t   ')
    print(f'{resultado[i][2]} L', end='\t\t')
    print(f'{resultado[i][3]} KwH', end='\t\t\t')
    print(f'{resultado[i][4]}%', end='\t\t\t')
    print(resultado[i][5:10])

# Processamento dos dados armazenados
print('\n')
print('-'*121)
print('Média dos dados coletados')
print('-'*121)

# Água
comando = 'SELECT avg(consumo_agua) FROM pi_entradas_sustentabilidade'
cursor.execute(comando)
media_agua = cursor.fetchone()
print(f'Média do consumo de água: {media_agua[0]:.2f} L')

# Energia
comando = 'SELECT avg(consumo_energia) FROM pi_entradas_sustentabilidade'
cursor.execute(comando)
media_energia = cursor.fetchone()
print(f'Média do consumo de energia: {media_energia[0]:.2f} kwH')

#Porcentagem
comando = 'SELECT avg(pct_lixo) FROM pi_entradas_sustentabilidade'
cursor.execute(comando)
media_lixo = cursor.fetchone()
print(f'Média da porcentagem de lixo reciclável gerado: {media_lixo[0]:.2f}%')

# Tipos de transporte
comando = 'SELECT transporte_publico, bicicleta, caminhada, carro_comb_fossil, carro_eletrico, carona FROM pi_entradas_sustentabilidade'
cursor.execute(comando)
dados_transporte = class_transporte = []
dados_transporte = cursor.fetchall()
# Conversão das letras de cada linha em classificação (1 - alta; 2 - moderada; 3 - baixa)
for i in range(len(dados_transporte)):
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
elif ((not 1 in class_transporte) and (not 3 in class_transporte)) or ((1 in class_transporte) and ((2 in class_transporte) or (3 in class_transporte))):
    print('Moderada sustentabilidade')
elif (not 1 in class_transporte) and (not 2 in class_transporte):
    print('Baixa sustentabilidade')


cursor.close()
connection.close()