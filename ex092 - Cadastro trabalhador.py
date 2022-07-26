from datetime import date, datetime

fun = {}
print('>> CADASTRO DE FUNCIONÁRIO <<')
fun['nome'] = str(input('Nome: '))
nasc = int(input('Ano nascimento: '))
fun['carteira'] = int(input('Cateira de trabalho: ( 0 não tem ) '))
hoje = date.today().year
fun['idade'] = date.today().year - nasc

if fun['carteira'] != 0:
    fun['contratação'] = int(input('Ano de contratação: '))
    fun['salário'] = float(input('Sálario: R$ '))
    fun['aposentadoria'] = fun['contratação'] - hoje + 35 + fun['idade']
    
print('-='*25)
for k, v in fun.items():
    print(f'    - {k} é igual a {v} !')
        