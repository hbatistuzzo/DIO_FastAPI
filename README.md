<div align="center">
<img src="https://hermes.digitalinnovation.one/assets/diome/logo-full.svg" alt="Logo Bootcamp" width="80">
<h1> Coding The Future Vivo <br> Python AI Backend Developer </h1>
<img src="https://hermes.dio.me/files/assets/ef695d25-f647-45eb-b1ad-a25c124b28ca.png" alt="Logo Bootcamp" width="220">
</div>
 
Objetivo: desenvolver uma API com FastAPI, Python e Docker.

# Tecnologias Utilizadas

- pipenv - controle de versão
- PostgreSQL - banco de dados com docker-compose
- SQLAlchemy + Pydantic + Alembic - conexão com banco de dados
- FastAPI - desenvolver a aplicação


#  Solução do desafio

A estrutura geral do repositório e os códigos foram feitos seguindo o passo-a-passo da instrutora. Em seguida, foram adicionadas as modificações do desafio.

Para executar o código:
- Rodar banco de dados na pasta workout_api

```console
$ docker-compose up -d
```

- Rodar alembic na pasta do projeto (local do Makefile)
- 
```console
$ make run-migrations
```

- Rodar app na pasta do projeto

```console
$ make run
```
