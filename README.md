# Configuração do Projeto

## Pré-requisitos

Antes de começar, certifique-se de ter os seguintes requisitos instalados em sua máquina:

- **Pipenv**
- **Docker**

---

## Configuração do Ambiente

Siga os passos abaixo para configurar o projeto:

1. **Acesse o diretório do projeto** e execute o seguinte comando para ativar o ambiente virtual e instalar as dependências necessárias:

    ```bash
    pipenv shell
    pipenv install
    opentelemetry-bootstrap -a install
    ```

2. **Inicie os serviços do Docker** executando o comando abaixo:

    ```bash
    docker compose up -d
    ```

3. **Execute a aplicação** utilizando um dos comandos a seguir:

    - Para rodar com Uvicorn:
        ```bash
        opentelemetry-instrument uvicorn main:app
        ```

    - Para rodar com FastAPI em modo desenvolvimento:
        ```bash
        opentelemetry-instrument fastapi dev main.py
        ```

---

Agora, você está pronto para utilizar o projeto! 🚀
