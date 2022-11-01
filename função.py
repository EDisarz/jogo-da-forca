import os 
import random

def limparTela():
    os.system("cls")

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def limparLetras(item):
    return item.upper().replace(" ","")

def verificaLetra(palavra):
    while not palavra.isalpha():
        print("\nErro, informe apenas letras!\n")
        palavra = str(input("Informe a palavra Chave: "))
    return palavra.upper()

def errou_letra(erros):
    print("você errou a letra")