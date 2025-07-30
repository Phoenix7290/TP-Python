import importlib
import sys
import os
import time

# Adiciona o diretório raiz (TP/) ao sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.append(project_root)

def run_exercise(tp, ex_number):
    try:
        # Importa o módulo main do exercício
        module = importlib.import_module(f"tp{tp}.ex{ex_number:02d}.main")
        print(f"\nExecutando TP{tp} - Exercício {ex_number:02d}")
        start_time = time.perf_counter()
        module.main()  # Executa a função main()
        end_time = time.perf_counter()
        print(f"Tempo de execução: {end_time - start_time:.6f} segundos")
    except (ImportError, AttributeError, Exception) as e:
        print(f"Erro ao executar TP{tp} - Exercício {ex_number:02d}: {e}")

if __name__ == "__main__":
    for ex in range(1, 13):  # Para 12 exercícios
        run_exercise(1, ex)