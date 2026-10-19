import time

# 1. Definimos a função no topo do código
def exibir_tabuada(numero):
    print(f"\n--- Tabuada do {numero} ---")
    # range(1, 11) vai do 1 até o 10
    for c in range(1, 11):
        resultado = c * numero
        print(f"{numero} x {c:2d} = {resultado}")
    print("-" * 22)

# 2. Tratamento de exceção cobrindo o loop
try:
    while True:
        # Entrada de dados
        soma = int(input("\nDigite o número da tabuada que deseja (ou 0 para sair): "))
        
        # Condição para quebrar o loop
        if soma == 0:
            print("Programa encerrado. Até mais!")
            break
            
        print("Processando dados...")
        time.sleep(1.0)
        
        # Chamada da função que imprime a tabuada inteira
        exibir_tabuada(soma)

except ValueError:
    print("\nErro! Digite apenas números inteiros válidos.")