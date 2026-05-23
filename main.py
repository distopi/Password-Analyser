import sys
from pathlib import Path


def carregar_senhas_vazadas(diretorio: str) -> set[str]:

    senhas_compiladas = set()
    caminho_dir = Path(diretorio)

    if not caminho_dir.exists() or not caminho_dir.is_dir():
        print(f"O diretório '{diretorio}' não foi encontrado. A análise de vazamentos será ignorada.")
        return senhas_compiladas

    print(f"Carregando banco de dados de vazamentos em '{diretorio}'...")

    for arquivo in caminho_dir.glob("*.txt"):
        try:
            with open(arquivo, "r", encoding="utf-8", errors="ignore") as f:
                for linha in f:
                    senha = linha.strip()
                    if senha:
                        senhas_compiladas.add(senha.lower())
        except Exception as e:
            print(f"Erro ao ler o arquivo {arquivo.name}: {e}")

    print(f"Total de senhas vazadas carregadas: {len(senhas_compiladas)}\n")
    return senhas_compiladas


def analisar_senha(senha_usuario: str, senhas_vazadas: set[str]) -> dict:

    defeitos = []
    tamanho = len(senha_usuario)
    senha_minuscula = senha_usuario.lower()

    if tamanho < 8:
        classificacao_tamanho = "Fraca"
        defeitos.append(f"Muito curta: Tem apenas {tamanho} caracteres (Mínimo aceitável: 8, Forte: 10, Ideal: 12+).")
    elif tamanho < 10:
        classificacao_tamanho = "Média"
        defeitos.append(f"Tamanho mediano: Tem {tamanho} caracteres. Considere expandir para 10 ou mais.")
    elif tamanho < 12:
        classificacao_tamanho = "Forte"
    else:
        classificacao_tamanho = "Ideal"

    if senha_usuario.isalpha():
        defeitos.append("Baixa complexidade: A senha contém exclusivamente letras.")
    elif senha_usuario.isdigit():
        defeitos.append("Baixa complexidade: A senha contém exclusivamente números.")

    tem_maiuscula = any(c.isupper() for c in senha_usuario)
    tem_minuscula = any(c.islower() for c in senha_usuario)

    if any(c.isalpha() for c in senha_usuario) and not (tem_maiuscula and tem_minuscula):
        defeitos.append("Falta de variedade: A senha não mistura letras maiúsculas e minúsculas.")

    tem_especial = any(not c.isalnum() for c in senha_usuario)
    if not tem_especial:
        defeitos.append("Falta de símbolos: A senha não possui caracteres especiais (ex: @, #, $, %, etc.).")

    if senha_minuscula in senhas_vazadas:
        defeitos.append("Esta senha exata consta na lista de senhas mais comuns/vazadas do mundo.")
    else:
        for senha_vazada in senhas_vazadas:
            if len(senha_vazada) >= 4 and senha_vazada in senha_minuscula:
                defeitos.append(
                    f"A sua senha contém um padrão amplamente comum/vazado dentro dela ('{senha_vazada}').")
                break

    return {
        "classificacao_tamanho": classificacao_tamanho,
        "defeitos": defeitos
    }


def main():
    banco_vazadas = carregar_senhas_vazadas("Passwords")

    print("=========================================")
    print("       ANALISADOR DE SENHAS")
    print("=========================================\n")

    senha = input("Digite a senha que deseja analisar: ").strip()

    if not senha:
        print("Nenhuma senha foi digitada.")
        return

    resultado = analisar_senha(senha, banco_vazadas)

    print("\n-----------------------------------------")
    print(f"📊 Classificação de tamanho: {resultado['classificacao_tamanho']}")
    print("-----------------------------------------")

    if not resultado["defeitos"]:
        print("Nenhum defeito ou ponto fraco foi encontrado na sua senha.")
    else:
        print("Pontos fracos e defeitos encontrados:")
        for defeito in resultado["defeitos"]:
            print(f" {defeito}")
    print("-----------------------------------------")


if __name__ == "__main__":
    main()