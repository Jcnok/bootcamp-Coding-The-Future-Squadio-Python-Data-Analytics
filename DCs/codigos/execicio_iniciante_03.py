# Entrada de dados
capacidade_atual, aumento_percentual = map(int, input().split())

# Calcula a nova capacidade do disco de Mithril
nova_capacidade = capacidade_atual * (1 + aumento_percentual / 100)

# Imprime a nova capacidade
print(int(nova_capacidade))
