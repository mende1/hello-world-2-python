import interface
import palavras
import funcoes

def acertou():
    return tamanho == numeroAcertos


def enforcou():
    return numeroErros == ERROS_MAXIMOS


def verificaLetra(letra):
    count = 0
    for c in range(0, tamanho):
        if letra == palavraSecreta[c]:
            count += 1
            palavraUsuario[c] = letra
            palavraSecreta[c] = '.'
    return count


palavras.lerNovasPalavras()

dica = palavras.retornaDica()
palavra = palavras.retornaPalavra()
palavraSecreta = list()
funcoes.recebePalavra(palavraSecreta, palavra)

tamanho = len(palavra)

palavraUsuario = list()
numeroAcertos = 0
numeroErros = 0

letrasRepetidas = list()

tentativasUsuario = 1
ERROS_MAXIMOS = 7

funcoes.abertura()
funcoes.interfacePalavra(palavraUsuario, tamanho, dica)

while not acertou() and not enforcou():
    interface.imprimeForca(numeroErros)
    funcoes.imprimePalavra(palavraUsuario)

    print(f"Tentativa {tentativasUsuario}: ")
    print(f"Letras já escritas: {letrasRepetidas}")
    print(f"Erros: {numeroErros}\n")

    letra = funcoes.recebeLetra()

    if letra not in letrasRepetidas:
        letrasRepetidas.append(letra)

    acertos = verificaLetra(letra)

    if acertos > 0:
        numeroAcertos += acertos
    else:
        numeroErros += 1
        if not enforcou():
            funcoes.mensagemErro(numeroErros)

    if acertou():
        print("")
        funcoes.imprimePalavra(palavraUsuario)
    else:
        tentativasUsuario += 1

if acertou():
    funcoes.ganhou(numeroErros, palavra, tentativasUsuario)
    interface.imprimeVitoria()
else:
    funcoes.perdeu(palavra)
    interface.imprimeDerrota()

palavras.adicionarPalavras()
