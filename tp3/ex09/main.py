def criptografar_cme(lista_pedidos, status="Pendente"):
    for codigo in lista_pedidos:
        mensagem = f"Pedido {codigo}: Status - {status}"
        criptografada = ""
        for i, char in enumerate(mensagem):
            if char == " ":
                criptografada += char
            elif i % 2 == 0:
                criptografada += chr(ord(char) + 2)
            else:
                criptografada += chr(ord(char) - 1)
        print(criptografada)

pedidos = ["A123", "B456", "C789"]
criptografar_cme(pedidos)
criptografar_cme(pedidos, status="Enviado")