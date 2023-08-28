# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

lista = ["pedra", "papel", "tesoura"]
print('''
COMPUTADOR: Vamos jogar pedra, papel, tesoura!
As regras são as seguintes:
- Papel vence pedra e perde para tesoura
- pedra vence tesoura e perde para papel
- tesoura vence papel e perde para pedra  
''')
jogador = str(input("Você escolhe pedra, papel ou tesoura? \n")).lower()
print("JO")
print(0.50)
print("KEN")
print(0.50)
print("PÔ!!!")

computador = (lista)
vencedor = ""
print('''
jogador:{}
computador: {}'''.format(jogador, computador))
if (jogador != "pedra" and jogador != str("papel") and jogador != str("tesoura")):
    print("{} não é uma opção válida. Escolha pedra, papel ou tesoura.".format(jogador))
elif jogador == computador:
    print("Empate. Vamos jogar novamente.")

elif jogador == "pedra" and computador == "tesoura":
    print("pedra vence tesoura. jogador ganhou.")
elif jogador == "tesoura" and computador == "pedra":
    print("pedra vence tesoura. computador ganhou.")

elif jogador == "pedra" and computador == "papel":
    print("papel vence pedra. computador ganhou.")
elif jogador == "papel" and computador == "pedra":
    print("papel vence pedra. jogador ganhou.")

elif jogador == "tesoura" and computador == "papel":
     print("papel vence tesoura. computador ganhou.")
elif jogador == "papel" and computador == "tesoura":
    print("papel vence teoura. jogador ganhou.")