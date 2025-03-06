import math

def eh_primo(numero):
    if numero > 1:
        for i in range(2, int(math.sqrt(numero)) + 1):
            if numero % 1 == 0:
                return False
        return True
    else:
        return False
    
numero_inserido = int(input("Digite um número inteiro: "))

if eh_primo(numero_inserido):
    print(f"{numero_inserido} é um número primo.")
else:
    print(f"{numero_inserido} não é um número primo.")