# 🔐 Password Analyser

Um analisador de segurança de senhas via linha de comando (CLI) desenvolvido em Python. 

Esta ferramenta avalia a força de uma senha fornecida pelo usuário com base em múltiplos critérios de complexidade e, de forma contínua, cruza essa senha com bancos de dados locais de vazamentos (wordlists) para garantir que ela não é um padrão já comprometido. Tudo isso rodando **100% localmente**, garantindo privacidade total sem a necessidade de enviar dados sensíveis para APIs externas na web.

---

## 🚀 Funcionalidades

O script realiza uma varredura completa na senha e retorna um relatório de "defeitos", avaliando:

- **Métrica de Tamanho:** Classifica a senha como Fraca (< 8), Média (8-9), Forte (10-11) ou Ideal (12+).
- **Diversidade de Caracteres:** Verifica a presença obrigatória de letras, números e caracteres especiais.
- **Variação de Caixa:** Exige a mistura de letras maiúsculas e minúsculas para evitar padrões simples.
- **Verificação de Vazamentos (Wordlists):** - Compara a senha digitada contra milhares/milhões de senhas vazadas compiladas em arquivos `.txt`.
  - Checa tanto a correspondência exata quanto a inclusão (se a senha digitada contém um padrão vazado em seu interior).

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3
- **Bibliotecas Nativas:** `sys`, `pathlib` (para manipulação segura e cross-platform de diretórios).
- **Estruturas de Dados:** Uso intensivo de `set()` para carregamento e busca otimizada do banco de senhas vazadas em memória.

