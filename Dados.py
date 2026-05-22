import json
class Dados:
    def create(nome_arquivo):
        try:
            with open(nome_arquivo, "x", encoding="utf-8") as f:
                json.dump([], f, indent=4, ensure_ascii=False)
        except FileExistsError:
            print(" ")



    def save(nome_arquivo, dados):
        with open(nome_arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)
        print(f"Arquivo '{nome_arquivo}' salvo com sucesso!")


    def load(nome_arquivo):
        try:
            with open(nome_arquivo, "r", encoding="utf-8") as f:
                dados = json.load(f)
            return dados
        except FileNotFoundError:
            print(f"Arquivo '{nome_arquivo}' não encontrado.")
            return None