# rpg-rabbithole-tools
Aplicação em Python para auxiliar em sessões de RPG, com rolagem de dados, testes de perícias, ataques e cálculos de dano. Projeto pessoal voltado ao aprendizado da linguagem e ao desenvolvimento de lógica de programação.

***Status:** Em desenvolvimento.*

## Sobre o Projeto
Este projeto foi desenvolvido como uma ferramenta auxiliar para sessões de RPG, permitindo a automatização de testes de criaturas e rolagens de dados para ataques.

Ao procurar ferramentas para realizar rolagens de dados pré-definidas, encontrei diversos sites que exigiam alternar entre diferentes telas ou configurar novamente os dados a cada utilização. Isso acabava tornando o processo mais demorado durante as sessões de RPG.

Por isso, desenvolvi este programa como uma ferramenta centralizada para realizar as principais rolagens que utilizo durante minhas sessões, reduzindo a necessidade de consultar e gerenciar manualmente fichas de personagens não jogadores.

O projeto também serve como estudo prático de programação em Python, com foco em funções, estruturas condicionais, dicionários e organização de dados.

## Sistema
O sistema possui diferentes criaturas, cada uma com atributos e comportamentos próprios, permitindo que o mecanismo de testes e ataques seja adaptado a diferentes situações.

| Criatura | Função |
|---|---|
| Freddy | Foco em furtividade e ataques surpresa |
| Bonnie | Realiza ataques que causam dano adicional |
| Chica | Possibilidade de ataque à distância ou corpo a corpo |
| Foxy | Comportamento especial baseado em mudanças de estado e duas opções de ataque |
| Golden Freddy | Comportamento relacionado a eventos aleatórios |
| Viajante | Foco em ataques que ficam mais fortes ao longo do tempo |

## Tecnologias

- Python 3.x
- Git
- GitHub

### Dependências

O projeto utiliza apenas bibliotecas da biblioteca padrão do Python.

## Funcionalidades

- Rolagem de dados
- Testes de ataque
- Testes específicos para criaturas
- Modificadores baseados em condições
- Sistema de dano e dano crítico
- Eventos aleatórios

## Exemplo de Uso

Ao realizar um teste de furtividade com a criatura "Viajante", o sistema pergunta se a criatura está invisível ou não e aplica o bônus correspondente.

```text
=== CASO 1: TESTE DE CRIATURA INVISÍVEL ===

Criatura: Viajante
Teste: Furtividade
Condição: Está invisível

Dados: [15, 10, 2, 10]
Bônus: +15
Resultado: 30

=== CASO 2: TESTE DE CRIATURA VISÍVEL ===

Criatura: Viajante
Teste: Furtividade
Condição: Está visível

Dados: [17, 16, 14, 7]
Bônus: +0
Resultado: 17
```
## Conceitos praticados
- Funções e parâmetros
- Estruturas condicionais
- Loops
- Dicionários aninhados
- Manipulação de dados
- Geração de números aleatórios
- Organização de código
- Tratamento de diferentes comportamentos utilizando estruturas de dados.
## Como executar
O projeto foi desenvolvido em Python 3.x e atualmente é executado
diretamente pelo arquivo `main.py`.
