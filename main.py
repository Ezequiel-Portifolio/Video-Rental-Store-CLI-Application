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
import validation

def confirmar_acao(mensagem):
    """
    Solicita confirmação do usuário para ações destrutivas.
    
    Parâmetros:
    -----------
    mensagem : str
        Mensagem de confirmação a ser exibida
        
    Retorna:
    --------
    bool
        True se o usuário confirmar, False caso contrário
    """
    print(mensagem)
    resposta = input(lang.get_string("confirm_action")).lower().strip()
    return resposta in ['sim', 's', 'yes', 'y']


def obter_input_validado(prompt, validator_func, *validator_args):
    """
    Obtém input do usuário com validação.
    
    Parâmetros:
    -----------
    prompt : str
        Mensagem para solicitar input
    validator_func : function
        Função de validação a ser chamada
    *validator_args : tuple
        Argumentos adicionais para a função de validação
        
    Retorna:
    --------
    tuple
        Resultado da validação ou None se cancelado
    """
    max_attempts = 3
    attempts = 0
    
    while attempts < max_attempts:
        user_input = input(prompt)
        
        # Allow user to cancel with empty input on second attempt
        if attempts > 0 and not user_input.strip():
            if confirmar_acao(lang.get_string("cancel_operation")):
                return None
        
        result = validator_func(user_input, *validator_args)
        if result[0]:  # is_valid
            return result
        else:
            print(f"Erro: {result[-1]}")  # error_message
            attempts += 1
    
    print(lang.get_string("max_attempts_reached"))
    return None


def limpar_console():
    """
    Limpa a tela do console para melhor visualização do menu.
    Usa sequências de escape ANSI que são compatíveis com a maioria dos terminais.
    """
    print("\033[H\033[J", end="") #Limpa o console


def mudar_idioma():
    """
    Exibe menu para seleção de idioma e atualiza o idioma do sistema.
    Após a troca, retorna ao menu principal com o novo idioma aplicado.
    """
    print(lang.get_string("select_language"))
    
    # Use validated input for language selection
    result = obter_input_validado("", validation.validate_option_input, [1, 2])
    if result is None:
        menu_principal()
        return
    
    opcao = result[1]  # Get the validated option
    message = lang.set_language(opcao)
    print(message)
    
    time.sleep(1)
    limpar_console()
    menu_principal()

def primeiro_menu():
    """
    Função inicial que é chamada quando o programa começa.
    Primeiro solicita a seleção do idioma antes de mostrar o menu principal.
    """
    mudar_idioma()
    menu_principal()


def salvar_filmes():
    """
    Salva a lista atual de filmes em um arquivo JSON.
    Utiliza a função do módulo database para persistir os dados.
    """
    database.salvar_arquivoFilmes()
    entrada = input(lang.get_string("press_continue"))
    print(lang.get_string("loading"))
    time.sleep(1)
    limpar_console()
    menu_principal()


def remover_filmes():
    """
    Remove um filme do catálogo com base no ID fornecido pelo usuário.
    Exibe mensagem de confirmação ou erro se o filme não for encontrado.
    """
    if not database.filmes_cadastrados:
        print(lang.get_string("no_movies"))
        continuar = input(lang.get_string("press_exit"))
        print(lang.get_string("loading"))
        time.sleep(1)
        limpar_console()
        menu_principal()
        return
    
    # Show available movies
    print(lang.get_string("available_movies"))
    for filme_id in database.filmes_cadastrados.keys():
        print(f"- {filme_id}: {database.filmes_cadastrados[filme_id]['Nome']}")
    print()
    
    # Get movie ID with validation
    result = obter_input_validado(
        lang.get_string("enter_remove_id"),
        validation.validate_non_empty,
        "ID do filme"
    )
    
    if result is None:
        limpar_console()
        menu_principal()
        return
    
    id_filme = result[1]  # Get sanitized ID
    
    if id_filme in database.filmes_cadastrados:
        # Ask for confirmation before removing
        movie_name = database.filmes_cadastrados[id_filme]["Nome"]
        if confirmar_acao(f"Tem certeza que deseja remover o filme '{movie_name}' (ID: {id_filme})?"):
            del database.filmes_cadastrados[id_filme]
            print(lang.get_string("movie_removed"))
        else:
            print("Operação cancelada.")
    else:
        print(lang.get_string("movie_not_found"))
    
    continuar = input(lang.get_string("press_exit"))
    print(lang.get_string("loading"))
    time.sleep(1)
    limpar_console()
    menu_principal()


def carregar_filmes():
    """
    Carrega a lista de filmes de um arquivo JSON.
    Utiliza a função do módulo database para ler os dados salvos anteriormente.
    """
    database.carregar_arquivoFilmes()
    entrada = input(lang.get_string("press_continue"))
    print(lang.get_string("loading"))
    time.sleep(1)
    limpar_console()
    menu_principal()

def opcoes_menu(valor_opcao):
    """
    Processa a opção selecionada pelo usuário no menu principal.
    
    Parâmetros:
    -----------
    valor_opcao : int
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
    if valor_opcao == 0:  # Se a opção for 0, fecha o console
        print(lang.get_string("exiting"))
        time.sleep(1)
        sys.exit()
  
    elif valor_opcao == 1:  # Se a opção for 1, cadastra novo filme
        cadastrar_filme()
    
    elif valor_opcao == 2:  # Se a opção for 2, mostra os filmes cadastrados
        listar_filmes()

    elif valor_opcao == 3:  # Se a opção for 3, chama a função remover_filmes()
        remover_filmes()
    
    elif valor_opcao == 4:  # Se 4, salva os filmes cadastrados em um arquivo JSON
        salvar_filmes()
  
    elif valor_opcao == 5:  # Se 5, carrega os filmes cadastrados de um arquivo JSON
        carregar_filmes()
        
    elif valor_opcao == 6:  # Se 6, altera o idioma
        mudar_idioma()


def cadastrar_filme():
    """
    Cadastra um novo filme com validação de dados.
    """
    print(lang.get_string("register_movie"))
    print("=" * 40)
    
    # Validate movie ID
    id_result = obter_input_validado(
        lang.get_string("define_id"),
        validation.validate_movie_id,
        database.filmes_cadastrados
    )
    if id_result is None:
        limpar_console()
        menu_principal()
        return
    id_filme = id_result[1]
    
    # Validate movie name
    name_result = obter_input_validado(
        lang.get_string("enter_name"),
        validation.validate_non_empty,
        "Nome do filme"
    )
    if name_result is None:
        limpar_console()
        menu_principal()
        return
    nome = name_result[1]
    
    # Validate movie year
    year_result = obter_input_validado(
        lang.get_string("enter_year"),
        validation.validate_year
    )
    if year_result is None:
        limpar_console()
        menu_principal()
        return
    ano = year_result[1]
    
    # Validate movie genre
    genre_result = obter_input_validado(
        lang.get_string("enter_genre"),
        validation.validate_non_empty,
        "Gênero do filme"
    )
    if genre_result is None:
        limpar_console()
        menu_principal()
        return
    genero = genre_result[1]
    
    # Validate availability
    availability_result = obter_input_validado(
        lang.get_string("enter_availability"),
        validation.validate_availability
    )
    if availability_result is None:
        limpar_console()
        menu_principal()
        return
    disponibilidade_bool = availability_result[1]
    disponibilidade_display = availability_result[2]
    
    # Create movie entry
    database.filmes_cadastrados[id_filme] = {
        "Nome": nome,
        "Ano": ano,
        "Genero": genero,
        "Disponibilidade": disponibilidade_bool
    }
    
    print(lang.get_string("movie_registered"))
    print(f"ID: {id_filme} | Nome: {nome} | Ano: {ano} | Gênero: {genero} | Disponibilidade: {disponibilidade_display}")
    
    continuar = input(lang.get_string("press_exit"))
    print(lang.get_string("loading"))
    time.sleep(1)
    limpar_console()
    menu_principal()


def listar_filmes():
    """
    Lista todos os filmes cadastrados em formato melhorado.
    """
    if database.filmes_cadastrados:  # Se houver filmes cadastrados, mostra os filmes
        print(lang.get_string("list_movies"))
        print("=" * 70)
        
        for filme_id in database.filmes_cadastrados:
            filme = database.filmes_cadastrados[filme_id]
            disponibilidade_display = "Disponível" if filme["Disponibilidade"] else "Indisponível"
            
            print(f"{lang.get_string('movie_id')} {filme_id}")
            print(f"{lang.get_string('movie_name')} {filme['Nome']}")
            print(f"{lang.get_string('movie_year')} {filme['Ano']}")
            print(f"{lang.get_string('movie_genre')} {filme['Genero']}")
            print(f"{lang.get_string('movie_availability')} {disponibilidade_display}")
            print("-" * 70)
    else:  # Se não houver filmes cadastrados, mostra uma mensagem de erro
        print(lang.get_string("no_movies"))
    
    continuar = input(lang.get_string("press_exit"))
    print(lang.get_string("loading"))
    time.sleep(1)
    limpar_console()
    menu_principal()
    
def menu_principal():
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

    # Use validated input for menu selection
    result = obter_input_validado(
        lang.get_string("select_option"),
        validation.validate_option_input,
        [0, 1, 2, 3, 4, 5, 6]
    )
    
    if result is None:
        limpar_console()
        menu_principal()
        return
    
    opcao = result[1]  # Get the validated option
    opcoes_menu(opcao)
  
if __name__ == "__main__":
    """
    Ponto de entrada principal do programa.
    Inicia a aplicação chamando a função primeiro_menu que configura o idioma
    antes de exibir o menu principal.
    """
    primeiro_menu()