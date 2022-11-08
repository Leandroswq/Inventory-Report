# Projeto Inventory Report

Esse projeto foi desenvolvido durante meus estudos em python. Ele possui o objetivo de gerar relatórios através de arquivos CSV, XML e JSON.

# Tecnologias utilizadas

* Python
* CSV
* XML
* JSON

# Como instalar as dependências

## 1 - Crie o ambiente virtual

~~~
python3 -m venv .venv
~~~

## 2 - Entre no ambiente virtual
~~~
source .venv/bin/activate
~~~

## 3 - Instale as dependências

Dependências de produção:

~~~
pip install -r requirements.txt
~~~

Dependências de produção e desenvolvimento:

~~~
pip install -r dev-requirements.txt
~~~

# Como executar

## 1 - Entre no ambiente virtual
Caso já esteja no ambiente virtual e as dependências pode pular essa etapa
~~~
source .venv/bin/activate
~~~

## 2 - Rode a aplicação
Ao instalar as dependências automaticamente a aplicação e o comando ```inventory_report``` ficará disponível no terminal do ambiente virtual. Para executar a aplicação basta digitar o comando ```inventory_report``` seguido do caminho do arquivo com os dados a serem analisados, na pasta data tem alguns exemplos de dados que a aplicação suporta.

~~~
inventory_report ./inventory_report/data/inventory.csv completo
~~~