tabuleiro=[]

for i in range(5):
    linha=[]
    for j in range(5):
        linha.append('~') #REPRESENTA A AGUA
    tabuleiro.append(linha)

def mostrar_tabuleiro():
    for linha in tabuleiro:
        print(" ".join(linha))

navio_linha=2
navio_coluna=3

mostrar_tabuleiro()
acertou=False
while acertou==False:

    linha_tiro= int(input("Escolha a linha de 0 a 4: "))
    coluna_tiro= int(input("Escolha a coluna de 0 a 4: "))

    if linha_tiro== navio_linha and coluna_tiro== navio_coluna:
        print("ACERTOU O NAVIO!")
        tabuleiro[linha_tiro][coluna_tiro] = "X"
        acertou=True
    else:
        print("ACERTOU NA ÁGUA!")
        tabuleiro[linha_tiro][coluna_tiro]= "O"

    mostrar_tabuleiro()