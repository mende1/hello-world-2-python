# Jogo-da-forca

**_O computador escolherá, de maneira randômica, uma palavra que está salva em um arquivo de palavras, e o jogador deve chutar, letra por letra, até adivinhar a palavra._**

_Se o jogador chutar 6 letras erradas, ele perde. Ao final, o computador oferecerá a possibilidade do usuário inserir uma nova palavra no banco de dados._

## Com o jogo feito, a ideia é aprender em linguagem Python:

- Criar, varrer e manipular arrays e dicionários
- Entender e criar funções que recebem parâmetros e devolvem valores.
- Ler e escrever arquivos com formatos específicos.
- Aprender mais boas práticas de código, como a criação e extração de funções para evitar repetição de código.

## Mecanismo de adicionar novas palavras e novo mecanismo de dicas

O programa já veio preparado com um banco de dados enorme de palavras para sortear. Uma mudança interessante dessa versão 'Python'
para a versão do jogo feita em 'c', é que aqui foi implementado um mecanismo de dicas, em que foi feito um dicionário, e em 'dicas'
foi adicionado 3 delas: frutas, animais, e nomes de pessoas. Ao final do jogo, ele irá perguntar se o usuário deseja adicionar
alguma palavra com alguma das 3 dias.

Para tal mecanismo funcionar, foi criado um arquivo `novasPalavras.txt` para armazenar os nomes adicionados pelo usuário, que todas
elas irão ficar lá, com a ajuda da função em Python `open()`, a partir daí, podemos escrever, sobrescrever e ler dados de algum
arquivo, neste caso, `novasPalavras.txt`.

Ao adicionar uma nova palavra, é usado um sistema de identificação das dicas: [0] para frutas, [1] animais e por fim [2] para os
nomes de pessoas. Desta maneira toda vez que um usuário adicionar uma nova palavra, no arquivo ficará assim:

```
[id das dicas]
[nova palavra]

```
Exemplo:

```
0
Morango
1
Baleia
2 
Gustavo
```

Deste jeito, toda vez que o programa rodar, além de carregar o dicionário com as palavras e dicas pré-definidas, ele irá 
rodar a função criada `lerNovasPalavras()`, que irá abrir o arquivo das palavras, ler o índicie das dicas, e adicionando as
novas palavras de acordo.

Ou seja, toda vez que o programa for executado, irá contar com uma gama de palavras novas, assim como uma dica, que irá
facilitar a vida do jogador, e dando uma maior dinâmica para o jogo.
