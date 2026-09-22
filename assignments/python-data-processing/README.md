# 📘 Assignment: Python Data Processing Project

## 🎯 Objective

Use Python to load, clean, and summarize data from a CSV file. Esta atividade ajuda a praticar leitura de arquivos, estruturas de dados, funções e processamento de informações em um cenário realista.

## 📝 Tasks

### 🛠️ Load and Explore the Dataset

#### Descrição
Leia um arquivo CSV com registros de alunos e entenda a estrutura dos dados antes de processá-los.

#### Requisitos
O programa concluído deve:

- Ler o arquivo `data.csv` usando `csv.DictReader` ou outra abordagem adequada
- Armazenar os registros em uma lista de dicionários
- Exibir o número total de registros
- Mostrar os nomes das colunas disponíveis
- Tratar valores ausentes ou vazios de forma simples e segura

### 🛠️ Compute Summary Statistics

#### Descrição
Crie funções para calcular estatísticas úteis a partir dos dados e apresentar um resumo legível para o usuário.

#### Requisitos
O programa concluído deve:

- Calcular a média de uma coluna numérica, como `score`
- Identificar o maior e o menor valor da coluna escolhida
- Filtrar registros por uma categoria, como `course` ou `group`
- Mostrar um relatório final em texto com os resultados principais
- Organizar a lógica em funções reutilizáveis
