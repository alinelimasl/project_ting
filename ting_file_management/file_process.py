from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    new_file = dict(
        {
            "nome_do_arquivo": path_file,
            "qtd_linhas": txt_importer(path_file).__len__(),
            "linhas_do_arquivo": txt_importer(path_file),
        }
    )

    if new_file not in instance._fila:
        instance.enqueue(new_file)
        sys.stdout.write(str(new_file))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
