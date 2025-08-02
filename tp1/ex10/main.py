def main():
    opiniao = 'Serviço excelente aluno Marcos Ryan Silva Santos, voltarei a comprar!'
    print(f'Caracteres: {len(opiniao)}')
    print(f'Caracter A: {opiniao.count('a')}') # count, diferente do dito no enunciado, conta as ocorrencias de determinada string
    print(f'Palavras na Frase: {len(opiniao.split())}') # seria mais correto para contas as palavras
    
    # Há uma forma que é possível fazer funcionar o count com:
    print(f'Palavras na Frase: {opiniao.count('a') +1}')
    
if __name__ == "__main__":
    main()