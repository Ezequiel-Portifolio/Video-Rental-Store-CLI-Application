"""
Database Module - Video Rental Store CLI Application
---------------------------------------------------

Este módulo gerencia a persistência de dados da aplicação de Locadora de Vídeos.
Implementa as funções para salvar e carregar os dados dos filmes em formato JSON.

Funcionalidades:
- Armazenamento temporário de filmes em dicionário
- Salvamento da lista de filmes em arquivo JSON
- Carregamento de filmes a partir de arquivo JSON

Estrutura de dados:
O dicionário filmes_cadastrados utiliza o ID do filme como chave
e um sub-dicionário com os detalhes do filme como valor.
"""

import os
import json

filmes_cadastrados = {}  
"""
Dicionário que armazena os filmes cadastrados na sessão atual.
Estrutura:
{
    "F001": {
        "Nome": "Nome do Filme",
        "Ano": "2023",
        "Genero": "Ação",
        "Disponibilidade": "Sim"
    },
    ...
}                        
""" 

def salvar_arquivoFilmes():
    """
    Salva o dicionário de filmes cadastrados em um arquivo JSON.
    
    Retorna:
    --------
    bool
        True se o salvamento for bem-sucedido, False caso contrário.
    
    Exemplo:
    --------
    >>> salvar_arquivoFilmes()
    Arquivo de filmes salvo com sucesso em dados_filmes.json
    True
    """
    try:
        #abre ou cria o arquivo, se não existir
        with open("dados_filmes.json", "w", encoding="utf-8") as arquivo: 
            #Salva o dicionário no arquivo JSON
            json.dump(filmes_cadastrados, arquivo, indent=4, ensure_ascii=False)
        print ("Arquivo de filmes salvo com sucesso em dados_filmes.json")
        return True
    except Exception as erro:
        print (f"Erro ao salvar o arquivo de filmes: {erro}")
        return False

def carregar_arquivoFilmes():
    """
    Carrega o dicionário de filmes cadastrados a partir de um arquivo JSON.
    Atualiza a variável global filmes_cadastrados com os dados carregados.
    
    Retorna:
    --------
    bool
        True se o carregamento for bem-sucedido, False caso contrário.
    
    Exemplo:
    --------
    >>> carregar_arquivoFilmes()
    5 filmes carregados com sucesso.
    True
    """
    global filmes_cadastrados
    
    try:
        #Tentar abrir o arquivo para leitura
        with open("dados_filmes.json", "r", encoding="utf-8") as arquivo:
            #Carrega o dicionário do arquivo JSON
            filmes_cadastrados = json.load(arquivo)
        print(f"{len(filmes_cadastrados)} filmes carregados com sucesso.")
        return True
    
    except FileNotFoundError:
        # Se o arquivo não existir, não carrega nada
        print("Arquivo de filmes não encontrado. Verifique se o arquivo está no mesmo diretório.")
        return False
    
    except Exception as erro:
        print(f"Erro ao carregar o arquivo de filmes: {erro}")
        return False