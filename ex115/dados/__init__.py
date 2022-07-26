from interface import titulo

def arq_existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except:
        return False
    else:
        return True

def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO ao criar o arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso.')

def ler_arquivo(nome):
    try:
        titulo('pessoas cadastradas')
        a = open('jujuba.txt', 'r')
    except:
        print('Erro ao ler o arquivo.') 
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30} {dado[1]:>3} anos')
    finally:
        a.close()

def criar_cadastro(aqr, nome='desconhecido', idade=0):
    try:
        a = open(aqr, 'at')
        a.writelines(f'{nome};{idade}\n')
    except:
        print('Houve um erro durante o cadastro.')
        print(Exception.__class__)
    else:
        print(f'Novo registo {nome} realizado.')
    finally:
        a.close()
    
