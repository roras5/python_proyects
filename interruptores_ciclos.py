def run():
    '''
    for contador in range(0,999):
        if contador % 2!= 0:
            continue
        print(contador)

    for i in range (0,10000):
        if i == 5678:
            break
        print(i)
     '''
    LIMITE = 10000
    contador = 1
    while LIMITE > contador:
        if contador % 2 == 0:
            print(contador)
        if contador == 9972:
            break
       # else: continue
        contador += 1


if __name__ == "__main__":
    run()
