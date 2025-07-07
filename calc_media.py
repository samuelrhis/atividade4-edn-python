def registrar_notas_turma():
    """
    Este programa registra as notas de uma turma, valida as entradas e,
    ao final, calcula e exibe a média das notas válidas.
    """
    notas_validas = []
    print("--- Sistema de Registro de Notas ---")
    print("Digite as notas dos alunos (0 a 10).")
    print("Para concluir e calcular a média, digite 'fim'.")
    print("-" * 35)

    while True:
        entrada = input("Digite uma nota ou 'fim': ")

        # 1. Verifica se o professor deseja encerrar o programa
        # Usamos .lower() para aceitar 'fim', 'Fim', 'FIM', etc.
        if entrada.lower() == 'fim':
            break

        # 2. Tenta converter a entrada para um número e validar
        try:
            nota = float(entrada)

            # 3. Verifica se a nota está no intervalo válido (0 a 10)
            if 0 <= nota <= 10:
                notas_validas.append(nota)
                print(f"Nota {nota} registrada com sucesso.")
            else:
                # Informa que a nota está fora do intervalo permitido
                print("Erro: Nota inválida. O valor deve estar entre 0 e 10.")

        except ValueError:
            # Informa que a entrada não é um número válido
            print("Erro: Entrada inválida. Por favor, digite um número ou 'fim'.")

    # 4. Após o loop, calcula e exibe o resultado final
    print("\n" + "-" * 35)
    print("Registro de notas finalizado.")

    # Verifica se alguma nota foi inserida para evitar divisão por zero
    if notas_validas:
        media_turma = sum(notas_validas) / len(notas_validas)
        total_de_notas = len(notas_validas)

        print(f"Total de notas válidas registradas: {total_de_notas}")
        # Formata a média para exibir apenas duas casas decimais
        print(f"A média da turma é: {media_turma:.2f}")
    else:
        print("Nenhuma nota válida foi registrada para calcular a média.")
    print("-" * 35)

# Executa o programa
if __name__ == "__main__":
    registrar_notas_turma()