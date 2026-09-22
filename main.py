# =========================
# IMPORTS
# =========================

import random

# =========================
# CONSTANTES
# =========================

MSG_ESCOLHA_FUNCAO = "Escolha qual função você deseja usar: "
MSG_ESCOLHA_CRIATURA = "Escolha a criatura: "
TIPOS_TESTE = {
    1: 'furtividade',
    2: 'iniciativa',
    3: 'percepcao',
    11: 'fortitude',
    12: 'reflexos',
    13: 'vontade',
    21: 'ataque',
}

# =========================
# INFORMAÇÕES DO JOGO
# =========================

CRIATURAS = {
    1: {
        'nome': 'Freddy',
        
        'ataques': {
            1: {
                'bonus': 15,
                'dados': 3,
                'dado_dano': 6,
                'qtde_dados': 3,
                'bonus_dano': 12,
                'tipo_dano': 'Impacto'
            },
        },
        
        'furtividade': {
            'bonus': 15,
            'dados': 4
        },
            
        'iniciativa': {
            'bonus': 10,
            'dados': 1
        },
        
        'percepcao': {
            'bonus': 12,
            'dados': 4
        },
        
        'fortitude': {
            'bonus': 15,
            'dados': 3
        },
        
        'reflexos': {
            'bonus': 10,
            'dados': 1
        },
        
        'vontade': {
            'bonus': 15,
            'dados': 4
        },
        
        'habilidades': {
            1: {
                'nome': 'Aterrorizar',
                'dado_dano': 8,
                'qtde_dados': 2,
                'DT': 25,
                'tipo_dano': 'Mental',
                'teste_resist': 'Vontade',
            },
        },
    
    },
    
    2: {
        'nome': 'Bonnie',
        
        'ataques': {
            1: {
                'bonus': 15,
                'dados': 3,
                'dado_dano': 8,
                'qtde_dados': 2,
                'bonus_dano': 12,
                'tipo_dano': 'Cortante',
                'dado_dano_add': 6,
                'qtde_dados_add': 2,
                'tipo_dano_add': 'Sangue',
            },
        },
        
        'furtividade': {
            'bonus': 0,
            'dados': 3
        },
            
        'iniciativa': {
            'bonus': 15,
            'dados': 3
        },
        
        'percepcao': {
            'bonus': 10,
            'dados': 3
        },
        
        'fortitude': {
            'bonus': 15,
            'dados': 4
        },
        
        'reflexos': {
            'bonus': 15,
            'dados': 3
        },
        
        'vontade': {
            'bonus': 10,
            'dados': 3
        },
        
        'habilidades': {
            1: {
                'nome': 'Grunhido de Dor',
                'dado_dano': 6,
                'qtde_dados': 2,
                'DT': 20,
                'tipo_dano': 'Mental',
                'teste_resist': 'Vontade',
            },
        },
        
    },
    
    3: {
        'nome': 'Chica',
        
        'ataques': {
            # Porrada
            1: {
                'bonus': 15,
                'dados': 3,
                'dado_dano': 6,
                'qtde_dados': 2,
                'bonus_dano': 12,
                'tipo_dano': 'Impacto'
            },
            
            # Cupcake
            2: {
                'bonus': 15,
                'dados': 3,
                'dado_dano': 8,
                'qtde_dados': 2,
                'bonus_dano': 12,
                'tipo_dano': 'Perfurante'
            },
        },
        
        'furtividade': {
            'bonus': 10,
            'dados': 2
        },
            
        'iniciativa': {
            'bonus': 10,
            'dados': 2
        },
        
        'percepcao': {
            'bonus': 10,
            'dados': 3
        },
        
        'fortitude': {
            'bonus': 15,
            'dados': 4
        },
        
        'reflexos': {
            'bonus': 10,
            'dados': 2
        },
        
        'vontade': {
            'bonus': 15,
            'dados': 3
        },
        
        'habilidades': {
            1: {
                'nome': 'Grunhido de Dor',
                'dado_dano': 6,
                'qtde_dados': 2,
                'DT': 20,
                'tipo_dano': 'Mental',
                'teste_resist': 'Vontade',
            },
            
            2: {
                'nome': 'Você não é Capaz',
                'dado_dano': 6,
                'qtde_dados': 2,
                'DT': 25,
                'tipo_dano': 'Mental',
                'dado_dano_add': 4,
                'qtde_dados_add': 4,
                'bonus_dano_add': 6,
                'tipo_dano_add': 'Conhecimento',
                'teste_resist': 'Vontade',
            },
        },
        
    },
    
    4: {
        'nome': 'Foxy',
        
        'ataques': {
            1: {
                'bonus': 15,
                'dados': 4,
                'dado_dano': 8,
                'qtde_dados': 4,
                'bonus_dano': 12,
                'tipo_dano': 'Energia'
            },
            
            2: {
                'bonus': 15,
                'dados': 4,
                'dado_dano': 6,
                'qtde_dados': 6,
                'bonus_dano': 10,
                'tipo_dano': 'Perfurante'
            },
        },
        
        'furtividade': {
            'bonus': 0,
            'dados': 4
        },
            
        'iniciativa': {
            'bonus': 15,
            'dados': 4
        },
        
        'percepcao': {
            'bonus': 5,
            'dados': 2
        },
        
        'fortitude': {
            'bonus': 10,
            'dados': 2
        },
        
        'reflexos': {
            'bonus': 15,
            'dados': 4
        },
        
        'vontade': {
            'bonus': 15,
            'dados': 2
        },
        
    },
    
    5: {
        'nome': 'Golden Freddy',
        
        'ataques':{},
        
        'furtividade': {
            'bonus': 10,
            'dados': 2
        },
            
        'iniciativa': {
            'bonus': 15,
            'dados': 2
        },
        
        'percepcao': {
            'bonus': 15,
            'dados': 5
        },
        
        'fortitude': {
            'bonus': 15,
            'dados': 2
        },
        
        'reflexos': {
            'bonus': 15,
            'dados': 2
        },
        
        'vontade': {
            'bonus': 15,
            'dados': 4
        },
        
        'habilidades': {
            
            1: {
                'nome': 'Circo da Morte',
                'dado_dano': 10,
                'qtde_dados': 2,
                'bonus_dano': 5,
                'DT': 30,
                'tipo_dano': 'Mental',
                'teste_resist': 'Vontade',
            },
            
            2: {
                'nome': 'Quebre minha mente',
                'dado_dano': 4,
                'qtde_dados': 1,
                'bonus_dano': 2,
                'DT': 20,
                'tipo_dano': 'Mental',
                'teste_resist': 'Vontade',
            },
            
        },
        
    },
    
    6: {
        'nome': 'Viajante',
        
        'ataques': {
            1: {
                'bonus': 15,
                'dados': 4,
                'dado_dano': 12,
                'qtde_dados': 2,
                'bonus_dano': 10,
                'tipo_dano': 'Impacto'
            },
        },

        'furtividade': {
            'bonus': 0,
            'dados': 4,
            'invisivel': 15
        },
            
        'iniciativa': {
            'bonus': 12,
            'dados': 4
        },
        
        'percepcao': {
            'bonus': 15,
            'dados': 4
        },
        
        'fortitude': {
            'bonus': 10,
            'dados': 2
        },
        
        'reflexos': {
            'bonus': 15,
            'dados': 4
        },
        
        'vontade': {
            'bonus': 15,
            'dados': 4
        },
        
        'habilidades': {
            1: {
                'nome': 'Devorar Memória',
                'dado_dano': 10,
                'qtde_dados': 2,
                'DT': 29,
                'tipo_dano': 'Mental',
                'teste_resist': 'Vontade',
            },
            
        },
        
    },
    
}

# =========================
# FUNÇÕES
# =========================

def confirmar(prompt):
    while True:
        resposta = input(prompt).strip().lower()
        
        if resposta in ('s','sim','1'):
            return True
            
        if resposta in ('n','nao','não','0'):
            return False
        print("Digite s ou n.\n")

def exibir_criaturas(ids_criaturas):
    for id_criatura in ids_criaturas:
        criatura = CRIATURAS[id_criatura]
        print(f"{id_criatura} - {criatura['nome']}")

def ler_input(prompt, opcoes):
    while True:
        try:
            valor = int(input(prompt))
        except ValueError:
            print("Digite um número válido.\n")
            continue
        
        if valor not in opcoes:
            print("Escolha uma opção válida.\n")
            continue
        
        return valor
        
def rolar_dados(faces_dado, qtde_dados):
    dados = []
    for i in range(qtde_dados):
        dados.append(random.randint(1,faces_dado))
    return dados

# =========================
# PROGRAMA PRINCIPAL
# =========================

while True:
    print('------')
    
    print("\nInício")
    print('1: Evento Aleatório.')
    print('2: Teste de Criaturas.')
    print('3: Dano de Presença Perturbadora.')
    print('4: Dano de Habilidade.')
    escolha_usuario = ler_input(MSG_ESCOLHA_FUNCAO, range(1,5))
    print('')
    
    # Verifica a primeira escolha do usuário
    if escolha_usuario == 1:
        
        exibir_criaturas([4,5])
        escolha_animatronico = ler_input(MSG_ESCOLHA_FUNCAO, range(4,6))
        print("")
        
        if escolha_animatronico == 4:
            print('- Estado 0, Cortina Fechada.')
            print('- Estado 1, Cortina levemente aberta.')
            print('- Estado 2, Cortina completamente aberta.')
            print('- Estado 3, Cortina completamente aberta e cabeça vibrando.')
            estado_foxy = ler_input("Informe o estado atual do Foxy: ", range(0,4))
            
            if estado_foxy == 0:
                print('')
                print('Foxy abrirá sua cortina às 1 da manhã.')
            elif (estado_foxy == 1) or (estado_foxy == 2):
                numero_rodadas = ler_input("Informe quantas rodadas o Foxy já está nessa fase: ", range(0,99))
                print('')
                if(estado_foxy == 1):
                    qtde_dados_foxy = 2
                else:
                    qtde_dados_foxy = 1
                
                dados = rolar_dados(
                    4, qtde_dados_foxy+numero_rodadas
                )
                resultado = min(dados)
                
                print("Dados: ", dados)
                if resultado == 1:
                    if estado_foxy == 1:
                        print("Foxy agora está no estado 2 com a cortina completamente aberta.")
                    else:
                        print('Foxy agora está no estado 3 esperando alguém aparecer em seu campo de visão.')
                else:
                    print('Foxy permanece no mesmo estado.')
            else:
                print('\nFoxy só precisa esperar alguém aparecer em seu campo de visão para iniciar a perseguição.')
        
        elif escolha_animatronico == 5:
            # Foi criada essa opção para o mestre  realizar uma rápida rolagem para ver se os jogadores
            # encontraram o golden freddy.
            dados = rolar_dados(6, 2)
            
            if all(dado == 1 for dado in dados):
                print('Golden Freddy aparece.')
                print(dados)
                
            else:
                print('Sala segura.')
                print(dados)
        
    elif escolha_usuario == 2:
        
        exibir_criaturas(range(1,7))
        
        escolha_animatronico = ler_input(MSG_ESCOLHA_CRIATURA, range(1,7))
        # Realiza a escolha do animatronico
        criatura = CRIATURAS.get(escolha_animatronico)
        # Identifica qual animatronico de acordo com o dicionário
        
        print('')
        print('Testes de Perícia')
        print('1. Furtividade')
        print('2. Iniciativa')
        print('3. Percepção')
        print('')
        print('Testes de Resistência')
        print('11. Fortitude')
        print('12. Reflexos')
        print('13. Vontade')
        print('')
        print('21. Ataque')
        print('')
        escolha_teste = ler_input(
            "Escolha qual teste: ",
            TIPOS_TESTE
        )
        tipo_teste = TIPOS_TESTE[escolha_teste]
        
        print("")
        
        # Estrutura que diferencia testes comuns de ataques, se for diferente de 21, é um Teste
        # Padrão.
        if (escolha_teste != 21):
                     
            # Faz a chamada da função de rolar um teste
            dados = rolar_dados(20, criatura.get(tipo_teste)['dados'])
            resultado = max(dados)
            bonus = criatura.get(tipo_teste)['bonus']
            
            # O viajante tem uma mecânica que enquanto estiver invisível, recebe um
            # bônus e +15 em furtividade.
            if (escolha_animatronico == 6) and (escolha_teste == 1):
                
                if confirmar("O viajante está invisível? (s/n): "):
                    bonus += criatura.get('furtividade')['invisivel']
            
            print("")
            print(f"Teste de {tipo_teste} de {criatura.get('nome')}: {resultado + bonus}")
            print("Dados: ", dados)
            
        else:
                    
            # Cria variável intermediária de ataques
            ataques = criatura.get('ataques')

            margem_ameaca = 0
            
            if not ataques:
                print("A criatura não tem ataques.\n")
                continue
            
            # Se o alvo ter somente 1 ataque:
            if len(ataques) == 1:
                # Cria outra variável intermediária de ataque, dos múltiplos ataques
                # Na linha a seguir, ele seleciona o 1º ataque já que o alvo possui
                # somente 1 ataque.
                ataque = ataques.get(1)
            
            else:
                if (escolha_animatronico == 3):
                    print('1. Porrada')
                    print('2. Cupcake')
                elif (escolha_animatronico == 4):
                    print('1. Gancho')
                    print('2. Mordida')
                    
                # Na linha a seguir, ele identifica qual ataque foi selecionado e
                # armazena na variável intermediária "Ataque"
                escolha_ataque = ler_input("Escolha o ataque: ", ataques)
                ataque = ataques.get(escolha_ataque)
                
            # Faz a chamada da função de rolar um teste de ataque
            dados = rolar_dados(
                20,ataque.get('dados')
            )
            resultado = max(dados)
            
            # Move o bônus de ataque para uma variável intermediária
            bonus = ataque.get('bonus')
                
            # Se a pizzaria estiver sem luz, a margem de ameaça/crítico de Freddy
            # diminui em 1 ponto.
            if (escolha_animatronico == 1):
                if confirmar('A pizza está sem luz? (s/n): '):
                    margem_ameaca = 1
            elif (escolha_animatronico == 4):
                if (escolha_ataque == 2):
                    margem_ameaca = 1

            # Move a quantidade de dados de dano para uma variável intermediária.
            qtde_dados_dano = ataque.get('qtde_dados')
            
            if (escolha_animatronico == 6):
                viajante_dano_add = ler_input(
                    "Quantos seres o viajante já deixou perturbado com devorar memória? "
                    , range(1,6)
                )
                # Viajante passa a dar mais dano com base na condição cumprida.
                qtde_dados_dano += viajante_dano_add
            else:
                qtde_dados_dano = ataque.get('qtde_dados')
            
            # Condição para ataque
            print(f"Teste de {tipo_teste} de {criatura.get('nome')}: {resultado + bonus}")
            print("Dados: ", dados)

            # Acerto normal
            if (resultado < (20-margem_ameaca)) :
                dados_dano = rolar_dados(
                    ataque.get('dado_dano'), qtde_dados_dano
                )
                total_dano = sum(dados_dano)
                bonus_dano = ataque.get('bonus_dano')
                
                print(f"Dano do ataque: {total_dano + bonus_dano} de {ataque.get('tipo_dano')}.")
                print("Dados: ", dados_dano, "+", bonus_dano)
                
            else:
                # Estrutura para acerto crítico, que dobra os dados naturais de dano
                dados_dano = rolar_dados(
                    ataque.get('dado_dano'), qtde_dados_dano * 2
                )
                total_dano = sum(dados_dano)
                bonus_dano = ataque.get('bonus_dano')
                
                print(f"Dano do ataque: {total_dano + bonus_dano} de {ataque.get('tipo_dano')}.")
                print("Dados: ", dados_dano, "+", bonus_dano)

            # Se possuir algum tipo de dano adicional, realiza a estrutura a seguir:
            if 'dado_dano_add' in ataque:
                dados_add = rolar_dados(
                    ataque.get('dado_dano_add'),
                    ataque.get('qtde_dados_add')
                )
                total_add = sum(dados_add)
                print(f"Dano adicional: {total_add} de {ataque.get('tipo_dano_add')}.")
                print("Dados: ", dados_add)
                
    elif(escolha_usuario == 3):
        
        print('1. Freddy - DT 20, 2d6')
        print('2. Bonnie - DT 20, 2d6')
        print('3. Chica - DT 20, 2d6')
        print('4. Foxy - DT 20, 2d6')
        print('5. Golden Freddy - DT 25, 2d6+4')
        print('6. Viajante - DT 20, 3d4')
        escolha_animatronico = ler_input("Escolha a presença perturbadora do animatrônico para jogar: ", range(1,7))
        print("")

        # As 5 criaturas possuem a mesma rolagem
        if(escolha_animatronico >= 1) and (escolha_animatronico <= 5):
            dados = rolar_dados(6,2)
            total_dano = sum(dados)

            # Golden Freddy possui um bônus de +4 ao dano
            if(escolha_animatronico == 5):
                print(f"Dano mental: {total_dano+4}.")
                print("Dados: ", dados, "+4")
                
            # Dano padrão para o resto
            else:
                print(f"Dano mental: {total_dano}.")
                print("Dados: ", dados)
                
        # Viajante dá dano com uma rolagem diferente
        else:
            dados = rolar_dados(4,3)
            total_dano = sum(dados)

            print(f"Dano mental: {total_dano}.")
            print("Dados: ", dados)
            
    else:
        exibir_criaturas(range(1,7))
        escolha_animatronico = ler_input(MSG_ESCOLHA_CRIATURA, range(1,7))
        print('')
        criatura = CRIATURAS.get(escolha_animatronico)

        # Recebe o valor de habilidades, identificando também caso a criatura não tenha.
        habilidades = criatura.get('habilidades', {})

        # Informa que a criatura não possui esse tipo de habilidade.
        if not habilidades:
            print('A criatura não possui esse tipo de habilidade.')
            print('')
            continue

        # Retorna somente a única habilidade lida no dicionário
        elif len(habilidades) == 1:
            habilidade = next(iter(habilidades.values()))

        # Cria um laço de repetição que lista todas as habilidades da criatura, perguntando ao usuário qual
        # habilidade ele irá usar.
        else:
            for chave, valor in habilidades.items():
                print(f'{chave} - {valor["nome"]}')
            
            escolha_habilidade = ler_input("Escolha a habilidade: ", habilidades)
            habilidade = habilidades.get(escolha_habilidade)
            print('')
        
        dados_dano = rolar_dados(
            habilidade.get('dado_dano'), habilidade.get('qtde_dados')
        )
        total_dano = sum(dados)
        
        # Informa ao usuário informações da habilidade, como nome, DT e qual o teste de resistência.
        print(f"Habilidade {habilidade.get('nome')}, DT: {habilidade.get('DT')}, "
        f"Teste de {habilidade.get('teste_resist')}.")

        # Caso possua algum tipo de bônus de dano, ele o soma no dano da habilidade
        if 'bonus_dano' in habilidade:
            bonus_dano = habilidade.get('bonus_dano')
            print(f"Dano: {total_dano + bonus_dano} {habilidade.get('tipo_dano')}.")
        # Caso não exista bônus, ele simplesmente o ignora
        else:
            print(f"Dano: {total_dano} {habilidade.get('tipo_dano')}.")
            
        print("Dados: ", dados_dano)

        # Caso possua dano adicional, ele realiza a rolagem e informa o dano adicional.
        if 'dado_dano_add' in habilidade:
            dados_add = rolar_dados(
                habilidade.get('dado_dano_add'),
                habilidade.get('qtde_dados_add')
            )
            total_add = sum(dados_add)
            
            # Caso o dano adicional possua algum tipo de bônus.
            if 'bonus_dano_add' in habilidade:
                bonus_dano_add = habilidade.get('bonus_dano_add')
                print(f"Dano Adicional: {total_add + bonus_dano_add} de {habilidade.get('tipo_dano_add')}")
            else:
                print(f"Dano Adicional: {total_add} de {habilidade.get('tipo_dano_add')}")
            
            print("Dados: ", dados_add)
        
    # Pergunta ao usuário se ele quer continuar
    if not confirmar("\nDeseja rodar o código novamente? (s/n): "):
        break
