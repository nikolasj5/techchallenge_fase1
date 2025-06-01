Fase 1 do Tech Challenge

# API de Dados Vitivinícolas da Embrapa

Aplicação em Python com API REST para consulta dos dados públicos de vitivinicultura da Embrapa.

# Como Executar

## Pré-requisitos
- Python 3.8+
- Pip

## Instalação Local
```
# Crie e ative o ambiente virtual
python -m env venv
.\env\Scripts\activate   # Windows

# Instale as dependências
pip install -r requirements.txt

# Execute a API
uvicorn app.main:app --reload
```

Acesse a documentação:  
🔹 [http://localhost:8000/docs](http://localhost:8000/docs)  


## Tecnologias Utilizadas
- [FastAPI](https://fastapi.tiangolo.com/) - Framework para construção da API
- [Pandas](https://pandas.pydata.org/) - Processamento de dados
- [Requests](https://docs.python-requests.org/) - Requisições HTTP
- [Uvicorn](https://www.uvicorn.org/) - Servidor ASGI
