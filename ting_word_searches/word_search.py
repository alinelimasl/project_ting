def exists_word(word, instance):
    result = []
    fila = instance._fila
    for file_data in fila:
        file_name = file_data["nome_do_arquivo"]
        occurrences = []
        with open(file_name, "r") as file:
            for line_num, line in enumerate(file, start=1):
                if word.lower() in line.lower():
                    occurrences.append({"linha": line_num})
        if occurrences:
            result.append(
                {
                    "palavra": word,
                    "arquivo": file_name,
                    "ocorrencias": occurrences,
                }
            )
    return result


def search_by_word(word, instance):
    result = []
    fila = instance._fila
    for file_data in fila:
        file_name = file_data["nome_do_arquivo"]
        occurrences = []
        with open(file_name, "r") as file:
            for line_num, line in enumerate(file, start=1):
                if word.lower() in line.lower():
                    occurrences.append(
                        {"linha": line_num, "conteudo": line.strip()}
                    )
        if occurrences:
            result.append(
                {
                    "palavra": word,
                    "arquivo": file_name,
                    "ocorrencias": occurrences,
                }
            )
    return result
