while escolha_do_jogador == 'P' and numero % 2 != 0 or escolha_do_jogador == 'I' and numero % 2 == 0 :
        print ('vc deve jogar o numero de acordo com o par ou impar! tente novamente!')
        escolha_do_jogador = input('Par ou ímpar? (P/I): ').upper()
        numero = int(input('Digite um número: '))