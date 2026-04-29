## CONTROLE DOS NÍVEIS DE ÁGUA ##

# Configuração dos dados para os níveis de água
import random
import datetime

numero_aleatório = round(random.uniform(0, 100), 2)
def gerar_nivel_agua():
    return numero_aleatório

def gerar_data_hora():
    inicio = datetime.datetime(2026, 1, 1)
    fim = datetime.datetime(2026, 12, 31)
    delta = fim - inicio
    segundos_aleatorios = random.randint(0, int(delta.total_seconds()))
    dt = inicio + datetime.timedelta(seconds=segundos_aleatorios)
    data = dt.strftime("%d/%m/%Y")
    hora = dt.strftime("%H:%M:%S")
    return data, hora

# Configuração de cores para os níveis de água
from colorama import init, Fore, Back, Style
init(autoreset=True)

# Situação atual do reservatório
print("\nBEM-VINDO AO SISTEMA DE MONITORAMENTO DO RESERVATÓRIO DE ÁGUA.")
data, hora = gerar_data_hora()
print(f"\nHoje é dia {data}, agora são {hora}.")

nivel_atual = numero_aleatório
print(f"\nA capacidade ocupada do reservatório neste momento é: {nivel_atual:.2f}%.")

# Determinação dos níveis de água (em %)
def determinar_nivel_agua(valor):
    if valor < 20.00:
        return Fore.RED + "NÍVEL 1: MUITO BAIXO (CRÍTICO) --> SUSPENDA USOS NÃO ESSENCIAIS E PRIORIZE O CONSUMO BÁSICO."
    elif 20.00 <= valor < 40.00:
        return Fore.YELLOW + "NÍVEL 2: BAIXO --> RACIONE A ÁGUA E EVITE DESPERDÍCIOS."
    elif 40.00 <= valor < 60.00:
        return Fore.GREEN + "NÍVEL 3: MÉDIO --> UTILIZE A ÁGUA COM CONSCIÊNCIA E EVITE EXCESSOS."
    elif 60.00 <= valor < 80.00:
        return Fore.CYAN + "NÍVEL 4: ALTO --> SITUAÇÃO CONFORTÁVEL, MAS MANTENHA O USO RESPONSÁVEL."
    else:
        return Fore.BLUE + "NÍVEL 5: MUITO ALTO (ALERTA) --> ATENÇÃO PARA A POSSIBILIDADE DE TRANSBORDAMENTO."

print("\nDe acordo com essa porcentagem, o nível atual do reservatório é:\n")
print(determinar_nivel_agua(nivel_atual))
print() # Linha em branco para espaçamento