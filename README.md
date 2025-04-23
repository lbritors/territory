# Ferramenta de Consulta de Dimensões Territoriais do Brasil
Esta é uma ferramenta de linha de comando (CLI) desenvolvida em Python para consultar e comparar dimensões de territórios brasileiros (estados). 

Consulta de Dimensão: Permite consultar a dimensão (em km²) de um território brasileiro por nome ou ID, com geração de um gráfico de barras.

Comparação de Dimensões: Compara as dimensões de dois territórios, exibindo a diferença absoluta e gerando um gráfico comparativo.

Cache em Banco de Dados: Armazena os dados consultados em um banco SQLite para evitar consultas repetidas à API.

Gráficos: Gera visualizações com Matplotlib, salvas em uma pasta graphs/.

## Pré-requisitos

Python: Versão 3.9 ou superior.
* Dependências: Listadas em requirements.txt.

* Sistema Operacional: Testado em Windows

* Arquivos:
dict.csv: Arquivo CSV com mapeamento de IDs para nomes de territórios (ex.: id,nome\n25,Paraíba).

* .env (opcional): Arquivo para configurar caminhos do banco de dados e do CSV.



## Instalação

* Clone o repositório:
git clone <URL_DO_REPOSITORIO>



* Crie e ative um ambiente virtual (recomendado):
```python -m venv venv```



* Instale as dependências:
```pip install -r requirements.txt```


* Configure o ambiente (se necessário): Crie um arquivo .env na raiz do projeto (scientificloud/) com:
```DB_PATH=C:\caminho\para\database.db```
```CSV_PATH=C:\caminho\para\dict.csv```

Se não usar .env, certifique-se de que database.db e dict.csv estão na raiz do projeto.



## Uso
A ferramenta oferece dois comandos principais via CLI, além de um script de teste (main.py).
Comandos da CLI
Execute os comandos a partir da raiz do projeto.

* Consultar a dimensão de um território:
```python -m brasil.cli dimensao "<NOME_OU_ID>"```

Exemplo:

```python -m brasil.cli dimensao "Paraíba"```

Saída:
```
Território: Paraíba
Dimensão: 56467.242 km²
Gráfico salvo em: graphs/Paraíba_dimension.png
```

* Comparar dimensões de dois territórios:
```
python -m brasil.cli compara "<NOME_OU_ID_1>" "<NOME_OU_ID_2>"
```
Exemplo:
```
python -m brasil.cli compara "Paraíba" "São Paulo"
```
Saída:
```
Território 1: Paraíba (56467.242 km²)
Território 2: São Paulo (248219.485 km²)
Diferença: 191752.243 km²
Gráfico salvo em: graphs/Paraíba_vs_São_Paulo.png
```

## Dependências
As dependências estão listadas em requirements.txt:

* aiohttp: Para consultas assíncronas à API do IBGE.
* aiosqlite: Para gerenciamento assíncrono do banco SQLite.
* argparse: Para a interface de linha de comando.
* matplotlib: Para geração de gráficos.
* python-dotenv: Para carregar variáveis de ambiente.
