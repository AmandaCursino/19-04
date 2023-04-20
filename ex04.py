while True:
    try: 
        numero = int(input('Entre com um numero: '))
        print(numero/2)
        break
    except:
        print('O numero que voce inseriu não é valido, tente novamente.')