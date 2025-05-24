# Importando a blioteca para obter a data atual
from datetime import date

# Importando uma função que multiplica matrizes e outra que as transp da biblioteca mumpy -> usadas nas funções de cripto e descriptografia
from numpy import matmul, transpose

# Declarando a tabela do alfabeto
T = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

chave = [[4,3],[1,2]]

# Declarando a função de criptografia
def criptografia(chave, nome):

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

    # Caso a palavra tenha um tamanho ímpar, repete a última letra 
    if len(nome)%2 != 0:
        pos = T.index(nome[-1])
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
def descriptografia(chave, nome_cifrado):
    # Tabela dos inversos no Z26
    TABELA = [[1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25],[1, 9, 21, 15, 3, 19, 7, 23, 11, 5, 17, 25]]

    # Obtendo o determinante
    det = chave[0][0]*chave[1][1] - chave[0][1] * chave[1][0]
    # Obtendo o equivalente do determinante no conjunto Z6
    det %= 26
    # Encontrando o determinante na tabela dos inversos
    indice_inverso = TABELA[0].index(det)
    # Encontrando o equivalente do determinante na tabela dos inversos
    inverso = TABELA[1][indice_inverso]
    # Montando a matriz inversa
    matriz_inversa = [[chave[1][1]*inverso, chave[0][1]*(-1)*inverso],[chave[1][0]*(-1)*inverso, chave[0][0]*inverso]]

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
    M = matmul(matriz_inversa,P)

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

    # Excluindo a última letra do texto, caso ela seja repetida
    if texto_descripto[-1] == texto_descripto[-2]:
        texto_descripto = texto_descripto[:len(texto_descripto)-1]

    # Adicionando espaçamento para garantir uma melhor exibição dos dados
    if texto_descripto == 'BAIXASUSTENTABILIDADE':
        texto_descripto = 'BAIXA SUSTENTABILIDADE'
    elif texto_descripto == 'MODERADASUSTENTABILIDADE':
        texto_descripto = 'MODERADA SUSTENTABILIDADE'
    elif texto_descripto == 'ALTASUSTENTABILIDADE':
        texto_descripto = 'ALTA SUSTENTABILIDADE'

    # Retornando o texto descriptgrafado
    return texto_descripto

# Importando o conector sql
import mysql.connector

# Criando a conexão -> adicionar as infromações do seu banco de dados
connection = mysql.connector.connect(
    host = '127.0.0.1',
    user='root',
    password='EnzoPazian140207',
    database='teste_py'
)

cursor = connection.cursor()

print('-'*200)
print(f'\033[1m{">=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=< BEM VINDO(A) AO SISTEMA DE MONITORAMENTO DE SUSTENTABILIDADE PESSOAL! >=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<":^200}\033[0m')
print('-'*200)

# Looping de funcionamento do programa
while True:

    # Exibição do menu
    menu = int(input('\n\033[1mSelecione a opção desejada:\033[0m\n\n[1] - Inserir dados\n[2] - Alterar dados\n[3] - Apagar dados\n[4] - Listar registros\n[5] - Listar médias\n[6] - Sair\n\n>> '))
    match menu:

        # Inserção de dados
        case 1:
            # Inicializando a lista de entrada
            dados_entrada = ['',0,0,0,0,['N','N','N','N','N','N']]
            # Inicializando a lista de classificações
            class_entradas = ['','','','']
            # Data atual
            dados_entrada[0] = date.today()
            # Água
            dados_entrada[1] = float(input("\nInforme o quanto de água você consumiu hoje (Aprox., em Litros): "))
            # Energia
            dados_entrada[2] = float(input("\nInforme quanto de energia elétrica você consumiu hoje (em kWh): "))
            # Quantidade de lixo
            dados_entrada[3] = float(input("\nInforme quantos Kg de resíduos não recicláveis você produziu hoje: ")) 
            # Porcentagem de lixo
            dados_entrada[4] = float(input("\nInforme a porcentagem de resíduos recicláveis que você gerou hoje: "))

            #Inserção e validação inicial dos dados de transporte

            print("\nIndique quais meios de transporte foram utilizados por você hoje\n")

            while True:
                dados_entrada[5][0] = str(input("Transporte público (ônibus, metrô ou trem) [S/N]\n>> ")).upper()
                if dados_entrada[5][0] == 'S' or dados_entrada[5][0] == 'N':
                    break
                else:
                    print("Resposta inválida\n")

            while True:
                dados_entrada[5][1] = str(input("Bicicleta [S/N]\n>> ")).upper()
                if dados_entrada[5][1] == 'S' or dados_entrada[5][1] == 'N':
                    break
                else:
                    print("Resposta inválida\n")
                    
            while True: 
                dados_entrada[5][2] = str(input("Caminhada [S/N]\n>> ")).upper()
                if dados_entrada[5][2] == 'S' or dados_entrada[5][2] == 'N':
                    break
                else:
                    print("Resposta inválida\n")

            while True:
                dados_entrada[5][3] = str(input("Carro (combustível fóssil)? [S/N]\n>> ")).upper()
                if dados_entrada[5][3] == 'S' or dados_entrada[5][3] == 'N':
                    break
                else:
                    print("Resposta inválida\n")

            while True:
                dados_entrada[5][4] = str(input("Carro elétrico? [S/N]\n>> ")).upper()
                if dados_entrada[5][4] == 'S' or dados_entrada[5][4] == 'N':
                    break
                else:
                    print("Resposta inválida\n")

            while True:
                dados_entrada[5][5] = str(input("Carona compartilhada (combustível fóssil) [S/N]\n>> ")).upper()
                if dados_entrada[5][5] == 'S' or dados_entrada[5][5] == 'N':
                    break
                else:
                    print("Resposta inválida\n")

            # Inserção de dados mysql 
            comando = f'INSERT INTO pi_entradas_sustentabilidade(data_registro, consumo_agua, consumo_energia, qtde_lixo, pct_lixo, transporte_publico, bicicleta, caminhada, carro_comb_fossil, carro_eletrico, carona) VALUES ("{dados_entrada[0]}", {dados_entrada[1]}, {dados_entrada[2]}, {dados_entrada[3]}, {dados_entrada[4]}, "{dados_entrada[5][0]}", "{dados_entrada[5][1]}", "{dados_entrada[5][2]}", "{dados_entrada[5][3]}", "{dados_entrada[5][4]}", "{dados_entrada[5][5]}")'            
            cursor.execute(comando)
            connection.commit() # Editar banco de dados

            # Obtendo o último ID para a inserção na tabela de classificações
            cursor.execute('SELECT LAST_INSERT_ID()')
            ultimo_id = cursor.fetchone()

            # Classificando as entradas
            # Consumo de água
            if (dados_entrada[1] >= 150):
                if (dados_entrada[1] > 200):
                    class_entradas[0] = 'Baixa Sustentabilidade'
                else:
                    class_entradas[0] = 'Moderada Sustentabilidade'
            else:
                class_entradas[0] = 'Alta Sustentabilidade'

            # Consumo de energia
            if (dados_entrada[2] >= 5): 
                if (dados_entrada[2] > 10):
                    class_entradas[1] = 'Baixa Sustentabilidade'
                else:
                    class_entradas[1] = 'Moderada Sustentabilidade'
            else:
                class_entradas[1] = 'Alta Sustentabilidade'

            # Porcentagem de lixo
            if (dados_entrada[4] <= 50):
                if (dados_entrada[4] < 20):
                    class_entradas[2] = 'Baixa Sustentabilidade'
                else:
                    class_entradas[2] = 'Moderada Sustentabilidade'
            else:
                class_entradas[2] = 'Alta Sustentabilidade'

            # Meios de transporte
            if dados_entrada[5][0] == 'S' or dados_entrada[5][1] == 'S' or dados_entrada[5][2] == 'S' or dados_entrada[5][4] == 'S':
                if dados_entrada[5][3]=='S' or dados_entrada[5][5]=='S':
                    class_entradas[3] = 'Moderada Sustentabilidade'
                else:
                    class_entradas[3] = 'Alta Sustentabilidade'
            else:
                if dados_entrada[5][3]=='N' and dados_entrada[5][5]=='N':
                    class_entradas[3] = 'Alta Sustentabilidade'
                else:
                    class_entradas[3] = 'Baixa Sustentabilidade'

            # Criptografando as classificações
            # Água
            class_entradas[0] = criptografia(chave, class_entradas[0])
            # Energia
            class_entradas[1] = criptografia(chave, class_entradas[1])
            # Lixo
            class_entradas[2] = criptografia(chave, class_entradas[2])
            # Transporte
            class_entradas[3] = criptografia(chave, class_entradas[3])

            # Inserindo as classificações criptografadas na tabela
            comando = f'INSERT INTO pi_classificacoes_sustentabilidade(id, classificacao_agua, classificacao_energia, classificacao_pct_lixo, classificacao_transporte) VALUES ({ultimo_id[0]}, "{class_entradas[0]}", "{class_entradas[1]}", "{class_entradas[2]}", "{class_entradas[3]}")'            
            cursor.execute(comando)
            connection.commit() # Editar banco de dados

            print('\nInserção realizada com sucesso!!\nTe redirecionando para o menu principal...\n')
            print('-='*100)

        # Alteração de dados
        case 2:

            while True:
                id = int(input('\nInforme o ID do registro a ser alterado: ')) # Utilizando o ID como parâmetro para a alteração - chave primária
                cursor.execute(f'SELECT * FROM pi_entradas_sustentabilidade WHERE id = {id}') # Garantindo que o ID informado existe nos registros
                ids_existentes = []
                ids_existentes = cursor.fetchall()
                if len(ids_existentes) == 0: # Verificando se a lista não está vazia
                    print('\n\033[1;31mO ID informado não existe na tabela. Tente novamente.\033[m\n')
                else:
                    break
            nova_class = ['','']
            while True:
                coluna = int(input('\n\033[1mSelecione o campo que você deseja alterar:\033[m\n[1] - Data de registro\n[2] - Consumo de água: \n[3] - Consumo de energia\n[4] - Quantidade de lixo gerada\n[5] - Porcentagem de lixo reciclável gerado\n[6] - Dados de transporte\n\n>> ')) # Definindo o dado a ser alterado
                match coluna:
                    case 1:
                        valor = input('Informe seguindo o parâmetro (AAAA-MM-DD) o novo valor para o campo: ').upper() # Informando o novo valor
                        coluna = 'data_registro' # Identifica a coluna a ser alterada
                        tipo_dado = 'str' # Define o tipo de dado do campo
                        break
                    case 2:
                        valor = float(input('Informe em Litros o novo valor para o campo: '))
                        coluna = 'consumo_agua'
                        tipo_dado = 'float'
                        nova_class[0] = 'classificacao_agua'
                        if (valor >= 150): # Atualizando as classificações com base no novo valor
                            if (valor > 200):
                                nova_class[1] = 'Baixa Sustentabilidade'
                            else:
                                nova_class[1] = 'Moderada Sustentabilidade'
                        else:
                            nova_class[1] = 'Alta Sustentabilidade'
                        break
                    case 3:
                        valor = float(input('Informe em Kwh o novo valor para o campo: '))
                        coluna = 'consumo_energia'
                        tipo_dado = 'float'
                        nova_class[0] = 'classificacao_energia'
                        if (valor >= 5): 
                            if (valor > 10):
                                nova_class[1] = 'Baixa Sustentabilidade'
                            else: 
                                nova_class[1] = 'Moderada Sustentabilidade'
                        else:
                            nova_class[1] = 'Alta Sustentabilidade'
                        break
                    case 4:
                        valor = float(input('Informe em Kg o novo valor para o campo: '))
                        coluna = 'qtde_lixo'
                        tipo_dado = 'float'
                        break
                    case 5:
                        valor = float(input('Informe em % o novo valor para o campo: '))
                        coluna = 'pct_lixo'
                        tipo_dado = 'float'
                        nova_class[0] = 'classificacao_pct_lixo'
                        if (valor <= 50):
                            if (valor < 20):
                                nova_class[1] = 'Baixa Sustentabilidade'
                            else: 
                                nova_class[1] = 'Moderada Sustentabilidade'
                        else:
                            nova_class[1] = 'Alta Sustentabilidade'
                        break
                    case 6: # Dados de transporte
                        nova_class[0] = 'classificacao_transporte'
                        while True:
                            coluna = int(input('\n\033[1mSelecione o dado de transporte que você deseja alterar:\033[m\n[1] - Uso de transporte público\n[2] - Uso de bicicleta\n[3] - Caminhada\n[4] - Uso de carro movido a combustível fóssil\n[5] - Uso de carro elétrico\n[6] - Uso de carona compartilhada\n\n>> '))
                            match coluna:
                                case 1:
                                    coluna = 'transporte_publico'
                                    tipo_dado = 'str'
                                    break
                                case 2:
                                    coluna = 'bicicleta'
                                    tipo_dado = 'str'
                                    break
                                case 3:
                                    coluna = 'caminhada'
                                    tipo_dado = 'str'
                                    break
                                case 4:
                                    coluna = 'carro_comb_fossil'
                                    tipo_dado = 'str'
                                    break
                                case 5:
                                    coluna = 'carro_eletrico'
                                    tipo_dado = 'str'
                                    break
                                case 6:
                                    coluna = 'carona'
                                    tipo_dado = 'str'
                                    break
                                case _:
                                    print('\n\033[1;31mOpção inválida! Tente novamente.\033[m\n')
                        
                        print('>> Os campos de transporte só aceitam valores "S" e "N"')
                        while True:
                            valor = input('Informe o novo valor para o campo: ').upper() # Informando o novo valor
                            if valor == 'S' or valor == 'N':
                                print('>>Tipo de dado inválido. O campo só aceita os valores "S" e "N".')
                                break
                        break
                    case _:
                        print('\n\033[1;31mOpção inválida! Tente novamente.\033[m\n')

            if tipo_dado == 'str': # Verificando o tipo de dado para adequar o comando de atualização
                comando = f'UPDATE pi_entradas_sustentabilidade SET {coluna} = "{valor}" WHERE id = {id}'
            elif tipo_dado == 'float' or tipo_dado == 'int':
                comando = f'UPDATE pi_entradas_sustentabilidade SET {coluna} = {valor} WHERE id = {id}'    

            cursor.execute(comando) # Executando o comando de atualização
            connection.commit() # Editar banco de dados

            # Alterando os dados na tabela de classificações
            if nova_class[0] == 'classificacao_transporte': # Analisando os novos dados de transporte para alterar a classificação
                comando = f'SELECT transporte_publico, bicicleta, caminhada, carro_comb_fossil, carro_eletrico, carona FROM pi_entradas_sustentabilidade WHERE id = {id}' # Obtendo os dados de transporte com as informações atualizadas
                cursor.execute(comando)
                dados_transporte = cursor.fetchone()
                if dados_transporte[0]=='S' or dados_transporte[1]=='S' or dados_transporte[2]=='S' or dados_transporte[4]=='S':
                    if dados_transporte[3]=='S' or dados_transporte[5]=='S':
                        nova_class[1] = 'Moderada Sustentabilidade'
                    else: 
                        nova_class[1] = 'Alta Sustentabilidade'
                else:
                    if dados_transporte[3]=='N' and dados_transporte[5]=='N':
                        nova_class[1] = 'Alta Sustentabilidade'
                    else:
                        nova_class[1] = 'Baixa Sustentabilidade'

            nova_class[1] = criptografia(chave, nova_class[1])

            if coluna != 'data_registro' and coluna != 'qtde_lixo':
                cursor.execute(f'UPDATE pi_classificacoes_sustentabilidade SET {nova_class[0]} = "{nova_class[1]}" WHERE id = {id}') # Atualizando a classificação com base no novo valor
                connection.commit()

            print('\nCampo alterado com sucesso!!\nTe redirecionando para o menu principal...\n')
            print('-='*100)

        # Apagamento de dados
        case 3:
            # Verificação do ID
            while True:
                id = int(input('\nInforme o ID do registro a ser alterado: ')) # Utilizando o ID como parâmetro para a alteração - chave primária
                cursor.execute(f'SELECT * FROM pi_entradas_sustentabilidade WHERE id = {id}') # Garantindo que o ID informado existe nos registros
                ids_existentes = []
                ids_existentes = cursor.fetchall()
                if len(ids_existentes) == 0: # Verificando se a lista não está vazia
                    print('\n\033[1;31mO ID informado não existe na tabela. Tente novamente.\033[m\n')
                else:
                    break
            # Apagando dados da tabela de classificações
            comando = f'DELETE FROM pi_classificacoes_sustentabilidade WHERE id = {id}'
            cursor.execute(comando)
            connection.commit()
            # Apagando dados da tabela de entradas
            comando = f'DELETE FROM pi_entradas_sustentabilidade WHERE id = {id}'
            cursor.execute(comando)
            connection.commit()
            print('\nCampo apagado com sucesso!!\nTe redirecionando para o menu principal...\n')
            print('-='*100)

        # Listagem de registros
        case 4:

            # Exibição dos dados armazenados
            comando = 'SELECT * FROM pi_entradas_sustentabilidade'
            cursor.execute(comando)
            resultado = []
            resultado = cursor.fetchall() # lê o banco de dados -> apenas para selects
            print('\n\033[1mExibição dos dados de inserção:\033[0m\n')
            
            # Escrevendo a tabela
            print('='*200)
            print(f'\033[1m{"| ID ":^5}', end='')
            print(f'{"| Data de registro ":^15}', end='')
            print(f'{"| Consumo de água ":^18}', end='')
            print(f'{"| Consumo de energia ":^21}', end='')
            print(f'{"| Quantidade de lixo gerado ":^28}', end='')
            print(f'{"| % de lixo reciclável gerado ":^30}', end='| ')
            print(f'{"Meios de transportes utilizados":<76}', end=f'|\033[0m\n')
            print('='*200)
            transportes = []
            for i in range(len(resultado)):
                print(f'|{resultado[i][0]:^4}', end='|')
                print(f'{str(resultado[i][1]):^18}', end='|')
                print(f'{f"{resultado[i][2]} L":^17}', end='|')
                print(f'{f"{resultado[i][3]} KwH":^20}', end='|')
                print(f'{f"{resultado[i][4]} Kg":^27}', end='|')
                print(f'{f"{resultado[i][5]}%":^29}', end='| ')
                transportes.clear()
                if resultado[i][6] == 'S':
                    transportes.append('Transp. público')
                if resultado[i][7] == 'S':
                    transportes.append('Bicicleta')
                if resultado[i][8] == 'S':
                    transportes.append('Caminhada')
                if resultado[i][9] == 'S':
                    transportes.append('Carro comb. fóssil')
                if resultado[i][10] == 'S':
                    transportes.append('Carro elétrico')
                if resultado[i][11] == 'S':
                    transportes.append('Carona')
                if resultado[i][6:12] == ['N', 'N', 'N', 'N', 'N', 'N']:
                    transportes.append('Nenhum transporte utilizado')
                print(f'{str(transportes[:]):<76}', end='|\n')
                print('-'*200)

            # Exibição da classificação dos registros
            comando = 'SELECT * FROM pi_classificacoes_sustentabilidade'
            cursor.execute(comando)
            resultado_class = []
            resultado_class = cursor.fetchall()
            print('\n\033[1mExibição da classificação dos dados armazenados:\033[0m\n')
            print('='*143)
            print(f'\033[1m{"| ID ":^5}', end='|')
            print(f'{"Consumo de água ":^30}', end='|')
            print(f'{"Consumo de energia ":^30}', end='|')
            print(f'{"% de lixo reciclável gerado ":^32}', end='|')
            print(f'{"Meios de transportes utilizados":^41}', end=f'|\033[0m\n')
            print('='*143)
            for i in range(len(resultado_class)):
                print(f'|{resultado_class[i][0]:^4}', end='|')
                print(f'{descriptografia(chave, resultado_class[i][1]):^30}', end='|')
                print(f'{descriptografia(chave, resultado_class[i][2]):^30}', end='|')
                print(f'{descriptografia(chave, resultado_class[i][3]):^32}', end='| ')
                print(f'{descriptografia(chave, resultado_class[i][4]):^40}', end='|\n')
                print('-'*143)

        # Listagem de médias
        case 5:
            print('='*143)
            print(f'\033[1m{"MÉDIA DOS DADOS COLETADOS":^143}\033[0m')
            print('='*143)

            # Água
            comando = 'SELECT avg(consumo_agua) FROM pi_entradas_sustentabilidade'
            cursor.execute(comando)
            media_agua = cursor.fetchone()
            print(f'\n\033[1m Média do consumo de água:\033[0m {media_agua[0]:.2f} L')
            print("\033[1m Classificação do consumo de água: \033[0m", end='')

            if (media_agua[0] >= 150):
                if (media_agua[0] > 200):
                    print("Baixa sustentabilidade\n")
                else:
                    print("Moderada sustentabilidade\n")
            else:
                print("Alta sustentabilidade\n")
            print('-'*143)

            # Energia
            comando = 'SELECT avg(consumo_energia) FROM pi_entradas_sustentabilidade'
            cursor.execute(comando)
            media_energia = cursor.fetchone()

            print(f'\n\033[1m Média do consumo de energia:\033[0m {media_energia[0]:.2f} kwH')
            print("\033[1m Classificação do consumo de energia: \033[0m", end='')

            if (media_energia[0] >= 5): 
                if (media_energia[0] > 10):
                    print("Baixa sustentabilidade\n")
                else: 
                    print("Moderada sustentabilidade\n")
            else:
                print("Alta sustentabilidade\n")  
            print('-'*143) 

            #Porcentagem
            comando = 'SELECT avg(pct_lixo) FROM pi_entradas_sustentabilidade'
            cursor.execute(comando)
            media_lixo = cursor.fetchone()
            print(f'\n\033[1m Média da porcentagem de lixo reciclável gerado:\033[0m {media_lixo[0]:.2f}%')
            print("\033[1m Classificação do consumo da porcentagem de lixo reciclável gerado: \033[0m", end='')

            if (media_lixo[0] <= 50):
                if (media_lixo[0] < 20):
                    print("Baixa sustentabilidade\n")
                else:
                    print("Moderada sustentabilidade\n")
            else:
                print("Alta sustentabilidade\n")
            print('-'*143)

            # Tipos de transporte
            comando = 'SELECT transporte_publico, bicicleta, caminhada, carro_comb_fossil, carro_eletrico, carona FROM pi_entradas_sustentabilidade'
            cursor.execute(comando)
            dados_transporte = []
            class_transporte = []
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

            print('\n\033[1m Média da classificação de transportes:\033[0m ', end='')
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
            print('\n\033[1;31mOpção inválida! Tente novamente.\033[m\n')

cursor.close()
connection.close()

print('\nEncerrando programa...\n')
print('-'*200)
print(f'\033[1m{">=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=< ATÉ A PRÓXIMA! >=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<>=<":^200}\033[0m')
print('-'*200)