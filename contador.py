def contador_par_impar():
    """
    Este programa solicita números inteiros ao usuário, informa se cada
    número é par ou ímpar e, no final, exibe a contagem total de cada tipo.
    O programa lida com entradas inválidas e continua até que o usuário
    digite 'fim'.
    """
    # Inicializa os contadores
    contagem_pares = 0
    contagem_impares = 0

    print("--- Contador de Pares e Ímpares ---")
    print("Insira números inteiros. Para encerrar e ver o resultado, digite 'fim'.")
    print("-" * 40)

    while True:
        entrada = input("Digite um número inteiro ou 'fim': ")

        # 1. Verifica a condição de parada
        if entrada.lower() == 'fim':
            break

        # 2. Tenta converter e processar a entrada
        try:
            # Converte a entrada para um número inteiro.
            # Se a entrada for "abc" ou "3.14", um ValueError ocorrerá.
            numero = int(entrada)

            # 3. Verifica se o número é par ou ímpar usando o operador módulo (%)
            # O resto da divisão de um número par por 2 é sempre 0.
            if numero % 2 == 0:
                print(f"-> O número {numero} é PAR.")
                contagem_pares += 1
            else:
                print(f"-> O número {numero} é ÍMPAR.")
                contagem_impares += 1

        except ValueError:
            # Captura o erro se a entrada não for um número inteiro válido
            print("Erro: Entrada inválida. Por favor, insira um número inteiro.")
        
        print("-" * 25) # Adiciona um separador para clareza

    # 4. Exibe o resumo final após o loop ser encerrado
    print("\n--- Resumo Final ---")
    print(f"Total de números PARES inseridos: {contagem_pares}")
    print(f"Total de números ÍMPARES inseridos: {contagem_impares}")
    print("-" * 40)

# Executa a função principal do programa
if __name__ == "__main__":
    contador_par_impar()