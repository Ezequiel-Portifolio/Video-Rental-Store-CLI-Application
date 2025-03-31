# Sistema de multilinguagem para a aplicação de locadora de vídeo

# Dicionário para português
pt_BR = {
    # Menu principal
    "welcome": "Seja bem-vindo ao Sistema de Locadora de Vídeo.",
    "exit": "Sair",
    "register_movie": "Cadastrar Filme",
    "list_movies": "Listar Filmes",
    "remove_movie": "Remover Filme",
    "save_movies": "Salvar Lista de Filmes em JSON",
    "load_movies": "Carregar Lista de Filmes de JSON",
    "change_language": "Alterar Idioma",
    "select_option": "Digite a opção desejada: ",
    "invalid_option": "Opção inválida!",
    "enter_number": "Por favor, digite um número!",
    
    # Operações com filmes
    "movie_id": "ID do filme:",
    "movie_name": "Nome do filme:",
    "movie_year": "Ano do filme:",
    "movie_genre": "Gênero do filme:",
    "movie_availability": "Disponibilidade do filme:",
    "define_id": "Defina um ID para o filme: ",
    "enter_name": "Digite o nome do filme: ",
    "enter_year": "Digite o ano do filme: ",
    "enter_genre": "Digite o gênero do filme: ",
    "enter_availability": "Digite a disponibilidade do filme: ",
    "movie_registered": "Filme cadastrado com sucesso!",
    "no_movies": "Não há filmes cadastrados.",
    "enter_remove_id": "Digite o ID do filme que deseja remover: ",
    "movie_removed": "Filme removido com sucesso!",
    "movie_not_found": "Filme não encontrado.",
    
    # Geral
    "press_continue": "Pressione qualquer tecla para continuar",
    "press_exit": "Aperte qualquer tecla para sair",
    "loading": "Carregando...",
    "exiting": "Saindo do sistema...",
    
    # Operações de arquivo
    "file_saved": "Arquivo de filmes salvo com sucesso em dados_filmes.json",
    "save_error": "Erro ao salvar o arquivo de filmes: {0}",
    "movies_loaded": "{0} filmes carregados com sucesso.",
    "file_not_found": "Arquivo de filmes não encontrado. Verifique se o arquivo está no mesmo diretório.",
    "load_error": "Erro ao carregar o arquivo de filmes: {0}",
    
    # Idiomas
    "language_name": "Português",
    "select_language": "Selecione o idioma:\n1 - Português\n2 - English\n",
    "language_changed": "Idioma alterado para Português"
}

# Dicionário para inglês
en_US = {
    # Main menu
    "welcome": "Welcome to the Video Rental Store System.",
    "exit": "Exit",
    "register_movie": "Register Movie",
    "list_movies": "List Movies",
    "remove_movie": "Remove Movie",
    "save_movies": "Save Movie List to JSON",
    "load_movies": "Load Movie List from JSON",
    "change_language": "Change Language",
    "select_option": "Enter the desired option: ",
    "invalid_option": "Invalid option!",
    "enter_number": "Please, enter a number!",
    
    # Movie operations
    "movie_id": "Movie ID:",
    "movie_name": "Movie name:",
    "movie_year": "Movie year:",
    "movie_genre": "Movie genre:",
    "movie_availability": "Movie availability:",
    "define_id": "Set an ID for the movie: ",
    "enter_name": "Enter the movie name: ",
    "enter_year": "Enter the movie year: ",
    "enter_genre": "Enter the movie genre: ",
    "enter_availability": "Enter the movie availability: ",
    "movie_registered": "Movie successfully registered!",
    "no_movies": "There are no registered movies.",
    "enter_remove_id": "Enter the ID of the movie you want to remove: ",
    "movie_removed": "Movie successfully removed!",
    "movie_not_found": "Movie not found.",
    
    # General
    "press_continue": "Press any key to continue",
    "press_exit": "Press any key to exit",
    "loading": "Loading...",
    "exiting": "Exiting the system...",
    
    # File operations
    "file_saved": "Movie file successfully saved in dados_filmes.json",
    "save_error": "Error saving the movie file: {0}",
    "movies_loaded": "{0} movies successfully loaded.",
    "file_not_found": "Movie file not found. Check if the file is in the same directory.",
    "load_error": "Error loading the movie file: {0}",
    
    # Languages
    "language_name": "English",
    "select_language": "Select language:\n1 - Português\n2 - English\n",
    "language_changed": "Language changed to English"
}

# Idioma padrão
current_language = pt_BR

def get_string(key, *args):
    """
    Retorna uma string no idioma atual para a chave especificada.
    Se args for fornecido, eles são usados para formatar a string.
    """
    try:
        text = current_language[key]
        if args:
            return text.format(*args)
        return text
    except KeyError:
        return f"[Missing text: {key}]"

def set_language(language_code):
    """
    Define o idioma atual.
    language_code: 1 para português, 2 para inglês
    """
    global current_language
    
    if language_code == 1:
        current_language = pt_BR
        return current_language["language_changed"]
    elif language_code == 2:
        current_language = en_US
        return current_language["language_changed"]
    else:
        return "Invalid language code / Código de idioma inválido"