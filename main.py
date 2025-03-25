import os
import json
import database
import sys
import time

def limpar_console():
  os.system('cls' if os.name == 'nt' else 'clear') #Limpa o console
  
def OpcoesMenu(ValorOpcao):
  if ValorOpcao == 0: #Se a opção for 0, fecha o console
    print ("Saindo do sistema...")
    time.sleep(1)
    sys.exit()
  
  elif ValorOpcao == 1:  #Se a opção for 1, pega as entradas para definir os dados do filme
    id_filme = input("Defina um ID para o filme: ")
    Nome = input("Digite o nome do filme: ") 
    Ano = input("Digite o ano do filme: ")
    Genero = input("Digite o gênero do filme: ")
    Disponibilidade = input("Digite a disponibilidade do filme: ")
    database.filmes_cadastrados[id_filme] = {
      "Nome": Nome,
      "Ano": Ano,
      "Genero": Genero,
      "Disponibilidade": Disponibilidade
    }
    print ("Filme cadastrado com sucesso!")
    continuar = input("Aperte qualquer tecla para sair")
    print ("Carregando...")
    time.sleep(1)
    limpar_console()
    MenuPrincipal()
    
  elif ValorOpcao == 2: #Se a opção for 2, mostra os filmes cadastrados
    try:
     for filme in database.filmes_cadastrados:
      print ("ID do filme:", filme)
      print ("Nome do filme:", database.filmes_cadastrados[filme]["Nome"])
      print ("Ano do filme:", database.filmes_cadastrados[filme]["Ano"])
      print ("Gênero do filme:", database.filmes_cadastrados[filme]["Genero"])
      print ("Disponibilidade do filme:", database.filmes_cadastrados[filme]["Disponibilidade"])
      print ("-----------------------------")
    except:
      print ("Não há filmes cadastrados.")
    continuar = input("Aperte qualquer tecla para sair")
    print ("Carregando...")
    time.sleep(1)
    limpar_console()
    MenuPrincipal()

def MenuPrincipal(): #Abre o menu de opções
  print ("-----------------------------")
  print ("Seja bem-vindo ao Sistema de Locadora de Vídeo.")
  print ("0 - Sair")
  print ("1 - Cadastrar Filme")
  print ("2 - Carregar Filme")
  opcao = input("Digite a opção desejada: ")
  OpcoesMenu(int(opcao))
  
if __name__ == "__main__": #Verifica se é o script principal; se for, roda a função MenuPrincipal()
    MenuPrincipal()