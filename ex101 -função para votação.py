def titulo(msg):
    tam = len(msg) + 8
    print('~' * tam)
    print(f'    {msg}')
    print('~' * tam)


def voto(idade):
    from datetime import date
    hoje = date.today().year
    idade = hoje - nasc
    print(f'Você tem {idade} anos:', end=' ')
    if idade < 16:
        print(f'NÂO VOTA !')
    elif  16 <= idade <= 18 or idade >= 70:
        print('VOTO OPCIONAL !')
    elif idade > 18 and idade < 70:
        print('VOTO OBRIGATÓRIO')


titulo('VOTAÇÂO')
nasc = int(input('Qual seu ano de nascimento? '))
voto(nasc)