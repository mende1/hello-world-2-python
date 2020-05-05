from random import randint

minhasPalavras = { 
    'dicas': 
        ['FRUTAS', 'ANIMAIS', 'NOMES'],
    'palavras': 
    [
        [
        'MELANCIA','MELAO','MARACUJA','MORANGO','MAÇA','LIMAO','BANANA','PERA','UMBU','UVA','ACAI','ABACAXI','ABACATE','TOMATE','TANGERINA','LARANJA','TAMARINDO','SERIGUELA','PEQUI','PESSEGO','PINHA','PITANGA','MANGA','MAMAO','LICHIA','KIWI','JABUTICABA','JACA','GRAVIOLA','GROSELIA','GOIABA','FIGO','CACAU','CAJA','CUPUACU','CAJU','CARAMBOLA','COCO','CAQUI','BURITI','AZEITONA','ACEROLA','ABOBORA','MANDIOCA','AIPIM','MACAXEIRA','MANGA'
        ],

        [
        'BALEIA','CACHORRO','CAVALO','COBRA','CROCODILO','ELEFANTE','FRANGO','GALINHA', 'GAMBA','GATO','GOLFINHO','LEAO','GIRAFA','LOBO','MACACO','OVELHA','PAPAGAIO','POLVO','POMBO','RINOCERONTE','TARTARUGA','TOURO','URSO','VACA'
        ],

        [
        'HELENA','MIGUEL','ALICE','ARTHUR','LAURA','HEITOR','MANUELA','BERNARDO','VALENTINA','DAVI','SOPHIA','THEO','ISABELLA','LORENZO','HELOISA','GABRIEL','LUIZA','PEDRO','JULIA','BENJAMIN','LORENA','MATHEUS','LIVIA','LUCAS','MARIA','LUIZA','NICOLAS','CECILIA','JOAQUIM','ELOA','SAMUEL','GIOVANNA','HENRIQUE','MARIA','CLARA','RAFAEL','MARIA','EDUARDA','GUILHERME','MARIANA','ENZO','LARA','MURILO','BEATRIZ','BENICIO','ANTONELLA','GUSTAVO','MARIA','JULIA','ISAAC','EMANUELLY','JOAO','ISADORA','LUCCA','ANA','CLARA','ENZO','MELISSA','PEDRO','HENRIQUE','LUIZA','FELIPE','JULIA','JOAO','PEDRO','ESTHER','PIETRO','LAVINIA','ANTHONY','MAITE','DANIEL','CECILIA','BRYAN','ALICE','DAVI','LUCCA','SARAH','LEONARDO','ELISA','VICENTE','LIZ','EDUARDO','YASMIN','GAEL','ISABELLY','ANTONIO','ALICIA','VITOR','CLARA','NOAH','ISIS','CAIO','REBECA','JOAO','RAFAELA','EMANUEL','MARINA','CAUA','ANA','JOAO','MARIA','CALEBE','AGATHA','ENRICO','GABRIELA','VINICIUS','CATARINA'
        ]
    ]
}


def adicionarPalavras():
    adicionar = input("\nDeseja adicionar uma palavra? [s/n] ")
    while adicionar not in 'nNsS':
        print("comando errado!", end='')
        adicionar = input("\nDeseja adicionar uma palavra? [s/n] ")
    if adicionar in 'sS':
        print("Qual a dica para a nova palavra? ")
        novaDica = str(input("[Frutas/Animais/Nomes] ")).upper()

        while novaDica not in ['FRUTAS', 'ANIMAIS', 'NOMES']:
            print("dica inválida")
            novaDica = str(input("[Frutas/Animais/Nomes] ")).upper()

        numeroId = minhasPalavras['dicas'].index(novaDica)
    
        arquivo = open("novasPalavras.txt", "a")
        arquivo.write(f"\n{numeroId}\n")

        novaPalavra = str(input("Qual a nova palavra? ")).upper()
        arquivo.write(f"{novaPalavra}\n")

        arquivo.close()

        print(f"\nPalavra {novaPalavra} adicionada com sucesso na lista de '{novaDica}'", end='')

    print("\n... FIM DE JOGO! ...\n")


def lerNovasPalavras():
    arquivo = open("novasPalavras.txt", "r")

    for i in arquivo:
        novaDica = arquivo.readline()
        dicaId = novaDica[0]
        novaPalavra = arquivo.readline().upper()
        minhasPalavras['palavras'][int(dicaId)].append(novaPalavra.strip())

    arquivo.close()


def defineDica():
    dicas = randint(0, len(minhasPalavras['dicas'])-1)
    return dicas


dicas = defineDica()


def retornaDica():
    return minhasPalavras['dicas'][dicas]


def retornaPalavra():
    palavras = randint(0, len(minhasPalavras['palavras'][dicas])-1)
    return minhasPalavras['palavras'][dicas][palavras]
