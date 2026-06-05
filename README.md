# Weather App

Aplicação desenvolvida em Python utilizando a API Open-Meteo para consultar condições climáticas atuais, previsão dos próximos dias e manter um histórico local de consultas.

## Funcionalidades

* Consulta de clima atual por cidade
* Busca automática de coordenadas (Geocoding)
* Previsão climática para os próximos dias
* Histórico persistente em arquivo JSON
* Estatísticas sobre consultas realizadas
* Tratamento de erros de rede e dados inválidos
* Estrutura modular
* Programação Orientada a Objetos

## Tecnologias

* Python 3
* Requests
* Open-Meteo API
* JSON

## Instalação

Clone o repositório:

```bash
git clone git@github.com:patrickoliveira-dev/python-weather-app.git
```

Acesse a pasta do projeto:

```bash
cd python-weather-app
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Execução

Execute o programa com:

```bash
python main.py
```

## Estrutura do Projeto

```text
python-weather-app/
│
├── main.py
├── api.py
├── historico.py
├── historico.json
├── requirements.txt
├── README.md
│
├── models/
│   └── consulta_clima.py
```

## Estatísticas Disponíveis

O sistema registra e exibe:

* Total de consultas realizadas
* Cidade mais consultada
* Temperatura média registrada
* Maior temperatura registrada
* Menor temperatura registrada
* Primeira consulta realizada
* Última consulta realizada
* Top 3 cidades mais consultadas

## Objetivo

Este projeto foi desenvolvido com fins de estudo para praticar:

* Consumo de APIs REST
* Manipulação de JSON
* Programação Orientada a Objetos
* Modularização
* Persistência de dados
* Tratamento de exceções
* Git e GitHub

## Licença

Projeto desenvolvido para fins educacionais.