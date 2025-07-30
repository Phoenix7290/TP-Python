def main():
    desconto_txt = '60'
    desconto_num = int(desconto_txt) / 3.14
    valor_fixo = 599.99
    valor_final = valor_fixo - desconto_num
    
    print(f"Valor final: {valor_final}")

if __name__ == "__main__":
    main()