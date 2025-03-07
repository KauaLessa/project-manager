# Projeto Gerenciador de 

Este é um projeto Django API com funcionalidades de gerenciamento de projetos, colaboradores, áreas tecnológicas e financiadores, utilizando Django e Django Rest Framework. O objetivo é fornecer uma API RESTful para interagir com os dados de forma eficiente e estruturada.

## 1) Como configurar o ambiente para executar o projeto

### Passo 1: Criando o ambiente virtual

1. Instale o `virtualenv` se ainda não o tiver:

   ```bash
   pip install virtualenv

2. Crie um ambiente virtual:

    ```bash
    python -m venv env

3. Ative o ambiente virtual

    ```bash
    source venv/bin/activate
    
### Passo 2: Clonando o repositório

1. Clone o repositório do projeto:

    ```bash
    git clone https://github.com/KauaLessa/project-manager
    cd project-manager
    
### Passo 3: Instalando as depêndencias

1. Instale as dependências necessárias, incluindo Django e Django Rest Framework

    ```bash
    pip install django
    pip install djangorestframework
    pip install validate-docbr
    ````

### Passo 4: Iniciando o servidor

Agora que o ambiente está configurado, você pode iniciar o servidor local do Django:

1. Aplique as migrações do banco de dados:

    ```bash
    python manage.py migrate

2. Crie um superusuário para acessar o painel administrativo

    ```bash
    python manage.py createsuperuser
    ```

3. Inicie o servidor de desenvolvimento

    ```bash
    python manage.py runserver
    ```

### Listagem de endpoints:
Aqui estão os endpoints disponíveis no projeto, de acordo com os padrões definidos anteriormente:

    Projetos
    GET /projetos/listar - Listar todos os projetos
    POST /projetos/cadastrar - Criar um novo projeto
    POST /projetos/<int:id>/inativar - Inativar um projeto
    PATCH /projetos/<int:id>/editar - Atualizar parcialmente um projeto
    GET /projetos/<int:id>/visualizar - Visualizar detalhes de um projeto específico
    GET /projetos/<int:id>/equipe - Obter informações da equipe de um projeto
    PATCH /projetos/<int:id>/equipe/atualizar - Atualizar equipe de um projeto
    GET /projetos/form - Exibir o formulário de criação/edição de projetos

    Colaboradores
    GET /colaboradores/listar - Listar todos os colaboradores
    POST /colaboradores/cadastrar - Criar um novo colaborador
    GET /colaboradores/<int:id>/visualizar - Visualizar detalhes de um colaborador específico
    PATCH /colaboradores/<int:id>/editar - Atualizar parcialmente um colaborador
    DELETE /colaboradores/<int:id>/excluir - Excluir um colaborador

    Áreas Tecnológicas
    GET /areas-tecnologicas/listar - Listar todas as áreas tecnológicas
    POST /areas-tecnologicas/cadastrar - Criar uma nova área tecnológica
    PATCH /areas-tecnologicas/<int:id>/editar - Atualizar parcialmente uma área tecnológica
    DELETE /areas-tecnologicas/<int:id>/excluir - Excluir uma área tecnológica
    
    Financiadores
    GET /financiadores/listar - Listar todos os financiadores
    POST /financiadores/cadastrar - Criar um novo financiador
    PATCH /financiadores/<int:id>/editar - Atualizar parcialmente um financiador
    DELETE /financiadores/<int:id>/excluir - Excluir um financiador


