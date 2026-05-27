import random

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))

peso1 = round(random.uniform(0, 1), 3)
peso2 = round(random.uniform(0, 1), 3)
peso3 = round(random.uniform(0, 1), 3)

lim_atv = -1

soma_produtos = (valor1 * peso1) + (valor2 * peso2) + (valor3 * peso3)

pot_de_atv = round((lim_atv + soma_produtos),3)

if pot_de_atv >= 0:
    y = 1
else:
    y = -1

print("\n--- Processamento do Perceptron ---")
print(f"Valores: [{valor1}, {valor2}, {valor3}]")
print(f"Pesos:   [{peso1}, {peso2}, {peso3}]")
print("-" * 40)
print(f"Soma Linear (Σ):            {round(soma_produtos, 3)}")
print(f"Potencial de Ativação (u):  {pot_de_atv}")
print(f"Sinal de Saída Final (y):   {y}")