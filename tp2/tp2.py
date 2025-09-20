# %% [markdown]
# # Exercício 1: Classificar transações bancárias
# Implementa a classificação de transações com base no valor e tipo, usando condicionais.

ANO_2_DIGITOS = 25 
VALOR_TRANSACAO = 100000
TIPO_TRANSACAO = "transferência"

limite_valor = 1000 * ANO_2_DIGITOS

if VALOR_TRANSACAO > limite_valor and TIPO_TRANSACAO == "transferência":
    print("Alerta: verificar origem da transferência")
elif TIPO_TRANSACAO == "saque":
    print("Alerta: confirmar com o cliente")
else:
    print("Transação normal")

# %% [markdown]
# # Exercício 2: Verificar elegibilidade para promoção
# Verifica se um funcionário é elegível para promoção com base em tempo de empresa e nota.

tempo_empresa_anos = 3
nota_avaliacao = 8.5
carga_horaria = 40

if tempo_empresa_anos > 2 and nota_avaliacao >= 8.0:
    print("Elegível para promoção")
else:
    print("Aguardando próxima avaliação")

# %% [markdown]
# # Exercício 3: Avaliar risco de atraso
# Classifica o risco de atraso de entregas com base em distância, clima e zona.

distancia_km = 350
clima = "chuva"
zona_entrega = "rural"

if distancia_km > 300 and (clima == "chuva" or zona_entrega == "rural"):
    print("Risco alto de atraso")
else:
    print("Entrega dentro do previsto")

# %% [markdown]
# # Exercício 4: Tratar falhas de sensores
# Decide ações com base no código de falha do sensor e temperatura.

codigo_falha = "F1"
temperatura = 35

if codigo_falha == "F1" and temperatura < 40:
    print("Reiniciar máquina")
elif codigo_falha == "F2" and temperatura > 60:
    print("Verificar conexão elétrica e sistema de refrigeração")
elif codigo_falha == "F3" and 45 <= temperatura <= 55:
    print("Ajustar temperatura da esteira")
elif codigo_falha == "F4":
    print("Realizar diagnóstico dos sensores ópticos")
else:
    print("Falha não reconhecida pelo sistema de alarme. Acionar engenheiro responsável")

# %% [markdown]
# # Exercício 5: Filtrar clientes satisfeitos
# Percorre uma lista de notas e imprime apenas as maiores que 7.

notas_avaliacao = [5, 8, 10, 6, 9, 4]

for nota in notas_avaliacao:
    if nota > 7:
        print(nota)

# %% [markdown]
# # Exercício 6: Gerar lista de comissões
# Gera uma lista de valores de 0 a 50, de 5 em 5.

comissoes = list(range(0, 51, 5))
print(comissoes)

# %% [markdown]
# # Exercício 7: Controlar tentativas de conexão
# Monitora tentativas de conexão e interrompe após um limite.

tentativas_conexao = [False, False, False, True, True]
tentativas = 0
limite_tentativas = 3

while tentativas < len(tentativas_conexao):
    print("Tentando conectar...")
    tentativas += 1
    if tentativas >= limite_tentativas and not tentativas_conexao[tentativas - 1]:
        print("Conexão interrompida após limite de tentativas")
        break

# %% [markdown]
# # Exercício 8: Reorganizar fila de pedidos
# Reorganiza uma fila de pedidos com base em prioridade e substituição.

# Cenário A
pedidos = ["P123", "P456", "P789"]
pedido_a_substituir = "P456"
prioridade_urgente = True
pedido_urgente = "P999"

if prioridade_urgente:
    pedidos.insert(0, pedido_urgente)
else:
    if pedido_a_substituir in pedidos:
        indice = pedidos.index(pedido_a_substituir)
        pedidos[indice] = pedido_urgente
print(f"Fila final (Cenário A): {pedidos}")

# Cenário B
pedidos = ["P123", "P456", "P789"]
pedido_a_substituir = "P456"
prioridade_urgente = False
pedido_urgente = "P999"

if prioridade_urgente:
    pedidos.insert(0, pedido_urgente)
else:
    if pedido_a_substituir in pedidos:
        indice = pedidos.index(pedido_a_substituir)
        pedidos[indice] = pedido_urgente
print(f"Fila final (Cenário B): {pedidos}")

# Cenário C
pedidos = ["P123", "P456", "P789"]
pedido_a_substituir = "P000"
prioridade_urgente = False
pedido_urgente = "P999"

if prioridade_urgente:
    pedidos.insert(0, pedido_urgente)
else:
    if pedido_a_substituir in pedidos:
        indice = pedidos.index(pedido_a_substituir)
        pedidos[indice] = pedido_urgente
    else:
        print(f"Pedido {pedido_a_substituir} não encontrado na lista.")
print(f"Fila final (Cenário C): {pedidos}")

# %% [markdown]
# # Exercício 9: Unificar estoque de armazéns
# Concatena listas de produtos e conta a quantidade de cada item.

produtos_a = ["banana", "maçã"]
produtos_b = ["laranja", "pera"]
produtos_c = ["laranja", "banana", "maçã", "romã"]

estoque_total = produtos_a + produtos_b + produtos_c
print(f"Estoque total: {estoque_total}")

contagem = {}
for produto in estoque_total:
    contagem[produto] = contagem.get(produto, 0) + 1
print("Contagem de produtos:")
for produto, quantidade in contagem.items():
    print(f"{produto}: {quantidade}")

# %% [markdown]
# # Exercício 10: Identificar boletos vencidos
# Verifica o status de boletos com base em datas de vencimento.

data_atual = "2025-08-12"
boletos = ["2025-08-05", "2025-08-12", "2025-08-15", "2025-08-01"]
total_vencidos = 0

for i, vencimento in enumerate(boletos, 1):
    if vencimento < data_atual:
        print(f"Boleto: {i} | Vencimento: {vencimento} | Situação: vencido")
        total_vencidos += 1
    elif vencimento == data_atual:
        print(f"Boleto: {i} | Vencimento: {vencimento} | Situação: vence hoje")
    else:
        print(f"Boleto: {i} | Vencimento: {vencimento} | Situação: dentro do prazo")

print(f"Total de boletos vencidos: {total_vencidos}")

# %% [markdown]
# # Exercício 11: Decodificar mensagem cifrada
# Desencripta uma mensagem usando a cifra de César com chave baseada na contagem de 'D', 'd', e 'W'.

mensagem = "SbwKrQ eh phokRu q MDydvfulsW"
chave = mensagem.count('D') + mensagem.count('d') + mensagem.count('W')


# A questao era bem mais complexa do que imaginei inicialmente de modo que pesquisei como realizar a decodificação.

def decodificar_cesar(texto, chave):
    resultado = ""
    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            nova_pos = (ord(char) - base - chave) % 26 + base
            resultado += chr(nova_pos)
        else:
            resultado += char
    return resultado

palavras = []
i = 0
while i < len(mensagem):
    palavra = ""
    while i < len(mensagem) and mensagem[i] != ' ':
        palavra += mensagem[i]
        i += 1
    if len(palavra) > 3:
        palavra = decodificar_cesar(palavra, chave)
    palavras.append(palavra)
    if i < len(mensagem) and mensagem[i] == ' ':
        palavras.append(' ')
        i += 1

mensagem_decodificada = "".join(palavras)
print(mensagem_decodificada)

# %% [markdown]
# # Exercício 12: Otimizar verificação de sensores
# Verifica temperaturas de sensores usando um laço para otimizar o código.

temperaturas = [28, 31, 27, 35, 29]

for i, temp in enumerate(temperaturas, 1):
    if temp > 30:
        print(f"Sensor {i} acima do limite")
# %%
