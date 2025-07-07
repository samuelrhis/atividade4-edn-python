def calculadora():
    while True:
        try:
            num1_str = input("Insira o primeiro número: ")
            operacao = input("Insira a operação (+, -, *, /): ")
            num2_str = input("Insira o segundo número: ")

            num1 = float(num1_str)
            num2 = float(num2_str)

            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                resultado = num1 / num2
            else:
                print("\nErro: Operação inválida. As opções são +, -, *, /.\n")
                continue

            print("-" * 30)
            print(f"O resultado de {num1} {operacao} {num2} é: {resultado}")
            print("-" * 30)
            break

        except ValueError:
            print("\nErro: Entrada inválida. Por favor, certifique-se de inserir apenas números.\n")

        except ZeroDivisionError:
            print("\nErro: A divisão por zero não é permitida.\n")

if __name__ == "__main__":
    calculadora()