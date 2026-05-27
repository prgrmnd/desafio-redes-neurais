import random

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))

peso1 = round(random.uniform(0, 1), 3)
peso2 = round(random.uniform(0, 1), 3)
peso3 = round(random.uniform(0, 1), 3)

lim_atv = -1

soma_produtos = (valor1 * peso1) + (valor2 * peso2) + (valor3 * peso3)

pot_de_atv = round((soma_produtos - lim_atv),3)

if pot_de_atv >= 0:
    y = 1
else:
    y = -1
