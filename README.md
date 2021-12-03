# Django Livre Bank
Projeto final da academia Construdelas.

API de um banco fictício com clientes, contas e transações.

# Integrantes da equipe
- Bárbara Santos | https://github.com/barbarathais 
- Cecília Costa | https://github.com/CeciliaTPSCosta
- Lótus Inaiê | https://github.com/lotusinaie
- Saemi Yokomichi | https://github.com/masyokomichi
- Yuka Nakazima | https://github.com/YukaNakazima 

# Executando o projeto
* Criar virtualenv e ativá-la
* Executar o comando ` pip3 install -r requirements.txt ` 
* Executar o comando ` python3 manage.py runserver `
* Estará disponível em http://http://127.0.0.1:8000/

# Project routes 
* **POST** /api/v1/users - Creates a client;
* **GET** /api/v1/users - List all clients;
* **GET** /api/v1/users/<client_id> - Fetch a specific client;
* **PATCH** /api/v1/users/<client_id> - Patch a specific client;
* **DELETE** /api/v1/users/<client_id> - Delete a specific client;

* **POST** /api/v1/accounts - Creates an account;
* **GET** /api/v1/accounts - List all accounts;
* **PATCH** /api/v1/accounts/<account_id> - Patch a specific account;
* **DELETE** /api/v1/accounts/<account_id> - Delete a specific account;

* **POST** /api/v1/transfers - Creates a transfer;
* **GET** /api/v1/transfers - List all transfers;
* **GET** /api/v1/transfers/<transfer_id> - Fetch a specific transfer;
* **PATCH** /api/v1/transfers/<transfer_id> - Patch a specific transfer;
**DELETE** /api/v1/transfers/<transfer_id> - Delete a specific transfer;