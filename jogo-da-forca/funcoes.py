def abertura():
    print("\n*************************")
    print("/*    Jogo da forca    */")
    print("*************************\n")


def imprimePalavra(palavra):
    for letra in palavra:
        print(f"{letra} ", end=' ')
    print("\n")


def recebeLetra():
    letra = str(input("Qual a letra? "))

    while len(letra) != 1:
        print("Entrada inválida.")
        letra = str(input("Qual a letra? "))
    return letra.upper()


def recebePalavra(lista, palavra):
    for c in palavra:
        lista.append(c)


def interfacePalavra(palavra, tamanho, dica):
    for i in range(0, tamanho):
        palavra.append('_')
    print(f"A palavra tem {tamanho} letras.")
    print(f"A dica é:    {dica}    ")


def ganhou(erros, palavra, tentativasUsuario):
    print(f"Você ACERTOU! A palavra era {palavra}")

    if erros == 1:
        print(f"Teve um total de {tentativasUsuario} tentativas e {erros} erro.\n")
    else:
        print(f"Teve um total de {tentativasUsuario} tentativas e {erros} erros.\n")


def perdeu(palavra):
    print(f"\nVocê PERDEU! A palavra era {palavra}")
    print("Atingiu o número máximo de erros 7\n")


def mensagemErro(erros):
    if erros == 1:
        print(f"Você ERROU! Já foram {erros} erro.")
    else:
        print(f"Você ERROU! Já foram {erros} erros.")
