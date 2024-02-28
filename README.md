# Currency Converter API

Esse projeto representa uma API usada para fazer a conversão entre diversos tipos de moedas com base em cotações disponibilizadas em tempo real. As moedas usadas são dólar(USD), real(BRL), euro(EUR), bitcoin(BTC) e etherium(ETH).


## Tecnologias usadas

1. Python 3.11.
2. FastAPI e todas as suas dependências para o desenvolvimento da API.
3. pytest e bibliotecas auxiliares para a execução dos testes unitários.


## Instruções para executar a aplicação

Primeiramente, é necessário fazer um clone desse repositório para o seu computador.
Abra um terminal no Linux e execute o comando abaixo.

```git clone https://github.com/Gflg/currency-converter-api```

Uma vez que o repositório for clonado com sucesso, basta entrar no diretório criado.

```cd currency-converter-api```

É preciso criar um arquivo **.env** baseado no arquivo **.env.sample**. A API key pode ser criada gratuitamente com a criação de uma conta nesse [site](https://currencybeacon.com/) utilizado para recuperar as cotações das moedas em tempo real. Você também pode utilizar a API key usada no desenvolvimento dessa aplicação para facilitar o seu uso: 

<details>
  <summary>API key</summary>
  B2H3NE0qJLnaS4XsEODlsLwY6K0IzArh
  
</details><br>

Existe 3 formas distintas para executar essa aplicação:

1. Docker
2. Docker-compose
3. Executando com o Python local

### Docker

Existe um arquivo Dockerfile criado para carregar a API criada dentro de um container Docker.
Para instalar e executar a aplicação, basta inserir os comandos abaixo em um terminal.

```docker build -t <tag_name>:latest .```

O comando acima irá criar uma imagem dentro do Docker instalado no seu computador a tag definida antes da execução desse comando. Depois disso, basta rodar um container com essa imagem criada. Exemplo de comando para executar a aplicação na porta 5000:

```docker run -h localhost -p 5000:5000 -d --name <container_name> <tag_name>:latest```

### Docker-compose

Existe um arquivo docker-compose.yml com todas as propriedades definidas para a criação de um container Docker para essa aplicação. Quaisquer alterações feitas durante a execução da aplicação com esse método, serão refletidas em tempo real na aplicação pois há uma sincronização dos arquivos dessa API com o container Docker. Para executar a aplicação, basta executar o comando abaixo:

```docker-compose up --build```

A aplicação é executada, por padrão, na porta 5000.

### Executando com o Python local

Para seguir esse tipo de execução, é preciso ter um Python instalado em seu computador. Como esse projeto foi desenvolvido utilizando o Python 3.11, é recomendado que essa versão seja a versão utilizada em seu computador.

É necessário instalar as dependências do projeto com o comando abaixo:

```pip install -r requirements.txt```

Após isso, é necessário ir até o diretório app/.

```cd app```

Nesse diretório, basta executar a aplicação do FastAPI com o comando abaixo:

```uvicorn main:app --port 5000 --reload```

A aplicação estará rodando na porta 5000, como nos outros tipos de execução.
Também é possível executar os testes da aplicação com o comando abaixo:

```python -m pytest tests/```