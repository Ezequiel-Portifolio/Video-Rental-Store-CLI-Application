"""
Validation Module - Video Rental Store CLI Application
----------------------------------------------------

This module provides input validation and sanitization functions
to ensure data integrity and security in the application.

Functions:
- validate_movie_id: Validates movie ID format and uniqueness
- validate_year: Validates and converts year input to integer
- validate_availability: Validates availability input to boolean
- sanitize_input: Basic input sanitization
- validate_non_empty: Validates non-empty string inputs
"""

import re
from datetime import datetime


def sanitize_input(user_input):
    """
    Sanitizes user input by removing potentially harmful characters.
    
    Parameters:
    -----------
    user_input : str
        The input string to sanitize
        
    Returns:
    --------
    str
        Sanitized input string
    """
    if not isinstance(user_input, str):
        return str(user_input)
    
    # Remove potential injection characters and excessive whitespace
    sanitized = user_input.strip()
    # Remove null bytes and control characters
    sanitized = ''.join(char for char in sanitized if ord(char) >= 32 or char in '\t\n\r')
    
    return sanitized


def validate_non_empty(input_string, field_name="Campo"):
    """
    Validates that input is not empty after sanitization.
    
    Parameters:
    -----------
    input_string : str
        The input to validate
    field_name : str
        Name of the field for error messages
        
    Returns:
    --------
    tuple
        (is_valid: bool, sanitized_value: str, error_message: str)
    """
    sanitized = sanitize_input(input_string)
    
    if not sanitized:
        return False, "", f"{field_name} não pode estar vazio."
    
    if len(sanitized) > 100:  # Reasonable length limit
        return False, "", f"{field_name} muito longo (máximo 100 caracteres)."
    
    return True, sanitized, ""


def validate_movie_id(movie_id, existing_movies):
    """
    Validates movie ID format and checks for uniqueness.
    
    Parameters:
    -----------
    movie_id : str
        The movie ID to validate
    existing_movies : dict
        Dictionary of existing movies to check for duplicates
        
    Returns:
    --------
    tuple
        (is_valid: bool, sanitized_id: str, error_message: str)
    """
    is_valid, sanitized_id, error = validate_non_empty(movie_id, "ID do filme")
    if not is_valid:
        return False, "", error
    
    # Check if ID already exists
    if sanitized_id in existing_movies:
        return False, "", "ID já existe. Escolha um ID diferente."
    
    # Basic format validation (alphanumeric and some special chars)
    if not re.match(r'^[A-Za-z0-9_-]+$', sanitized_id):
        return False, "", "ID deve conter apenas letras, números, hífen ou underscore."
    
    if len(sanitized_id) > 20:
        return False, "", "ID muito longo (máximo 20 caracteres)."
    
    return True, sanitized_id, ""


def validate_year(year_input):
    """
    Validates and converts year input to integer.
    
    Parameters:
    -----------
    year_input : str
        The year input to validate
        
    Returns:
    --------
    tuple
        (is_valid: bool, year_value: int, error_message: str)
    """
    sanitized = sanitize_input(year_input)
    
    if not sanitized:
        return False, 0, "Ano não pode estar vazio."
    
    try:
        year = int(sanitized)
        current_year = datetime.now().year
        
        if year < 1900:
            return False, 0, "Ano deve ser maior que 1900."
        
        if year > current_year + 5:  # Allow some future releases
            return False, 0, f"Ano não pode ser maior que {current_year + 5}."
        
        return True, year, ""
    
    except ValueError:
        return False, 0, "Ano deve ser um número válido."


def validate_availability(availability_input):
    """
    Validates availability input and converts to boolean.
    
    Parameters:
    -----------
    availability_input : str
        The availability input to validate
        
    Returns:
    --------
    tuple
        (is_valid: bool, availability_value: bool, display_value: str, error_message: str)
    """
    sanitized = sanitize_input(availability_input).lower()
    
    if not sanitized:
        return False, False, "", "Disponibilidade não pode estar vazia."
    
    # Accept various positive inputs
    positive_values = ['sim', 's', 'yes', 'y', 'disponível', 'disponivel', 'true', '1']
    negative_values = ['não', 'nao', 'n', 'no', 'indisponível', 'indisponivel', 'false', '0']
    
    if sanitized in positive_values:
        return True, True, "Disponível", ""
    elif sanitized in negative_values:
        return True, False, "Indisponível", ""
    else:
        return False, False, "", "Digite 'sim' ou 'não' para disponibilidade."


def validate_option_input(option_input, valid_options):
    """
    Validates menu option input.
    
    Parameters:
    -----------
    option_input : str
        The option input to validate
    valid_options : list
        List of valid option numbers
        
    Returns:
    --------
    tuple
        (is_valid: bool, option_value: int, error_message: str)
    """
    sanitized = sanitize_input(option_input)
    
    if not sanitized:
        return False, 0, "Opção não pode estar vazia."
    
    try:
        option = int(sanitized)
        
        if option not in valid_options:
            return False, 0, f"Opção inválida. Escolha entre: {', '.join(map(str, valid_options))}"
        
        return True, option, ""
    
    except ValueError:
        return False, 0, "Por favor, digite um número válido."