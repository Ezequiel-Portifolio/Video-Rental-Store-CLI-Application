# Video Rental Store CLI Application - Architecture Documentation

## Architecture Overview

The Video Rental Store CLI Application follows a simple modular architecture with clear separation of concerns. The application is designed to be maintainable, extensible, and easy to understand.

## System Components

### 1. User Interface (UI)
The application uses a command-line interface (CLI) implemented in `main.py`. It handles:
- Displaying the menu options
- Collecting user input
- Calling appropriate functions based on user selections
- Presenting results to the user

### 2. Language System
Implemented in `languages.py`, this component provides multi-language support through:
- Language dictionaries (`pt_BR` and `en_US`)
- Function to retrieve text strings (`get_string`)
- Function to switch languages (`set_language`)

### 3. Movie Data Model
The application uses a dictionary structure to represent movies:
- Each movie is stored as a key-value pair in the `filmes_cadastrados` dictionary
- The key is the movie's unique ID
- The value is another dictionary containing movie properties (name, year, genre, availability)

### 4. Data Persistence
Implemented in `database.py`, this component handles:
- Maintaining the in-memory movie collection during runtime
- Serializing the movie dictionary to a JSON file
- Deserializing the JSON data back into the movie dictionary structure

## Application Flow

1. The application starts by loading the main menu
2. User selects an option from the menu
3. The application processes the selected operation:
   - Adding a movie: Collects details and adds to the movie dictionary
   - Listing movies: Displays all movies in a formatted table
   - Removing a movie: Takes an ID and removes the corresponding movie
   - Saving/Loading: Interacts with the JSON file
   - Changing language: Calls the language system to update the UI language
4. After completing an operation, the application returns to the main menu
5. The cycle continues until the user chooses to exit

## Data Flow

1. User Input → UI → Business Logic → Data Model → Data Storage
2. Data Storage → Data Model → Business Logic → UI → User Display

## Design Patterns

The application implements:
- **Singleton Pattern**: The language system maintains a single instance of the current language
- **Repository Pattern**: The database module acts as a repository for movie data
- **Command Pattern**: Each menu option corresponds to a specific command or operation

## Extension Points

The application can be extended in several ways:
1. Adding new languages by creating additional language dictionaries
2. Adding new movie properties by extending the movie dictionary structure
3. Adding new menu options for additional functionality
4. Implementing more sophisticated data storage (e.g., database)
5. Adding user authentication and multiple user support

## Technical Decisions

1. **CLI Interface**: Chosen for simplicity and ease of implementation
2. **JSON Storage**: Selected for human-readable data format and no external dependencies
3. **Dictionary-based Localization**: Provides a straightforward approach to multi-language support
4. **Modular Architecture**: Enables easier maintenance and extension of the codebase

---

# Aplicativo CLI de Locadora de Vídeos - Documentação da Arquitetura

## Visão Geral da Arquitetura

O Aplicativo CLI de Locadora de Vídeos segue uma arquitetura modular simples com clara separação de responsabilidades. A aplicação foi projetada para ser manutenível, extensível e fácil de entender.

## Componentes do Sistema

### 1. Interface do Usuário (UI)
A aplicação utiliza uma interface de linha de comando (CLI) implementada no arquivo `main.py`. Ela gerencia:
- Exibição das opções de menu
- Coleta da entrada do usuário
- Chamada de funções apropriadas com base nas seleções do usuário
- Apresentação dos resultados ao usuário

### 2. Sistema de Idiomas
Implementado no arquivo `languages.py`, este componente fornece suporte a múltiplos idiomas através de:
- Dicionários de idiomas (`pt_BR` e `en_US`)
- Função para recuperar strings de texto (`get_string`)
- Função para alternar entre idiomas (`set_language`)

### 3. Modelo de Dados de Filmes
A aplicação utiliza uma estrutura de dicionário para representar filmes:
- Cada filme é armazenado como um par chave-valor no dicionário `filmes_cadastrados`
- A chave é o ID único do filme
- O valor é outro dicionário contendo propriedades do filme (nome, ano, gênero, disponibilidade)

### 4. Persistência de Dados
Implementada no arquivo `database.py`, este componente gerencia:
- Manutenção da coleção de filmes em memória durante a execução
- Serialização do dicionário de filmes para um arquivo JSON
- Desserialização dos dados JSON de volta para a estrutura de dicionário de filmes

## Fluxo da Aplicação

1. A aplicação inicia carregando o menu principal
2. O usuário seleciona uma opção do menu
3. A aplicação processa a operação selecionada:
   - Adicionar um filme: Coleta detalhes e adiciona ao dicionário de filmes
   - Listar filmes: Exibe todos os filmes em uma tabela formatada
   - Remover um filme: Recebe um ID e remove o filme correspondente
   - Salvar/Carregar: Interage com o arquivo JSON
   - Alterar idioma: Chama o sistema de idiomas para atualizar o idioma da UI
4. Após completar uma operação, a aplicação retorna ao menu principal
5. O ciclo continua até que o usuário escolha sair

## Fluxo de Dados

1. Entrada do Usuário → UI → Lógica de Negócio → Modelo de Dados → Armazenamento de Dados
2. Armazenamento de Dados → Modelo de Dados → Lógica de Negócio → UI → Exibição para o Usuário

## Padrões de Design

A aplicação implementa:
- **Padrão Singleton**: O sistema de idiomas mantém uma única instância do idioma atual
- **Padrão Repositório**: O módulo database atua como um repositório para dados de filmes
- **Padrão Command**: Cada opção de menu corresponde a um comando ou operação específica

## Pontos de Extensão

A aplicação pode ser estendida de várias maneiras:
1. Adicionando novos idiomas através da criação de dicionários de idioma adicionais
2. Adicionando novas propriedades de filme estendendo a estrutura do dicionário de filmes
3. Adicionando novas opções de menu para funcionalidades adicionais
4. Implementando armazenamento de dados mais sofisticado (por exemplo, banco de dados)
5. Adicionando autenticação de usuário e suporte a múltiplos usuários

## Decisões Técnicas

1. **Interface CLI**: Escolhida pela simplicidade e facilidade de implementação
2. **Armazenamento JSON**: Selecionado pelo formato de dados legível por humanos e sem dependências externas
3. **Localização Baseada em Dicionário**: Fornece uma abordagem direta para suporte a múltiplos idiomas
4. **Arquitetura Modular**: Permite manutenção e extensão mais fácil do código-fonte
