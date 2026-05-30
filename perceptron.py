import random

taxa_aprendizado = 0.01

dados_treino = [
    {"x1": -0.6508, "x2": 0.1097, "x3": 4.0009, "d": -1.0000},
    {"x1": -1.4492, "x2": 0.8896, "x3": 4.4005, "d": -1.0000},
    {"x1": 2.0850,  "x2": 0.6876, "x3": 12.0710, "d": -1.0000},
    {"x1": 0.2626,  "x2": 1.1476, "x3": 7.7985, "d": 1.0000},
    {"x1": 0.6418,  "x2": 1.0234, "x3": 7.0427, "d": 1.0000},
    {"x1": 0.2569,  "x2": 0.6730, "x3": 8.3265, "d": -1.0000},
    {"x1": 1.1155,  "x2": 0.6043, "x3": 7.4446, "d": 1.0000},
    {"x1": 0.0914,  "x2": 0.3399, "x3": 7.0677, "d": -1.0000},
    {"x1": 0.0121,  "x2": 0.5256, "x3": 4.6316, "d": 1.0000},
    {"x1": -0.0429, "x2": 0.4660, "x3": 5.4323, "d": 1.0000},
    {"x1": 0.4340,  "x2": 0.6870, "x3": 8.2287, "d": -1.0000},
    {"x1": 0.2735,  "x2": 1.0287, "x3": 7.1934, "d": 1.0000},
    {"x1": 0.4839,  "x2": 0.4851, "x3": 7.4850, "d": -1.0000},
    {"x1": 0.4089,  "x2": -0.1267, "x3": 5.5019, "d": -1.0000},
    {"x1": 1.4391,  "x2": 0.1614, "x3": 8.5843, "d": -1.0000},
    {"x1": -0.9115, "x2": -0.1973, "x3": 2.1962, "d": -1.0000},
    {"x1": 0.3654,  "x2": 1.0475, "x3": 7.4858, "d": 1.0000},
    {"x1": 0.2144,  "x2": 0.7515, "x3": 7.1699, "d": 1.0000},
    {"x1": 0.2013,  "x2": 1.0014, "x3": 6.5489, "d": 1.0000},
    {"x1": 0.6483,  "x2": 0.2183, "x3": 5.8991, "d": 1.0000},
    {"x1": -0.1147, "x2": 0.2242, "x3": 7.2435, "d": -1.0000},
    {"x1": -0.7970, "x2": 0.8795, "x3": 3.8762, "d": 1.0000},
    {"x1": -1.0625, "x2": 0.6366, "x3": 2.4707, "d": 1.0000},
    {"x1": 0.5307,  "x2": 0.1285, "x3": 5.6883, "d": 1.0000},
    {"x1": -1.2200, "x2": 0.7777, "x3": 1.7252, "d": 1.0000},
    {"x1": 0.3957,  "x2": 0.1076, "x3": 5.6623, "d": -1.0000},
    {"x1": -0.1013, "x2": 0.5989, "x3": 7.1812, "d": -1.0000},
    {"x1": 2.4482,  "x2": 0.9455, "x3": 11.2095, "d": 1.0000},
    {"x1": 2.0149,  "x2": 0.6192, "x3": 10.9263, "d": -1.0000},
    {"x1": 0.2012,  "x2": 0.2611, "x3": 5.4631, "d": 1.0000}
]

for rodada in range(1, 6):
    
    pesos = {
        'w1': random.uniform(0, 1),
        'w2': random.uniform(0, 1),
        'w3': random.uniform(0, 1),
        'w_limiar': random.uniform(0, 1)
    }
    
    pesos_iniciais = pesos.copy()
    epoca_atual = 0

    while True:
        epoca_atual += 1
        erros_epoca = 0

        for entradas in dados_treino:
            soma_produtos = (entradas['x1'] * pesos['w1']) + (entradas['x2'] * pesos['w2']) + (entradas['x3'] * pesos['w3']) + (-1 * pesos['w_limiar'])

            if soma_produtos >= 0:
                sinal_saida = 1
            else:
                sinal_saida = -1

            if sinal_saida != entradas['d']:
                erros_epoca += 1
                
                erro = entradas['d'] - sinal_saida
                pesos['w1'] = pesos['w1'] + (taxa_aprendizado * erro * entradas['x1'])
                pesos['w2'] = pesos['w2'] + (taxa_aprendizado * erro * entradas['x2'])
                pesos['w3'] = pesos['w3'] + (taxa_aprendizado * erro * entradas['x3'])
                pesos['w_limiar'] = pesos['w_limiar'] + (taxa_aprendizado * erro * -1)

        if erros_epoca == 0:
            break

    print("\n" + "="*115)
    print(f"{f'RESULTADO DO TREINAMENTO ATUAL - RODADA T{rodada}':^115}")
    print("="*115)
    print(f"{'Vetor de pesos iniciais':^39} | {'Vetor de pesos finais':^39} | {'Número de':<11}")
    print(f"{'w0':^8} {'w1':^8} {'w2':^8} {'w3':^8} | {'w0':^8} {'w1':^8} {'w2':^8} {'w3':^8} | {'épocas':<11}")
    print("-"*115)
    print(f"{pesos_iniciais['w_limiar']:8.4f} {pesos_iniciais['w1']:8.4f} {pesos_iniciais['w2']:8.4f} {pesos_iniciais['w3']:8.4f} | "
          f"{pesos['w_limiar']:8.4f} {pesos['w1']:8.4f} {pesos['w2']:8.4f} {pesos['w3']:8.4f} | "
          f"{epoca_atual:<11}")
    print("="*115)

    if rodada < 5:
        input(f"\nPressione ENTER para iniciar a rodada de treinamento T{rodada+1}...")
    else:
        print("\nFim das rodadas de treinamento!")