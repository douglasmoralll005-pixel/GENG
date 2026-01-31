frase = input('Informe uma frase: ')

palavras = len(frase.strip())

print(f'O texto digitado tem {palavras} caracteres')
if palavras == 0 : print('Você realmente digitou algo?\nEspaços em brancos não são considerados!!')