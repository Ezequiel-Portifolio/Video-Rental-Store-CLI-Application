import os
import json
import database
import time

def limpar_console():
  os.system('cls' if os.name == 'nt' else 'clear')
  
def OpcoesMenu(ValorOpcao):
  if ValorOpcao == 0:
    Nome = input("Digite o nome do filme:")
    Ano = input("Digite o ano do filme:")
    Genero = input("Digite o gênero do filme:")
    Disponibilidade = input("Digite a disponibilidade do filme:")
    database.filmes_cadastrados["Filme"]["Nome"] = Nome
    database.filmes_cadastrados["Filme"]["Ano"] = Ano
    database.filmes_cadastrados["Filme"]["Genero"] = Genero
    database.filmes_cadastrados["Filme"]["Disponibilidade"] = Disponibilidade
    print ("Filme cadastrado com sucesso!")
    continuar = input("Aperte qualquer tecla para sair")
    print ("Carregando...")
    time.sleep(2)
    limpar_console()
    MenuPrincipal()
    
  elif ValorOpcao == 1:
    if database.filmes_cadastrados["Filme"]["Nome"] == "":
      print ("Nenhum filme cadastrado.")
      time.sleep(2)
      MenuPrincipal()
    else:
      print ("Nome do filme:", database.filmes_cadastrados["Filme"]["Nome"])
      print ("Ano do filme:", database.filmes_cadastrados["Filme"]["Ano"])
      print ("Gênero do filme:", database.filmes_cadastrados["Filme"]["Genero"])
      print ("Disponibilidade do filme:", database.filmes_cadastrados["Filme"]["Disponibilidade"])
      continuar = input("Aperte qualquer tecla para sair")
      print ("Carregando...")
      time.sleep(2)
      limpar_console()
      MenuPrincipal()

def MenuPrincipal():
  print ("-----------------------------")
  print ("Seja bem-vindo ao Sistema de Locadora de Vídeo.")
  print ("0 - Cadastrar Filme")
  print ("1 - Carregar Filme")
  opcao = input("Digite a opção desejada:")
  OpcoesMenu(int(opcao))
if __name__ == "__main__":
    MenuPrincipal()