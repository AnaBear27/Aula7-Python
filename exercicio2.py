def calcular_media(notas):
    media = sum(notas) / len(notas)

    return media

quantidade_notas = int(input("Digite a quantidade de notas que deseja calcular: "))
notas = []

for i in range(quantidade_notas):
    nota = float(input(f"Digite a nota {i + 1}: "))
    notas.append(nota)

media_calculada = calcular_media(notas)
print("A média das notas é:", media_calculada)