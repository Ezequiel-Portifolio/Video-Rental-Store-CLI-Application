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
import languages as lang

filmes_cadastrados = {}  
"""
Dicionário que armazena os filmes cadastrados na sessão atual.
Estrutura:
{
    "F001": {
        "Nome": "Nome do Filme",
        "Ano": 2023,
        "Genero": "Ação",
        "Disponibilidade": True
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
        # Validate data before saving
        if not isinstance(filmes_cadastrados, dict):
            print(lang.get_string("save_error").format("Dados inválidos"))
            return False
        
        # Create backup of existing file if it exists
        if os.path.exists("dados_filmes.json"):
            try:
                os.rename("dados_filmes.json", "dados_filmes.json.backup")
            except OSError:
                pass  # Continue even if backup fails
        
        # Save to file with error handling
        with open("dados_filmes.json", "w", encoding="utf-8") as arquivo: 
            json.dump(filmes_cadastrados, arquivo, indent=4, ensure_ascii=False)
        
        # Remove backup file if save was successful
        if os.path.exists("dados_filmes.json.backup"):
            try:
                os.remove("dados_filmes.json.backup")
            except OSError:
                pass  # Continue even if backup removal fails
        
        print(lang.get_string("file_saved"))
        return True
        
    except PermissionError:
        print(lang.get_string("save_error").format("Sem permissão para escrever no arquivo"))
        return False
    except OSError as erro:
        print(lang.get_string("save_error").format(f"Erro no sistema de arquivos: {erro}"))
        return False
    except Exception as erro:
        print(lang.get_string("save_error").format(str(erro)))
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
        # Check if file exists and is readable
        if not os.path.exists("dados_filmes.json"):
            print(lang.get_string("file_not_found"))
            return False
        
        if not os.access("dados_filmes.json", os.R_OK):
            print(lang.get_string("load_error").format("Sem permissão para ler o arquivo"))
            return False
        
        # Try to load and validate the JSON data
        with open("dados_filmes.json", "r", encoding="utf-8") as arquivo:
            data = json.load(arquivo)
        
        # Validate loaded data structure
        if not isinstance(data, dict):
            print(lang.get_string("load_error").format("Formato de arquivo inválido"))
            return False
        
        # Validate each movie entry
        validated_data = {}
        for movie_id, movie_data in data.items():
            if isinstance(movie_data, dict) and all(key in movie_data for key in ["Nome", "Ano", "Genero", "Disponibilidade"]):
                # Convert old string format to new format if needed
                movie_copy = movie_data.copy()
                
                # Convert year to integer if it's a string
                if isinstance(movie_copy["Ano"], str):
                    try:
                        movie_copy["Ano"] = int(movie_copy["Ano"])
                    except ValueError:
                        movie_copy["Ano"] = 2000  # Default year
                
                # Convert availability to boolean if it's a string
                if isinstance(movie_copy["Disponibilidade"], str):
                    movie_copy["Disponibilidade"] = movie_copy["Disponibilidade"].lower() in ["sim", "yes", "true", "disponível", "disponivel"]
                
                validated_data[movie_id] = movie_copy
        
        filmes_cadastrados = validated_data
        print(lang.get_string("movies_loaded").format(len(filmes_cadastrados)))
        return True
    
    except FileNotFoundError:
        print(lang.get_string("file_not_found"))
        return False
    
    except PermissionError:
        print(lang.get_string("load_error").format("Sem permissão para acessar o arquivo"))
        return False
    
    except json.JSONDecodeError as erro:
        print(lang.get_string("load_error").format(f"Arquivo JSON inválido: {erro}"))
        return False
    
    except Exception as erro:
        print(lang.get_string("load_error").format(str(erro)))
        return False