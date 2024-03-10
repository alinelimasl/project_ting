import sys
from pathlib import Path


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    path = Path(path_file)
    if not path.suffix.lower() == ".txt":
        sys.stderr.write("Formato inválido\n")
        return []

    try:
        with open(path, "r") as file:
            news = file.read().splitlines()
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path} não encontrado\n")
        return []

    return news
