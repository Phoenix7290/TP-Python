def extrair_codigos(mensagem):
    codigos = []
    i = 0
    while i < len(mensagem):
        if mensagem[i] == "@":
            j = i + 1
            while j < len(mensagem) and mensagem[j] != "#":
                j += 1
            if j < len(mensagem):
                trecho = mensagem[i+1:j]
                codigo_limpo = ""
                for char in trecho:
                    if char.isalnum():
                        codigo_limpo += char
                if codigo_limpo:
                    codigos.append(codigo_limpo)
                i = j
            else:
                break
        i += 1
    return codigos

mensagem = "Sensor detectado: @A1B2C3# fora de faixa. Erro: @ 9X # ignorado. Validação: @99Z#"
codigos = extrair_codigos(mensagem)
print(codigos)