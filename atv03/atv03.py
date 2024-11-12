
senha = "7"
tentativas = 3

while tentativas > 0:
    advinhar = input('advinhe a senha: ')
    if advinhar == senha:
        print("certô")
        break
    else:
        tentativas -= 1
        if tentativas > 0:
            print(f'errou, você tem mais {tentativas} tentativas')
        else:
            print('acabou as tentativas main:/ sorrys')