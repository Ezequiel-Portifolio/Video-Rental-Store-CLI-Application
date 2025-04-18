"""
Main Module - Video Rental Store CLI Application
------------------------------------------------

Este módulo contém a interface principal da aplicação de Locadora de Vídeos.
Ele gerencia o menu principal e coordena as interações com os outros módulos.

Funcionalidades:
- Menu interativo para gerenciamento de filmes
- Registro, listagem e remoção de filmes
- Operações de persistência de dados (salvar/carregar)
- Troca de idioma entre Português e Inglês

Módulos Dependentes:
- database: Gerencia o armazenamento e persistência dos filmes
- languages: Fornece suporte a múltiplos idiomas
"""

import json
import database
import sys
import time
import languages as lang

def limpar_console():
    """
    Limpa a tela do console para melhor visualização do menu.
    Usa sequências de escape ANSI que são compatíveis com a maioria dos terminais.
    """
    print("\033[H\033[J", end="") #Limpa o console


def MudarIdioma():
    """
    Exibe menu para seleção de idioma e atualiza o idioma do sistema.
    Após a troca, retorna ao menu principal com o novo idioma aplicado.
    """
    print(lang.get_string("select_language"))
    try:
        opcao = int(input())
        if opcao in [1, 2]:
            message = lang.set_language(opcao)
            print(message)
        else:
            print(lang.get_string("invalid_option"))
    except ValueError:
        print(lang.get_string("enter_number"))
    
    time.sleep(1)
    limpar_console()
    MenuPrincipal()

def PrimeiroMenu():
    """
    Função inicial que é chamada quando o programa começa.
    Primeiro solicita a seleção do idioma antes de mostrar o menu principal.
    """
    MudarIdioma()
    MenuPrincipal()

def SalvarFilmes():
    """
    Salva a lista atual de filmes em um arquivo JSON.
    Utiliza a função do módulo database para persistir os dados.
    """
    database.salvar_arquivoFilmes()
    entrada = input(lang.get_string("press_continue"))
    print(lang.get_string("loading"))
    time.sleep(1)
    limpar_console()
    MenuPrincipal()

def RemoverFilmes():
    """
    Remove um filme do catálogo com base no ID fornecido pelo usuário.
    Exibe mensagem de confirmação ou erro se o filme não for encontrado.
    """
    id_filme = input(lang.get_string("enter_remove_id"))
    if id_filme in database.filmes_cadastrados:
        del database.filmes_cadastrados[id_filme]
        print(lang.get_string("movie_removed"))
    else:
        print(lang.get_string("movie_not_found"))
    continuar = input(lang.get_string("press_exit"))
    print(lang.get_string("loading"))
    time.sleep(1)
    limpar_console()
    MenuPrincipal()

def CarregarFilmes():
    """
    Carrega a lista de filmes de um arquivo JSON.
    Utiliza a função do módulo database para ler os dados salvos anteriormente.
    """
    database.carregar_arquivoFilmes()
    entrada = input(lang.get_string("press_continue"))
    print(lang.get_string("loading"))
    time.sleep(1)
    limpar_console()
    MenuPrincipal()

def OpcoesMenu(ValorOpcao):
    """
    Processa a opção selecionada pelo usuário no menu principal.
    
    Parâmetros:
    -----------
    ValorOpcao : int
        O número da opção selecionada pelo usuário
        
    Opções:
    -------
    0: Sair do programa
    1: Cadastrar novo filme
    2: Listar filmes cadastrados
    3: Remover filme existente
    4: Salvar lista de filmes em JSON
    5: Carregar lista de filmes de JSON
    6: Alterar idioma do sistema
    """
    if ValorOpcao == 0: #Se a opção for 0, fecha o console
        print(lang.get_string("exiting"))
        time.sleep(1)
        sys.exit()
  
    elif ValorOpcao == 1:  #Se a opção for 1, pega as entradas para definir os dados do filme
        id_filme = input(lang.get_string("define_id"))
        Nome = input(lang.get_string("enter_name"))
        Ano = input(lang.get_string("enter_year"))
        Genero = input(lang.get_string("enter_genre"))
        Disponibilidade = input(lang.get_string("enter_availability"))
        database.filmes_cadastrados[id_filme] = {
            "Nome": Nome,
            "Ano": Ano,
            "Genero": Genero,
            "Disponibilidade": Disponibilidade
        }
        print(lang.get_string("movie_registered"))
        continuar = input(lang.get_string("press_exit"))
        print(lang.get_string("loading"))
        time.sleep(1)
        limpar_console()
        MenuPrincipal()
    
    elif ValorOpcao == 2: #Se a opção for 2, mostra os filmes cadastrados
        if database.filmes_cadastrados: #Se houver filmes cadastrados, mostra os filmes
            for filme in database.filmes_cadastrados:
                print(lang.get_string("movie_id"), filme)
                print(lang.get_string("movie_name"), database.filmes_cadastrados[filme]["Nome"])
                print(lang.get_string("movie_year"), database.filmes_cadastrados[filme]["Ano"])
                print(lang.get_string("movie_genre"), database.filmes_cadastrados[filme]["Genero"])
                print(lang.get_string("movie_availability"), database.filmes_cadastrados[filme]["Disponibilidade"])
                print("-----------------------------")
        else: #Se não houver filmes cadastrados, mostra uma mensagem de erro
            print(lang.get_string("no_movies"))
        continuar = input(lang.get_string("press_exit"))
        print(lang.get_string("loading"))
        time.sleep(1)
        limpar_console()
        MenuPrincipal()

    elif ValorOpcao == 3: #Se a opção for 3, chama a função RemoverFilmes()
        RemoverFilmes()
    
    elif ValorOpcao == 4: #Se 4, salva os filmes cadastrados em um arquivo JSON
        SalvarFilmes()
  
    elif ValorOpcao == 5: #Se 5, carrega os filmes cadastrados de um arquivo JSON
        CarregarFilmes()
        
    elif ValorOpcao == 6: #Se 6, altera o idioma
        MudarIdioma()
    
def MenuPrincipal():
    """
    Exibe o menu principal da aplicação e processa a entrada do usuário.
    O menu é exibido no idioma atual configurado no sistema.
    Captura a entrada do usuário e valida se é uma opção válida antes de processá-la.
    """
    print("-----------------------------")
    print(lang.get_string("welcome"))
    print("0 -", lang.get_string("exit"))
    print("1 -", lang.get_string("register_movie"))
    print("2 -", lang.get_string("list_movies"))
    print("3 -", lang.get_string("remove_movie"))
    print("4 -", lang.get_string("save_movies"))
    print("5 -", lang.get_string("load_movies"))
    print("6 -", lang.get_string("change_language"))
    print("-----------------------------")

    try: #Tenta pegar a opção do usuário
        opcao = int(input(lang.get_string("select_option")))
        if opcao not in [0, 1, 2, 3, 4, 5, 6]: #Verifica se a opção é válida
            print(lang.get_string("invalid_option"))
            time.sleep(1)
            limpar_console()
            MenuPrincipal()
        else: #Se a opção for válida, chama a função OpcoesMenu()
            OpcoesMenu(opcao)
    except ValueError: #Se o usuário digitar algo que não seja um número, mostra uma mensagem de erro
        print(lang.get_string("enter_number"))
        time.sleep(1)
        limpar_console()
        MenuPrincipal()
  
if __name__ == "__main__":
    """
    Ponto de entrada principal do programa.
    Inicia a aplicação chamando a função PrimeiroMenu que configura o idioma
    antes de exibir o menu principal.
    """
    PrimeiroMenu()