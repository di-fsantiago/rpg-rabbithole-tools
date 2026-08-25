# =========================
# IMPORTS
# =========================

import random

# =========================
# FUNÇÕES
# =========================

def rolar_teste(faces_dado, qtde_dados):
    dados = []
    for i in range(qtde_dados):
        dados.append(random.randint(1,faces_dado))
    resultado = max(dados)
    return dados, resultado
    
def rolar_dano(faces_dado, qtde_dados):
    dados = []
    for i in range(qtde_dados):
        dados.append(random.randint(1,faces_dado))
    resultado = sum(dados)
    return dados, resultado

# =========================
# DADOS DO JOGO
# =========================

criaturas = {
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
        
    },
    
}

# =========================
# PROGRAMA PRINCIPAL
# =========================

while True:
    print('------')
    print('')
    print("Início")
    print('1: Evento Aleatório;')
    print('2: Teste de Criaturas;')
    print('3: Dano de Presença Perturbadora')
    print('4: Dano de Habilidade')
    escolha_usuario = int(input('Escolha a função que deseja usar: '))
    print('')
    
    
    if escolha_usuario == 1:
        
        print('1: Foxy')
        print('2: Golden Freddy')
        escolha_animatronico= int(input('Escolha a função que deseja usar: '))
        print('')
        
        if(escolha_animatronico == 1):
            pass
        
        elif(escolha_animatronico == 2):
            
            # Foi criada essa opção para caso o mestre precise realizar uma rápida
            # rolagem para ver se os jogadores depararam o golden freddy.
            d6_gf1 = random.randint(1,6)
            d6_gf2 = random.randint(1,6)
            
            if (d6_gf1 == 1) and (d6_gf2 ==  1):
                
                print('GF aparece')
                print(d6_gf1, d6_gf2)
                
            else:
                
                print('Sala segura')
                print(d6_gf1, d6_gf2)
                
        else:
            pass
        
    elif escolha_usuario == 2:
        
        print('1. Freddy')
        print('2. Bonnie')
        print('3. Chica')
        print('4. Foxy')
        print('5. Golden Freddy')
        print('6. Viajante')
        
        escolha_animatronico = int(input('Escolha qual criatura: '))
        # Realiza a escolha do animatronico
        criatura = criaturas.get(escolha_animatronico)
        # Identifica qual animatronico de acordo com o dicionário
        
        if (escolha_animatronico > 6) or (escolha_animatronico < 1):
            continue
        
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
        escolha_teste = int(input('Escolha qual teste: '))
        print('')
        
        if escolha_teste == 1 :
            tipo_teste = 'furtividade'
            
        elif escolha_teste == 2:
            tipo_teste = 'iniciativa'
            
        elif escolha_teste == 3:
            tipo_teste = 'percepcao'
            
        elif escolha_teste == 11:
            tipo_teste = 'fortitude'
            
        elif escolha_teste == 12:
            tipo_teste = 'reflexos'
        
        elif escolha_teste == 13:
            tipo_teste = 'vontade'
        
        elif escolha_teste == 21:
            tipo_teste = 'ataque'
        
        else:
            print("Esse teste não existe.")
            continue
            # Avança caso o usuário coloque um valor fora do informado.
        
        # Estrutura que diferencia testes comuns de ataques, se for diferente de 21, é um Teste
        # Padrão.
        
        if (escolha_teste != 21):
                     
            # Faz a chamada da função de rolar um teste
            dados, resultado = rolar_teste(
                20,criatura.get(tipo_teste)['dados']
            )
            bonus = criatura.get(tipo_teste)['bonus']
            
            # O viajante tem uma mecânica que enquanto estiver invisível, recebe um bônus e +15 em furtividade.
            if (escolha_animatronico == 6) and (escolha_teste == 2):
                invisibilidade = input('O Viajante está invisível? (s/n): ')
                print('')
                
                if (invisibilidade == 's') and (invisibilidade != '1'):
                    bonus += criatura.get('furtividade')['invisivel']
            
            print('')
            print(f"Teste de {tipo_teste} de {criatura.get('nome')}: {resultado + bonus}")
            print("Dados: ", dados)
            
        else:
                    
            # Cria variável intermediária de ataques
            ataques = criatura.get('ataques')

            margem_ameaca = 0
            
            # Se o alvo ter somente 1 ataque:
            if len (ataques) == 1:
                # Cria outra variável intermediária de ataque, dos múltiplos ataques
                # Na linha a seguir, ele seleciona o 1º ataque já que o alvo possui somente
                # 1 ataque.
                ataque = ataques.get(1)
            
            else:
                if (escolha_animatronico == 3):
                    print('1. Porrada')
                    print('2. Cupcake')
                elif (escolha_animatronico == 4):
                    print('1. Gancho')
                    print('2. Mordida')
                    
                # Na linha a seguir, ele identifica qual ataque foi selecionado
                escolha_ataque = int(input('Escolha o ataque: '))
                ataque = ataques.get(escolha_ataque)
                
            # Faz a chamada da função de rolar um teste de ataque
            dados, resultado = rolar_teste(
                20,ataque.get('dados')
            )
            bonus = ataque.get('bonus')
                
            # Se a pizzaria estiver sem luz, a margem de ameaça de Freddy
            # diminui em 1 ponto.
            if (escolha_animatronico == 1):
                escuridao = input('A pizza está sem luz? (s/n): ')
                if (escuridao == 's') or (escuridao == '1') or (escuridao == 'S'):
                    margem_ameaca = 1
            elif (escolha_animatronico == 4):
                if (escolha_ataque == 2):
                    margem_ameaca = 1
                else:
                    margem_ameaca = 0
            
            qtde_dados_dano = ataque.get('qtde_dados')
            
            if (escolha_animatronico == 6):
                viajante_dano_add = int(input("Quantos seres o viajante já deixou perturbado "
                "com devorar memória? "))
                qtde_dados_dano += viajante_dano_add
            else:
                qtde_dados_dano = ataque.get('qtde_dados')
            
            #Condição para ataque
            print(f"Teste de {tipo_teste} de {criatura.get('nome')}: {resultado + bonus}")
            print("Dados: ", dados)
            
            if (resultado < (20-margem_ameaca)) :
                dados_dano, total_dano = rolar_dano(
                    ataque.get('dado_dano'), qtde_dados_dano
                )
                bonus_dano = ataque.get('bonus_dano')
                
                print(f"Dano do ataque: {total_dano + bonus_dano} de {ataque.get('tipo_dano')}.")
                print("Dados: ", dados_dano, "+", bonus_dano)
                
            else:
                dados_dano, total_dano = rolar_dano(
                    ataque.get('dado_dano'), (qtde_dados_dano) * 2
                )
                bonus_dano = ataque.get('bonus_dano')
                
                print(f"Dano do ataque: {total_dano + bonus_dano} de {ataque.get('tipo_dano')}.")
                print("Dados: ", dados_dano, "+", bonus_dano)
                
            if 'dado_dano_add' in ataque:
                dados_add, total_add = rolar_dano(
                    ataque.get('dado_dano_add'),
                    ataque.get('qtde_dados_add')
                )
                print(f"Dano adicional: {total_add} de {ataque.get('tipo_dano_add')}.")
                print("Dados: ", dados_add)
                
    elif(escolha_usuario == 3):
        
        print('1. Freddy - DT 20, 2d6')
        print('2. Bonnie - DT 20, 2d6')
        print('3. Chica - DT 20, 2d6')
        print('4. Foxy - DT 20, 2d6')
        print('5. Golden Freddy - DT 25, 2d6+4')
        print('6. Viajante - DT 20, 3d4')
        escolha_animatronico = int(input('Escolha a presença perturbadora do animatrônico para jogar? '))
        print('')
        
        if(escolha_animatronico >= 1) and (escolha_animatronico <= 5):
            dados, total_dano = rolar_dano(
                6,2
            )
            
            if(escolha_animatronico == 5):
                print(f"Dano mental: {total_dano+4}.")
                print("Dados: ", dados, "+4")
            else:
                print(f"Dano mental: {total_dano}.")
                print("Dados: ", dados)
            
        elif(escolha_animatronico == 6):
            dados, resultado = rolar_dano(
                4,3
            )
            print(f"Dano mental: {total_dano}.")
            print("Dados: ", dados)
            
        else:
            print('Valor ultrapassa o limite.')
    
    elif (escolha_usuario == 4):
        pass
    
    else:
        print('O número informado está fora do limite.')
        
    print('')
    
    # PERGUNTA SE QUER CONTINUAR
    rodar_programa = input('Deseja rodar o código novamente? (s/n): ')
    print('')
    
    if (rodar_programa != 's') and (rodar_programa != '1') and (rodar_programa != 'S'):
        break



