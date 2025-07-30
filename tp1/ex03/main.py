def main():
    ano_2_digitos = 25
    km_por_dia = 80
    gasto_diario = 300 + ano_2_digitos
    
    total_semana = km_por_dia * 7 
    diferenca_gasto = gasto_diario - 100
    dias_cobertos = 500 / gasto_diario
    porcentagem_diaria = gasto_diario % 100
    media_diaria = gasto_diario / km_por_dia
    
    print(total_semana)
    print(diferenca_gasto)
    print(dias_cobertos)
    print(porcentagem_diaria)
    print(media_diaria)

if __name__ == "__main__":
    main()