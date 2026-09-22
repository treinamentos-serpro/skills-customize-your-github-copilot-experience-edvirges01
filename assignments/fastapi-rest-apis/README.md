# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Aprenda a construir uma API REST usando o framework FastAPI. Você irá criar endpoints, validar dados com modelos Pydantic e organizar operações CRUD para uma coleção de tarefas.

## 📝 Tasks

### 🛠️ Criar a API e o Endpoint de Saúde

#### Descrição

Use o arquivo inicial para criar uma aplicação FastAPI. Adicione um endpoint que confirme que a API está funcionando e execute o servidor localmente para testar a resposta.

#### Requisitos

O programa completo deve:

- Criar uma instância de `FastAPI`
- Implementar `GET /health` retornando um objeto JSON com o status da API
- Iniciar a aplicação com Uvicorn e permitir testes em `http://127.0.0.1:8000`
- Exibir ou consultar a documentação automática em `/docs`

### 🛠️ Implementar Endpoints de Tarefas

#### Descrição

Modele uma tarefa e implemente endpoints REST para criar, listar, consultar, atualizar e remover tarefas. Nesta etapa, os dados podem ser armazenados em memória usando uma lista ou um dicionário.

#### Requisitos

O programa completo deve:

- Definir um modelo de entrada para tarefas com título, descrição opcional e status
- Implementar `GET /tasks` para listar todas as tarefas
- Implementar `POST /tasks` para criar uma tarefa e gerar um identificador
- Implementar `GET /tasks/{task_id}` para consultar uma tarefa específica
- Implementar `PUT /tasks/{task_id}` ou `PATCH /tasks/{task_id}` para atualizar uma tarefa
- Implementar `DELETE /tasks/{task_id}` para remover uma tarefa

### 🛠️ Validar Dados e Respostas HTTP

#### Descrição

Melhore a API para lidar corretamente com entradas inválidas e recursos inexistentes. Use os recursos do FastAPI para declarar restrições, retornar códigos HTTP apropriados e documentar as respostas esperadas.

#### Requisitos

O programa completo deve:

- Rejeitar títulos vazios ou maiores que o limite definido usando validação do Pydantic
- Retornar `404 Not Found` quando o identificador de uma tarefa não existir
- Retornar `201 Created` ao criar uma tarefa e `204 No Content` ao removê-la com sucesso
- Retornar respostas JSON consistentes para erros de validação
- Documentar os endpoints com títulos, descrições ou códigos de resposta visíveis em `/docs`
