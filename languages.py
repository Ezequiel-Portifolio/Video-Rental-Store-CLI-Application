# Sistema de multilinguagem para a aplicação de locadora de vídeo
"""
Languages Module
---------------

This module implements the multilanguage system for the Video Rental Store application.
It contains dictionaries for each supported language (currently Portuguese and English),
and functions to manage text retrieval and language switching.

How it works:
1. Each language has a dictionary with keys representing text identifiers
2. The current_language variable points to the active language dictionary
3. The get_string() function retrieves text based on keys from the current language
4. The set_language() function allows changing the active language

To add a new language:
1. Create a new dictionary (e.g., es_ES for Spanish)
2. Copy all keys from an existing language dictionary
3. Translate all the values to the new language
4. Update the set_language() function to handle the new language option
5. Update the language selection menu in the main application
"""

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
    "enter_availability": "Digite a disponibilidade do filme (sim/não): ",
    "movie_registered": "Filme cadastrado com sucesso!",
    "no_movies": "Não há filmes cadastrados.",
    "available_movies": "Filmes disponíveis:",
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
    "language_changed": "Idioma alterado para Português",
    
    # Validação e confirmação
    "confirm_action": "Tem certeza? (sim/não): ",
    "cancel_operation": "Deseja cancelar a operação? (sim/não): ",
    "max_attempts_reached": "Número máximo de tentativas atingido. Retornando ao menu."
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
    "enter_availability": "Enter the movie availability (yes/no): ",
    "movie_registered": "Movie successfully registered!",
    "no_movies": "There are no registered movies.",
    "available_movies": "Available movies:",
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
    "language_changed": "Language changed to English",
    
    # Validation and confirmation
    "confirm_action": "Are you sure? (yes/no): ",
    "cancel_operation": "Do you want to cancel the operation? (yes/no): ",
    "max_attempts_reached": "Maximum number of attempts reached. Returning to menu."
}

# Idioma padrão
current_language = pt_BR

def get_string(key, *args):
    """
    Retrieves a string in the current language for the specified key.
    
    Parameters:
    -----------
    key : str
        The identifier for the text to be retrieved
    *args : tuple
        Optional arguments to format the string using str.format()
    
    Returns:
    --------
    str
        The translated text string, formatted with args if provided
        Returns "[Missing text: {key}]" if the key is not found
    
    Example:
    --------
    get_string("welcome") -> "Seja bem-vindo ao Sistema de Locadora de Vídeo."
    get_string("movies_loaded", 5) -> "5 filmes carregados com sucesso."
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
    Sets the current active language.
    
    Parameters:
    -----------
    language_code : int
        1 for Portuguese, 2 for English
    
    Returns:
    --------
    str
        Confirmation message in the newly set language
    
    Example:
    --------
    set_language(1) -> "Idioma alterado para Português"
    set_language(2) -> "Language changed to English"
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