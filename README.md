# Video Rental Store CLI Application

## Overview
This is a command-line interface (CLI) application for managing a video rental store's inventory. The application supports multiple languages (currently Portuguese and English) and provides basic CRUD operations for movie management.

## Features
- Multi-language support (Portuguese and English)
- Movie registration with details (ID, name, year, genre, availability)
- Listing all registered movies
- Removing movies by ID
- Saving movie data to JSON file
- Loading movie data from JSON file
- Language switching capability

## Project Structure
The project consists of the following key files:
- `main.py`: The entry point of the application, contains the main menu logic
- `languages.py`: Contains the multi-language system implementation
- `database.py`: Handles persistence operations with JSON files
- `dados_filmes.json`: JSON file for storing movie data

## How the Application Works

### Languages System
The application uses a dictionary-based localization system in `languages.py`. Each supported language has a dictionary with keys representing text identifiers and values representing the translated text. The `get_string()` function retrieves text in the current language, and `set_language()` allows switching between languages.

### Movie Management
Movies are represented as dictionary entries with properties like ID, name, year, genre, and availability. The application allows:
- Adding new movies with unique IDs
- Listing all movies in a formatted table
- Removing movies by their ID
- Saving the movie collection to a JSON file
- Loading the movie collection from a JSON file

## Usage Instructions

### Running the Application
1. Make sure Python 3.x is installed on your system
2. Navigate to the project directory
3. Run `python main.py`

### Main Menu Options
1. Register Movie - Add a new movie to the inventory
2. List Movies - View all registered movies
3. Remove Movie - Delete a movie from the inventory by ID
4. Save Movies to JSON - Persist the current movie list to a file
5. Load Movies from JSON - Load previously saved movie list
6. Change Language - Switch between Portuguese and English
7. Exit - Close the application

## Data Persistence
Movie data is stored in a JSON file named `dados_filmes.json`. This allows the application to maintain its inventory between sessions.

## Extending the Application
To add support for additional languages:
1. Create a new dictionary in `languages.py` (e.g., `es_ES` for Spanish)
2. Add all the required text keys and translated values
3. Update the `set_language()` function to handle the new language option
4. Add the new language option to the language selection menu

## Technical Details
- Written in Python 3
- No external dependencies beyond the Python standard library
- Uses JSON for data persistence
- Implements a simple MVC-inspired architecture

## Future Improvements
- Customer management functionality
- Rental and return processes
- Search and filter capabilities
- Data validation and error handling
- Additional language support

---

# Aplicativo CLI de Locadora de Vídeos

## Visão Geral
Este é um aplicativo de interface de linha de comando (CLI) para gerenciar o inventário de uma locadora de vídeos. O aplicativo suporta múltiplos idiomas (atualmente Português e Inglês) e fornece operações básicas de CRUD para gerenciamento de filmes.

## Funcionalidades
- Suporte a múltiplos idiomas (Português e Inglês)
- Cadastro de filmes com detalhes (ID, nome, ano, gênero, disponibilidade)
- Listagem de todos os filmes cadastrados
- Remoção de filmes por ID
- Salvamento de dados de filmes em arquivo JSON
- Carregamento de dados de filmes a partir de arquivo JSON
- Capacidade de alternar entre idiomas

## Estrutura do Projeto
O projeto consiste nos seguintes arquivos principais:
- `main.py`: O ponto de entrada da aplicação, contém a lógica do menu principal
- `languages.py`: Contém a implementação do sistema de múltiplos idiomas
- `database.py`: Gerencia operações de persistência com arquivos JSON
- `dados_filmes.json`: Arquivo JSON para armazenamento de dados de filmes

## Como o Aplicativo Funciona

### Sistema de Idiomas
O aplicativo usa um sistema de localização baseado em dicionários no `languages.py`. Cada idioma suportado tem um dicionário com chaves representando identificadores de texto e valores representando o texto traduzido. A função `get_string()` recupera texto no idioma atual, e `set_language()` permite alternar entre idiomas.

### Gerenciamento de Filmes
Os filmes são representados como entradas de dicionário com propriedades como ID, nome, ano, gênero e disponibilidade. O aplicativo permite:
- Adicionar novos filmes com IDs únicos
- Listar todos os filmes em uma tabela formatada
- Remover filmes pelo seu ID
- Salvar a coleção de filmes em um arquivo JSON
- Carregar a coleção de filmes a partir de um arquivo JSON

## Instruções de Uso

### Executando o Aplicativo
1. Certifique-se de que o Python 3.x esteja instalado em seu sistema
2. Navegue até o diretório do projeto
3. Execute `python main.py`

### Opções do Menu Principal
1. Cadastrar Filme - Adiciona um novo filme ao inventário
2. Listar Filmes - Visualiza todos os filmes cadastrados
3. Remover Filme - Exclui um filme do inventário por ID
4. Salvar Filmes em JSON - Persiste a lista atual de filmes em um arquivo
5. Carregar Filmes de JSON - Carrega uma lista de filmes previamente salva
6. Alterar Idioma - Alterna entre Português e Inglês
7. Sair - Fecha o aplicativo

## Persistência de Dados
Os dados dos filmes são armazenados em um arquivo JSON chamado `dados_filmes.json`. Isso permite que o aplicativo mantenha seu inventário entre sessões.

## Estendendo o Aplicativo
Para adicionar suporte a idiomas adicionais:
1. Crie um novo dicionário em `languages.py` (por exemplo, `es_ES` para Espanhol)
2. Adicione todas as chaves de texto necessárias e valores traduzidos
3. Atualize a função `set_language()` para lidar com a nova opção de idioma
4. Adicione a nova opção de idioma ao menu de seleção de idiomas

## Detalhes Técnicos
- Escrito em Python 3
- Sem dependências externas além da biblioteca padrão do Python
- Usa JSON para persistência de dados
- Implementa uma arquitetura simples inspirada em MVC

## Melhorias Futuras
- Funcionalidade de gerenciamento de clientes
- Processos de aluguel e devolução
- Capacidades de pesquisa e filtragem
- Validação de dados e tratamento de erros
- Suporte a idiomas adicionais
