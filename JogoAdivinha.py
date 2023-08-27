nrDeJogosJogados = 1

import random

while(nrDeJogosJogados <= 3):

    print("Weclenhos, é um Paleias que gosta de brincar com suas vitimas, porem, gosta de permitir chances de sobrevivencia, ele quer que você que você diga dois numeros!")
    
    x = int(input("Diga o primeiro numero agora!: "))
    
    y = int(input("Diga o segundo numero!: "))
    
    minimo = min(x,y)
    maximo = max(x,y)
    
    numero_pc = random.randint(minimo, maximo)
    
    nr_valido = False

    while nr_valido == False:

        palpite = int(input(f"Certo! Wesclenhos escolheu um numero aleatorio entre {minimo} e {maximo}. Agora para salvar sua vida, tente acertar qual o numero que Weclenhos escolheu!"))
        
        if palpite >= minimo and palpite <= maximo:
            
            nr_valido = True
            
        else:
            
            print(f"Tente novamente, o numero terá que estar obrigatoriamente entre {minimo} e {maximo}")
        
        
    if palpite == numero_pc:
        
        print("Parabens! Você irá sobreviver, pois acertou o numero que Weclenhos havia escolhido!")

        print("GAME WIN")

        break

    else:

        print(f"Infelizmente você errou, o numero escolhido por Weclenhos foi: {numero_pc}, porem, Weclenhos lhe dará uma segunda chance, vamos tentar novamente!")
    
    
    nrDeJogosJogados = nrDeJogosJogados + 1

if nrDeJogosJogados > 3:
    
    print("Você perdeu todas as suas chances. Prepara-se para sua MORTE!!!")

    print("GAME OVER")