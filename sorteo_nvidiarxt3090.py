import random
def run():
    number_winner = random.randint(1, 10)
    for i in range(1,11):
        print(i)
    ticket = int(input('Eliga un numero para el sorteo: '))
    while ticket != number_winner:
        print('Sigue intentandolo')
        ticket = int(input('Escoga otro numero: '))
    print('Ganaste una RXT 3090 FULL HD')
if __name__ == '__main__':
    run()