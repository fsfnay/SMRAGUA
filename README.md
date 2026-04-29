# SRMAGUA - Sistema de Monitoramento do Reservatório de Água

## Sobre ❗
    Projeto do Sistema de Monitoramento do Reservatório de Água (SMRAGUA), criado para a disciplina de DS I, do curso de Desenvolvimento de Sistemas, pela ETEC.

## Objetivo 🎯
    Exibir mensagens de alerta com cores diferentes, diretamente no terminal, conforme o nível de água disponível no reservatório.

## Linguagem de programação 🔡
    ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Funcionalidades 🧠
    Geração aleatória do nível de água (0 a 100%), de data (DD/MM/AA) e hora (HH:MM:SS), com base em valores definidos dentro de um limite prestabelecido
    Classificação do nível do reservatório em 5 categorias: 1- Muito baixo (crítico); 2 - Baixo; 3 - Médio; 4 - Alto; 5 - Muito alto (alerta)
    Exibição de mensagens orientativas, conforme o nível do reservatório, para o uso consciente da água
    Saída de dados no terminal utilizando a biblioteca colorama (cores vermelho, amarelo, verde, ciano e azul, respectivamente)

## Como executar ▶️
    Certifique-se de ter o Python instalado
    Instale a dependência: pip install colorama
    Execute o arquivo no terminal:
```
python3 smragua.py
```

## Exemplo de saída de dados 📈
```
BEM-VINDO AO SISTEMA DE MONITORAMENTO DO RESERVATÓRIO DE ÁGUA.

Hoje é dia 15/06/2026, agora são 14:32:10.

A capacidade ocupada do reservatório neste momento é: 37.45%.

De acordo com essa porcentagem, o nível atual do reservatório é:

NÍVEL 2: BAIXO --> RACIONE A ÁGUA E EVITE DESPERDÍCIOS. (As cores são exibidas no terminal)
```
