n = int(input())

#este corolário matemático não tem solução há 80 anos. Ele diz que:

while n !=1: #se n for diferente de 1, iniciamos o algoritmo
    if n%2 == 0: #sendo n par, dividimos ele por dois
        n = n/2
        print(n)
    else:
        n = n*3 + 1 #sendo n ímpar, multiplicamos por 3 e somamos 1
        print(n)
        
#impressionantemente, para qualquer valor natural, o algoritmo chega ao resultado '1'
