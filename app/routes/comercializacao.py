from fastapi import APIRouter, HTTPException, Depends
from app.scraper import EmbrapaScraper

router = APIRouter(prefix="/comercializacao", tags=["Comercialização"])

@router.get("/", summary="Dados de produção vitivinícola")
async def get_producao():
    scraper = EmbrapaScraper()
    data = scraper.get_data("comercializacao")
    if "error" in data:
        raise HTTPException(status_code=500, detail=data["error"])
    return data