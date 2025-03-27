import os
import json
import database
import sys
import time

def limpar_console():
  os.system('cls' if os.name == 'nt' else 'clear') #Limpa o console

def SalvarFilmes():
  database.salvar_arquivoFilmes()
  entrada = input("Pressione qualquer tecla para continuar")
  print ("Carregando...")
  time.sleep(1)
  limpar_console()
  MenuPrincipal()
  
def CarregarFilmes():
  database.carregar_arquivoFilmes()
  entrada = input("Pressione qualquer tecla para continuar")
  print ("Carregando...")
  time.sleep(1)
  limpar_console()
  MenuPrincipal()

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
    if database.filmes_cadastrados: #Se houver filmes cadastrados, mostra os filmes
     for filme in database.filmes_cadastrados:
      print ("ID do filme:", filme)
      print ("Nome do filme:", database.filmes_cadastrados[filme]["Nome"])
      print ("Ano do filme:", database.filmes_cadastrados[filme]["Ano"])
      print ("Gênero do filme:", database.filmes_cadastrados[filme]["Genero"])
      print ("Disponibilidade do filme:", database.filmes_cadastrados[filme]["Disponibilidade"])
      print ("-----------------------------")
    else: #Se não houver filmes cadastrados, mostra uma mensagem de erro
      print ("Não há filmes cadastrados.")
    continuar = input("Aperte qualquer tecla para sair")
    print ("Carregando...")
    time.sleep(1)
    limpar_console()
    MenuPrincipal()

  elif ValorOpcao == 4: #Se 4, salva os filmes cadastrados em um arquivo JSON
    SalvarFilmes()
  
  elif ValorOpcao == 5: #Se 5, carrega os filmes cadastrados de um arquivo JSON
    CarregarFilmes()
    
def MenuPrincipal(): #Abre o menu de opções
  print ("-----------------------------")
  print ("Seja bem-vindo ao Sistema de Locadora de Vídeo.")
  print ("0 - Sair")
  print ("1 - Cadastrar Filme")
  print ("2 - Carregar Filme")
  print ("3 - Remover Filme (Não implementado)")
  print ("4 - Salvar Lista de Filmes em JSON")
  print ("5 - Carregar Lista de Filmes de JSON")
  print ("-----------------------------")

  try: #Tenta pegar a opção do usuário
    opcao = int(input("Digite a opção desejada: "))
    if opcao not in [0, 1, 2, 4, 5]: #Se a opção não for 0, 1 ou 2, mostra uma mensagem de erro
        print("Opção inválida!")
        time.sleep(1)
        limpar_console()
        MenuPrincipal()
    else: #Se a opção for 0, 1 ou 2, chama a função OpcoesMenu()
        OpcoesMenu(opcao)
  except ValueError: #Se o usuário digitar algo que não seja um número, mostra uma mensagem de erro
    print("Por favor, digite um número!")
    time.sleep(1)
    limpar_console()
    MenuPrincipal()
  
if __name__ == "__main__": #Verifica se é o script principal; se for, roda a função MenuPrincipal()
    MenuPrincipal()