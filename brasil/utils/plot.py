import matplotlib.pyplot as plt
from pathlib import Path


def generate_dimension_plot(nome: str, dimensao: float):
    plt.figure(figsize=(6, 4))
    plt.bar(nome, dimensao, color="skyblue")
    plt.ylabel("Dimensão (km²)")
    plt.title(f"Dimensão de {nome}")
    plt.tight_layout()

    output_dir = Path("graphs")
    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / f"{nome.replace(' ', '_')}_dimension.png"
    plt.savefig(output_path)
    plt.close()
    return str(output_path)


def generate_difference_plot(nome1: str, dimensao1: float, nome2: str, dimensao2: float):
    plt.figure(figsize=(8, 4))
    plt.bar([nome1, nome2], [dimensao1, dimensao2], color=["skyblue", "lightgreen"])
    plt.ylabel("Dimensão (km²)")
    plt.title(f"Comparação: {nome1} vs {nome2}")
    plt.tight_layout()

    output_dir = Path("graphs")
    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / f"{nome1.replace(' ', '_')}_vs_{nome2.replace(' ', '_')}.png"
    plt.savefig(output_path)
    plt.close()
    return str(output_path)