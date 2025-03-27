import os
import json

filmes_cadastrados = {}  
"""
"F001": {
    "Nome": "",
    "Ano": "",
    "Genero": "",
    "Disponibilidade": 0
      }
}                        
""" 

def salvar_arquivoFilmes(): #Salva o dicionário de filmes cadastrados em um arquivo JSON
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

def carregar_arquivoFilmes(): #Carrega o dicionário de filmes cadastrados salvo no JSON
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