def main():
    ano_2_digitos = 15
    tempo_minutos = 150 + ano_2_digitos
    tempo_horas = 2.25
    
    horas = tempo_minutos / 60
    minutos = tempo_horas * 60
    
    print(f"{horas} horas & {minutos} minutos")

if __name__ == "__main__":
    main()