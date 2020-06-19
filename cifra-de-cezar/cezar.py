def presentation():
	print('========================')
	print('=====CIFRA=DE=CEZAR=====')
	print('========================')
	

def get_word():
	print('Digite o texto a ser criptografado: ')
	word = input()

	return word


def get_key():
	print('\nQual a rotação? [de 1 até 25]')
	print('Digite zero (0) para mostrar todas as rotações! ')

	key = int(input('\nChave: '))

	if key < 0 or key > 25:
		print("Rotação inválida! Digite uma entre 0 a 25 ...")
		key = get_key()

	return key


def print_cezar(key):
	
	for i in range(len(word)):
		caps = 0
		letter = word[i]

		for j in range(len(alphabet)):
			pointer = -1

			if letter == alphabet[j]:
				pointer = j
				break
			
		if pointer == -1:
			caps = 1
			for j in range(len(ALPHABET)):
				pointer = -1

				if letter == ALPHABET[j]:
					pointer = j
					break
		
		goal = (pointer + key)

		if goal > 25:
			goal -= 26

		while pointer != goal:
			if pointer == 26:
				pointer = 0

			else:
				pointer += 1

		if caps == 0:
			cezar = alphabet[pointer]

		else:
			cezar = ALPHABET[pointer]

		print(cezar, end='')
	print()
	

presentation()

word = get_word()
key = get_key()

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

if key != 0:
	print('\nTexto decifrado: ')
	print_cezar(key)

else:
	print('Textos decifrados: \n')

	for k in range(1, 26):
		print(f'Rotação {k:2}: ', end='')
		key = k
		print_cezar(key)
