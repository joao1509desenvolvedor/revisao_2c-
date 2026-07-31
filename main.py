nome = input('Digite seu nome')
nota1 = float(imput('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))

def calcular_media(nota1, nota2):
    return (nota1 + nota2)/ 2

media = calcular_media(nota1, nota2)
print(f'sua média é {media}')