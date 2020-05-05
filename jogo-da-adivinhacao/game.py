from random import randint

def apresentacao():
    print("*****************************************")
    print("*   Bem-vindo ao jogo de adivinhação!   *")
    print("*****************************************")

def recebeAleatorio():
    return randint(1, 100)

def recebeUsuario():
    usuario = int(input("Pensei em um número de 1 a 100, tente advinhá-lo: "))
    return usuario

def validaUsuario(usuario):
    if usuario < 1 or usuario > 100:
        print("\nVocê digitou um número INVÁLIDO!")
        print("Tente um número entre 1 e 100.\n")
        return False
    else:
        return True

def recebeDificuldade():
    print("Escolha o nível de dificuldade!")
    print("(1) Fácil    (2) Médio    (3) Difícil\n")

    dificuldade = int(input("Qual a dificuldade? "))

    if dificuldade not in [1, 2, 3]:
        print("Dificuldade inválida! Tente novamente.\n")
        dificuldade = recebeDificuldade()
    else:
        return dificuldade

def defineDificuldade(dificuldade):
    if dificuldade == 1: return 20
    elif dificuldade == 2: return 12
    else: return 6

def mensagemDificuldade(dificuldade):
    print("")
    if dificuldade == 1: 
        print("Você selecionou a dificuldade: Fácil")
        print("E por isso, tem 20 chances para acertar o número!")
    elif dificuldade == 2:
        print("Você selecionou a dificuldade: Médio")
        print("E por isso, tem 12 chances para acertar o número!")
    else: 
        print("Você selecionou a dificuldade: Difícil")
        print("E por isso, tem 6 chances para acertar o número!")
    print()

def acertou():
    if numeroAleatorio == numeroUsuario: 
        return True
    else: return False

def perdeu():
    if tentativasUsuario > tentativasMaximas: 
        return True
    else: return False

def maior():
    if numeroAleatorio > numeroUsuario: return True
    else: return False

def mensagemAcertou():
    print("Meus parabéns! Você ACERTOU!")
    print(f'O número sorteado foi {numeroAleatorio}.\n')
    print(f'Você acertou o número na {tentativasUsuario}ª tentativa.')
    print(f'Obteve um total de {pontosUsuario} pontos.\n')

def mensagemPerdeu():
    print("Você atingiu o número máximo de tentativas.")
    print("E por isso, você PERDEU!! ... Tente novamente ...\n")

apresentacao()

dificuldade = recebeDificuldade()
tentativasMaximas = defineDificuldade(dificuldade)
mensagemDificuldade(dificuldade)

tentativasUsuario = 1
pontosUsuario = 1000

numeroAleatorio = recebeAleatorio()

while tentativasUsuario <= tentativasMaximas:
    print(f"Tentativa {tentativasUsuario}:")
    numeroUsuario = recebeUsuario()
    if not validaUsuario(numeroUsuario):
        tentativasUsuario -= 1

    elif not acertou():
        print("Errou!", end=' ')
        if maior():
            print("Tente um número MAIOR\n")
        else:
            print("Tente um número MENOR\n")

        pontosUsuario -= (abs(numeroUsuario - numeroAleatorio) / 2.0)

    elif acertou():
        break
    
    tentativasUsuario += 1

print("\n... FIM DE JOGO! ...\n")

if acertou(): 
    mensagemAcertou()
else: 
    mensagemPerdeu()