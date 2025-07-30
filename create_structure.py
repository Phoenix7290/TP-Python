import os

# Define a estrutura do projeto - rápidez na formatação das pastas
base_dir = "TP"
tps = ["tp1", "tp2", "tp3"]
exercises = [f"ex{i:02d}" for i in range(1, 13)]
common_dir = "common"

os.makedirs(base_dir, exist_ok=True)

for tp in tps:
    tp_path = os.path.join(base_dir, tp)
    os.makedirs(tp_path, exist_ok=True)
    for ex in exercises:
        ex_path = os.path.join(tp_path, ex)
        os.makedirs(ex_path, exist_ok=True)

os.makedirs(os.path.join(base_dir, common_dir), exist_ok=True)

print("Estrutura de pastas criada com sucesso!")
