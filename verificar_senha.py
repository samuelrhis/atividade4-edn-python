def verificar_senha():
    """
    Este programa solicita ao usuário que crie uma senha e verifica se ela
    atende aos critérios de uma senha forte:
    - Pelo menos 8 caracteres de comprimento.
    - Contém pelo menos um número.
    O programa continua até que uma senha forte seja inserida ou o usuário
    digite 'sair'.
    """
    print("--- Verificador de Senha Forte ---")
    print("Uma senha forte deve ter no mínimo 8 caracteres e conter ao menos um número.")
    print("-" * 36)

    while True:
        senha = input("Crie uma senha ou digite 'sair' para encerrar: ")

        # Condição de saída do programa
        if senha.lower() == 'sair':
            print("Programa encerrado.")
            break

        # Verificando as duas condições para a senha ser forte
        tem_comprimento_suficiente = len(senha) >= 8
        tem_numero = any(char.isdigit() for char in senha)

        # Se ambas as condições forem verdadeiras, a senha é forte
        if tem_comprimento_suficiente and tem_numero:
            print("\n>> Senha forte criada com sucesso! <<\n")
            break
        # Se não for forte, informa o(s) motivo(s)
        else:
            print("\nSenha fraca. Por favor, tente novamente.")
            if not tem_comprimento_suficiente:
                print("- Motivo: A senha deve ter no mínimo 8 caracteres.")
            if not tem_numero:
                print("- Motivo: A senha deve conter pelo menos um número (0-9).")
            print("-" * 36)


# Executa o programa
if __name__ == "__main__":
    verificar_senha()