import time
from função import limparTela, inicializa_letras_acertadas,limparLetras,verificaLetra, errou_letra

limparTela()

while True:
    print("Bem Vindo ao Jogo da Forca\n")
    print("(1) Jogar")
    print("(2) Sair")
    comando = str(input("-> "))

    if comando == "1":
        limparTela()
        desafiante = input("\nInsira o nome do desafiante: ")
        competidor = input("\nInsira o nome do competidor: ")
        limparTela()

        palavra = str(input("Informe a palavra Chave: "))
        palavra = verificaLetra(palavra)

        dicaA = input("\nInforme a Dica 1: ")
        dicaB = input("Informe a Dica 2: ")
        dicaC = input("Informe a Dica 3: ")

        limparTela()

        listChave = []
        dicas = [dicaA, dicaB, dicaC]
        letrasTentadas = []
        dicasPedidas = 0
        erros = int(0)
        for letra in palavra:
            listChave.append(letra)
        letras_acertadas = inicializa_letras_acertadas(palavra)

        while True:
            print('   '.join(letras_acertadas)+"\n")
            if ("_" not in letras_acertadas):
                limparTela()
                print('   '.join(letras_acertadas)+"\n")
                ganhador = (f"Palavra: {palavra} – Vencedor: Competidor {competidor} , Perdedor: Desafiante {desafiante}")
                print(f"O competidor {competidor} ganhou!!")
                input("\nPressione enter para continuar: ")
                limparTela()
                break
            if erros == 5:
                limparTela()
                print('   '.join(letras_acertadas)+"\n")
                ganhador = (f"Palavra: {palavra} – Vencedor: Desafiante {desafiante} , Perdedor: Competidor {competidor}")
                print(f"O desafiante {desafiante} ganhou!!")
                print(f"A palavra chave era {palavra}")
                input("\nPressione enter para continuar: ")
                limparTela()
                break
                
            print("\nEscolha uma das opções:")
            print("(1) Jogar")
            print("(2) Solicitar Dica\n")
            escolha = str(input("-> "))
            limparTela()
            print('   '.join(letras_acertadas)+"\n")

            if escolha == "1":
                while True:
                    print("Digite uma letra: ")
                    chute = input("->")
                    chute = limparLetras(chute)
                    if not chute in letrasTentadas:
                        if chute.isalpha():
                            letrasTentadas.append(chute)
                            if (chute in listChave):
                                index = 0 
                                for letra in listChave:
                                    if (chute == letra):
                                        letras_acertadas[index] = letra
                                    index += 1
                                limparTela()
                                break
                            else:
                                erros = erros + 1
                                errou_letra(erros)
                                break
                        else:print("Digite somente letras!\n")
                    else:
                        print("Você já digitou esta letra!\n")
                
            elif escolha == "2":
                if dicasPedidas < 3:
                    print(f"Dica {dicasPedidas+1}: {dicas[dicasPedidas]}\n")
                    dicasPedidas +=1
                    while True: 
                        chute = (input("Digite uma letra: "))
                        chute = limparLetras(chute)
                        if not chute in letrasTentadas:
                            if chute.isalpha():
                                letrasTentadas.append(chute)
                                if (chute in listChave):
                                    index = 0 
                                    for letra in listChave:
                                        if (chute == letra):
                                            letras_acertadas[index] = letra
                                        index += 1
                                    limparTela()
                                    break
                                else:
                                    erros = erros + 1
                                    errou_letra(erros)
                                    break
                            else: print("Apenas letras devem ser digitadas!\n")
                        else: print("Você já tentou esta letra!\n")
                else:
                    limparTela()
                    print("Suas dicas acabaram!\n")
            else:
                limparTela()
                print("Nenhuma das opções selecionadas.\n")

        while True:
            limparTela()
            try:
                print("\n")
                arquivo = open('arquivo.txt','a')
                arquivo.write(ganhador + "\n")
                arquivo.close()
                
                arquivo = open('arquivo.txt','r')
                limparTela()
                print("Histórico de partidas:\n")
                for linha in arquivo:
                    linha = linha.rstrip()
                    print (linha)
                arquivo.close()
                input("\nPressione enter para continuar: ")
                limparTela()
                break
                
            except:
                arquivo = open('arquivo.txt','w')
                arquivo.close()
            
    elif(comando == "2"):
        print("\nVocê escolheu sair!")
        time.sleep(2)
        limparTela()
        break

    else:
        limparTela()
        print("Selecione uma das opções!\n")
