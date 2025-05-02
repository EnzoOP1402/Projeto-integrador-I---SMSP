# Importando a blioteca para obter a data atual
from datetime import date

# Importando uma função que multiplica matrizes e outra que as transp da biblioteca mumpy -> usadas nas funções de cripto e descriptografia
from numpy import matmul, transpose

# Declarando a tabela do alfabeto
T = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Declarando a função de criptografia
def criptografia(nome):

    # Declarando a matriz chave
    chave = [[4, 3],[1,2]]

    nome = nome.upper().replace(' ', '')

    # Vetor de indexação
    I = []

    # Indexando
    for i in range (len(nome)):
        pos = T.index(nome[i])
        if pos == '25':
            I.append(0)
        else:
            I.append(pos+1)

    # Declarando a matriz de texto comum
    P = [[],[]]

    # Indexan
    for i in range(len(I)):
        if i%2 == 0:
            P[0].append(I[i])
        else:
            P[1].append(I[i])

    # Obtendo a matriz de texto cifrado
    C = matmul(chave, P)

    # Convertendo os valores para os números existentes no conjunto alfabeto
    for i in range(len(C)):
        for j in range(len(C[0])):
            C[i][j] %= 26
            if C[i][j] == 0:
                C[i][j] = 26

    # Declarando o vetor que armazena as letras convertidas
    TC = []

    # Convertendo os números em letras
    for i in range(len(C)):
        for j in range(len(C[0])):
            TC.append(T[C[i][j]-1])

    # Declarando a matriz a ser usada na exibição
    cripto = [[],[]]

    # Ajustando as posições das letras na matriz
    for i in range(int(len(TC)/2)):
        cripto[0].append(TC[i])
        cripto[1].append(TC[int(len(TC)/2)+i])

    # Transpondo a matriz para facilitar a exibição
    cripto = transpose(cripto)

    # Obtendo o texto criptografado
    texto_cripto = ''
    for i in range(len(cripto)):
        for j in range(len(cripto[0])):
            texto_cripto += cripto[i][j]

    # Retornando o texto criptografado
    return texto_cripto

# Declarando a função de descriptografia
def descriptografia(nome_cifrado):
    Matriz_inversa=[[42, -63],[-21,84]]

    nome_cifrado = nome_cifrado.upper().replace(' ', '')

    # Vetor de indexação de decifragem
    V = []
    # Indexando
    for i in range (len(nome_cifrado)):
        pos = T.index(nome_cifrado[i])
        if pos == '25':
            V.append(0)
        else:
            V.append(pos+1)

    # Declarando a matriz de texto comum
    P = [[],[]]

    # Indexando
    for i in range(len(V)):
        if i%2 == 0:
            P[0].append(V[i])
        else:
            P[1].append(V[i])

    # Declarando a matriz de texto comum
    M = matmul(Matriz_inversa,P)

    # Convertendo os valores para os números existentes no conjunto alfabeto
    for i in range(len(M)):
        for j in range(len(M[0])):
            M[i][j] %= 26
            if M[i][j] == 0:
                M[i][j] = 26

    # Declarando o vetor que armazena as letras convertidas
    TD = []

    # Convertendo os números em letras
    for i in range(len(M)):
        for j in range(len(M[0])):
            TD.append(T[M[i][j]-1])

    # Declarando a matriz a ser usada na exibição
    descripto = [[],[]]

    # Ajustando as posições das letras na matriz
    for i in range(int(len(TD)/2)):
        descripto[0].append(TD[i])
        descripto[1].append(TD[int(len(TD)/2)+i])

    # Transpondo a matriz para facilitar a exibição
    descripto = transpose(descripto)

    # Obtendo o texto criptografado
    texto_descripto = ''
    for i in range(len(descripto)):
        for j in range(len(descripto[0])):
            texto_descripto += descripto[i][j]

    # Retornando o texto descriptgrafado
    return texto_descripto

# Importando o conector sql
import mysql.connector

# Criando a conexão -> adicionar as infromações do seu banco de dados
connection = mysql.connector.connect(
    host = '',
    user='',
    password='',
    database=''
)

cursor = connection.cursor()

print('-'*162)
print(f'{">=<>=<>=< BEM VINDO(A) AO SISTEMA DE MONITORAMENTO DE SUSTENTABILIDADE PESSOAL >=<>=<>=<":^162}')
print('-'*162)

# Looping de funcionamento do programa
while True:

    # Exibição do menu
    menu = int(input('\nSelecione a opção desejada:\n\n[1] - Inserir dados\n[2] - Alterar dados\n[3] - Apagar dados\n[4] - Listar registros\n[5] - Listar médias\n[6] - Sair\n\n>> '))
    match menu:

        # Inserção de dados
        case 1:
            id = int(input('informe o número para identificação: '))

            data = date.today()

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

            # Inserção de dados mysql 
            comando = f'INSERT INTO pi_entradas_sustentabilidade(id, data_registro, consumo_ag, consumo_energia, pct_lixo, transporte_publico, bicicleta, caminhada, carro_comb_fossil, carro_eltrico, carona) VALUES ( {id}, {data}, {consumo_agua}, {consumo_energia}, {media_lixo}, {transporte_publico}, {bicicleta}, {caminhada}, {carro_combustivel}, {carro_eletrico}, {carona_compartilhada})'
                
            cursor.execute(comando)
            connection.commit() # Editar banco de dados

        # Alteração de dados
        case 2:

            data = str(input('informe a data da inserção (AAAA-MM-DD): ')) # Utilizando a data como referência
            id =int(input('Insira um ID: '))
            print('-consumo_ag\n -consumo_energia\n -pct_lixo\n -transporte_publico\n -bicicleta\n -caminhada\n -carro_comb_fossil\n -carro_eltrico\n -carona')

            coluna = str(input('informe qual dos atributos acima deseja alterar: ')) # Coluna do dado a ser alterado
            valor = str(input('informe o novo valor: ')) # Informando o novo valor

            comando = f'UPDATE pi_entradas_sustentabilidade SET {coluna} = {valor} WHERE data_registro = {data} and id = {id}'

            cursor.execute(comando)
            connection.commit() # Editar banco de dados
            print('Alterou')

        # Apagamento de dados
        case 3:

            data = str(input('informe a data da inserção: ')) # Utilizando a data como referência
            id = int(input('Insira um ID: '))
            comando = f'DELETE FROM pi_entradas_sustentabilidade WHERE data_registro = {data} and id = {id}'
            cursor.execute(comando)
            connection.commit() # Editar banco de dados
            print('apagou')

        # Listagem de registros
        case 4:

            # Exibição dos dados armazenados
            comando = 'SELECT * FROM pi_entradas_sustentabilidade'
            cursor.execute(comando)
            resultado = []
            resultado = cursor.fetchall() # lê o banco de dados -> apenas para selects
            print('\nExibição dos dados de inserção:\n')
            
            # Escrevendo a tabela
            print('='*162)
            print(f'{"| ID ":^5}', end='')
            print(f'{"| Data de registro ":^15}', end='')
            print(f'{"| Consumo de água ":^18}', end='')
            print(f'{"| Consumo de energia ":^21}', end='')
            print(f'{"| Quantidade de lixo gerado ":^28}', end='')
            print(f'{"| % de lixo reciclável gerado ":^30}', end='')
            print(f'{"| Meios de transportes utilizados":<40}', end=f'{"|"}\n')
            print('='*162)
            for i in range(len(resultado)):
                print(f'|{resultado[i][0]:^4}', end='|')
                print(f'{str(resultado[i][1]):^18}', end='|')
                print(f'{f"{resultado[i][2]} L":^17}', end='|')
                print(f'{f"{resultado[i][3]} KwH":^20}', end='|')
                print(f'{f"{resultado[i][4]} Kg":^27}', end='|')
                print(f'{f"{resultado[i][5]}%":^29}', end='| ')
                print(resultado[i][6:12], end=f'{"|":>9}\n')
                print('-'*162)

            # Exibição da classificação dos registros
            comando = 'SELECT * FROM pi_classificacoes_sustentabilidade'
            cursor.execute(comando)
            resultado_class = []
            resultado_class = cursor.fetchall()
            print('\nExibição da classificação dos dados armazenados:\n')
            print('='*143)
            print(f'{"| ID ":^5}', end='|')
            print(f'{"Consumo de água ":^30}', end='|')
            print(f'{"Consumo de energia ":^30}', end='|')
            print(f'{"% de lixo reciclável gerado ":^32}', end='|')
            print(f'{"Meios de transportes utilizados":^41}', end=f'{"|"}\n')
            print('='*143)
            for i in range(len(resultado_class)):
                print(f'|{resultado_class[i][0]:^4}', end='|')
                print(f'{f"{resultado_class[i][1]}":^30}', end='|')
                print(f'{f"{resultado_class[i][2]}":^30}', end='|')
                print(f'{f"{resultado_class[i][3]}":^32}', end='| ')
                print(f'{resultado_class[i][4]:^40}', end='|\n')
                print('-'*143)

        # Listagem de médias
        case 5:
            print('='*143)
            print('Média dos dados coletados')
            print('='*143)

            # Água
            comando = 'SELECT avg(consumo_agua) FROM pi_entradas_sustentabilidade'
            cursor.execute(comando)
            media_agua = cursor.fetchone()
            print(f'\nMédia do consumo de água: {media_agua[0]:.2f} L')

            if (media_agua[0] >= 150):
                if (media_agua[0] > 200):
                    print("Classificação do consumo de água: Baixa sustentabilidade\n")
                else:
                    print("Classificação do consumo de água: Moderada sustentabilidade\n")
            else:
                print("Classificação do consumo de água: Alta sustentabilidade\n")
            print('-'*143)

            # Energia
            comando = 'SELECT avg(consumo_energia) FROM pi_entradas_sustentabilidade'
            cursor.execute(comando)
            media_energia = cursor.fetchone()

            print(f'\nMédia do consumo de energia: {media_energia[0]:.2f} kwH')
            if (media_energia[0] >= 5): 
                if (media_energia[0] > 10):
                    print("Classificação do consumo de energia: Baixa sustentabilidade\n")
                else: 
                    print("Classificação do consumo de energia: Moderada sustentabilidade\n")
            else:
                print("Classificação do consumo de energia: Alta sustentabilidade\n")  
            print('-'*143) 

            #Porcentagem
            comando = 'SELECT avg(pct_lixo) FROM pi_entradas_sustentabilidade'
            cursor.execute(comando)
            media_lixo = cursor.fetchone()
            print(f'\nMédia da porcentagem de lixo reciclável gerado: {media_lixo[0]:.2f}%')

            if (media_lixo[0] <= 50):
                if (media_lixo[0] < 20):
                    print("Classificação da geração de resíduos recicláveis: Baixa sustentabilidade\n")
                else:
                    print("Classificação da geração de resíduos recicláveis: Moderada sustentabilidade\n")
            else:
                print("Classificação da geração de resíduos recicláveis: Alta sustentabilidade\n")
            print('-'*143)

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

            print('\nMédia da classificação de transportes: ', end='')
            # Análise dos dados convertidos
            if (not 3 in class_transporte) and (not 2 in class_transporte):
                print('Alta sustentabilidade\n')
            elif (not 1 in class_transporte) and (not 2 in class_transporte):
                print('Baixa sustentabilidade\n')
            else:
                print('Moderada sustentabilidade\n')
            print('-'*143)

        # Sair do programa
        case 6:
            break

        # Opções inválidas
        case _:
            print('Opção inválida! Tente novamente.\n')

cursor.close()
connection.close()

print('Encerrando programa...')
print('ATÉ A PRÓXIMA!')