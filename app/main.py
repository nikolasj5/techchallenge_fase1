from fastapi import FastAPI, HTTPException, status
from app.routes import producao, processamento, comercializacao, importacao, exportacao
from pydantic import BaseModel, Field
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi

# Cria a instância da aplicação FastAPI
app = FastAPI()

# Registrar os endpoints
app.include_router(producao.router)
app.include_router(processamento.router)
app.include_router(comercializacao.router)
app.include_router(importacao.router)
app.include_router(exportacao.router)

# Rota inicial
@app.get("/", summary="Página inicial da API")
async def home():
    return {
        "message": "Bem-vindo à API de Vitivinicultura!",
        "endpoints": [
            "/producao",
            "/processamento",
            "/comercializacao",
            "/importacao",
            "/exportacao"
        ]
    }