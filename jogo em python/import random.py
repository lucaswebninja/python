import random

numero = random.randint(1, 100)
tentativas = 0

print("bem-Vindo ao jogo da adivinhação!")
print("Eu escolhi um número entre 1 e 100. Você tem 10 tentativas para adivinhar.")

while tentativas < 10:
    palpite = int(input("Digite o seu palpite: "))
    tentativas += 1

    if palpite == numero:
        print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
    elif palpite < numero:
        print("o número é maior. Tente novamente.")
    else:
        print("O número é menor. tente novamente.")
else:
    print(f"Você perdeu! O número era {numero}.")                