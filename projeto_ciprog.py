print("===================================")
print("\033[1m JOGO: MISSÃO CULTURA DA PAZ\033[0m")
print("===================================")

nome = input("Digite seu nome: ")

print(f"\nOlá, {nome}!")
print("Hoje você viverá um dia inteiro na escola.")
print("Suas escolhas irão mudar a história.\n")

pontos = 0
vidas = 3
inventario = []

jogando = True

while jogando and vidas > 0:

    # ---------------- FASE 1 ----------------
    print("\n========== FASE 1 ==========")
    print("Você chegou na escola e viu dois colegas discutindo.")

    print("\nO que você faz?")
    print("1 - Tenta separar a briga")
    print("2 - Começa a filmar")
    print("3 - Vai embora")

    escolha1 = input("Escolha: ")

    if escolha1 == "1":
        print("\nVocê tentou conversar com os colegas.")
        print("A situação melhorou.")
        pontos += 10

    elif escolha1 == "2":
        print("\nOs colegas ficaram mais nervosos.")
        print("Você perdeu pontos.")
        pontos -= 5
        vidas -= 1

    elif escolha1 == "3":
        print("\nVocê ignorou a situação.")
        pontos += 0

    else:
        print("\nEscolha inválida.")
        continue

    print(f"\nPontos: {pontos}")
    print(f"Vidas: {vidas}")

    # ---------------- FASE 2 ----------------
    print("\n========== FASE 2 ==========")
    print("Na sala, um colega esqueceu o material.")

    print("\nO que você faz?")
    print("1 - Empresta seu material")
    print("2 - Diz que não é problema seu")
    print("3 - Ri da situação")

    escolha2 = input("Escolha: ")

    if escolha2 == "1":
        print("\nVocê ajudou o colega.")
        pontos += 15
        inventario.append("amizade")

    elif escolha2 == "2":
        print("\nVocê decidiu não ajudar.")
        pontos -= 2

    elif escolha2 == "3":
        print("\nO colega ficou triste.")
        pontos -= 10
        vidas -= 1

    else:
        print("\nEscolha inválida.")
        continue

    print(f"\nPontos: {pontos}")
    print(f"Vidas: {vidas}")

    # ---------------- FASE 3 ----------------
    print("\n========== FASE 3 ==========")
    print("Hora do trabalho em grupo.")

    integrantes = ["Ana", "Lucas", "Maria", "Pedro"]

    print("\nSeu grupo:")
    for pessoa in integrantes:
        print("-", pessoa)

    print("\nUma discussão começou no grupo.")

    print("1 - Organizar as tarefas")
    print("2 - Discutir com todos")
    print("3 - Não participar")

    escolha3 = input("Escolha: ")

    if escolha3 == "1":
        print("\nO grupo conseguiu trabalhar junto.")
        pontos += 20
        inventario.append("liderança")

    elif escolha3 == "2":
        print("\nA discussão piorou.")
        pontos -= 10
        vidas -= 1

    elif escolha3 == "3":
        print("\nO grupo ficou desorganizado.")
        pontos -= 5

    else:
        print("\nEscolha inválida.")
        continue

    print(f"\nPontos: {pontos}")
    print(f"Vidas: {vidas}")

    # ---------------- FASE 4 ----------------
    print("\n========== FASE 4 ==========")
    print("Você encontrou um celular perdido no corredor.")

    print("\nO que fazer?")
    print("1 - Entregar para coordenação")
    print("2 - Guardar para você")
    print("3 - Procurar o dono")

    escolha4 = input("Escolha: ")

    if escolha4 == "1":
        print("\nA coordenação agradeceu sua honestidade.")
        pontos += 20
        inventario.append("honestidade")

    elif escolha4 == "2":
        print("\nIsso foi uma atitude errada.")
        pontos -= 20
        vidas -= 2

    elif escolha4 == "3":
        print("\nVocê encontrou o dono do celular.")
        pontos += 15

    else:
        print("\nEscolha inválida.")
        continue

    print(f"\nPontos: {pontos}")
    print(f"Vidas: {vidas}")

    # ---------------- FASE 5 ----------------
    print("\n========== FASE 5 ==========")
    print("Última aula do dia.")

    print("\nO professor pediu uma apresentação em grupo.")

    print("1 - Incentivar todos a participar")
    print("2 - Fazer tudo sozinho")
    print("3 - Não ajudar")

    escolha5 = input("Escolha: ")

    if escolha5 == "1":
        print("\nO grupo trabalhou unido.")
        pontos += 25

    elif escolha5 == "2":
        print("\nVocê ficou sobrecarregado.")
        pontos += 5

    elif escolha5 == "3":
        print("\nO grupo não conseguiu terminar.")
        pontos -= 15
        vidas -= 1

    else:
        print("\nEscolha inválida.")
        continue

    # ---------------- FINAL ----------------
    print("\n===================================")
    print(" RESULTADO FINAL ")
    print("===================================")

    print(f"\nJogador: {nome}")
    print(f"Pontos finais: {pontos}")
    print(f"Vidas restantes: {vidas}")

    print("\nItens conquistados:")
    for item in inventario:
        print("-", item)

    # finais diferentes
    if pontos >= 70 and vidas >= 2:
        print("\nFINAL PERFEITO")
        print("Você demonstrou respeito, empatia e liderança.")
        print("Sua escola ficou mais unida graças às suas atitudes.")

    elif pontos >= 40:
        print("\nFINAL BOM")
        print("Você tomou boas decisões na maior parte do tempo.")

    elif pontos >= 10:
        print("\nFINAL NEUTRO")
        print("Algumas escolhas poderiam ter sido moelhores.")

    else:
        print("\nFINAL NEGATIVO")
        print("Os conflitos aumentaram durante o dia.")

    # jogar novamente
    print("\nDeseja jogar novamente?")
    repetir = input("Digite sim ou nao: ")

    if repetir == "sim" or repetir == "s":
        pontos = 0
        vidas = 3
        inventario = []
        print("\nReiniciando jogo...\n")

    else:
        jogando = False

print("\nObrigado por jogar!")
print("Fim do jogo.")