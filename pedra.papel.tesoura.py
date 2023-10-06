soma1 = 0
soma2 = 0
for x in range(3):
    jogador1 = input("Jogador 1 faça sua escolha: pedra, papel ou tesoura? ")
    while jogador1 != "pedra" and jogador1 != "papel" and jogador1 != "tesoura":
        jogador1 = input("INVÁLIDO! Tente novamente, pedra, papel ou tesoura: ")
    jogador2 = input("Jogador 2 faça sua escolha: pedra, papel ou tesoura: ")
    while jogador2 != "pedra" and jogador2 != "papel" and jogador2 != "tesoura":
        jogador2 = input("INVÁLIDO! Tente novamente, pedra, papel ou tesoura: ")

    if jogador1 == jogador2:
        print("EMPATE")
    elif jogador1 == "pedra":
        if jogador2 == "papel":
            soma2 += 1
            print(f"Papel vence pedra. Ponto jogador 2. Placar [J1]{soma1}x{soma2}[J2]")
        else:
            soma1 += 1
            print(f"Pedra vence tesoura. Ponto jogador 1. Placar [J1]{soma1}x{soma2}[J2]")
    elif jogador1 == "papel":
        if jogador2 == "pedra":
            soma1 += 1
            print(f"Papel vence pedra. Ponto jogador 1. Placar [J1]{soma1}x{soma2}[J2]")
        else:
            soma2 += 1
            print(f"Tesoura vence papel. Ponto jogador 2. Placar [J1]{soma1}x{soma2}[J2]")
    elif jogador1 == "tesoura":
        if jogador2 == "papel":
            soma1 += 1
            print(f"Tesoura vence papel. Ponto jogador 1. Placar [J1]{soma1}x{soma2}[J2]")
        else:
            soma2 += 1
            print(f"Pedra vence tesoura. Ponto jogador 2. Placar [J1]{soma1}x{soma2}[J2]")

if soma1 == 2 or soma == 3:
    print("Vencedor jogador 1!")
elif soma2 == 2 or soma == 3:
    print("Vencedor jogador 2!")