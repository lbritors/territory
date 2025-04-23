import aiosqlite
import aiohttp
import asyncio
import json
from ..db.sqlite_access import save_territory_db


async def get_territory_api_ibge(id: int, nome: str):
    async with aiohttp.ClientSession() as session:
        url = f"https://servicodados.ibge.gov.br/api/v3/malhas/estados/{id}/metadados"
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    territory_data = data[0]
                    dimensao = float(territory_data["area"]["dimensao"])
                    territory_id = int(territory_data["id"])

                    await save_territory_db(territory_id, nome, dimensao)

                    return {
                        "id": territory_id,
                        "nome": nome,
                        "dimensao": dimensao
                    }
                else:
                    print(f"Erro na API do Ibge: Status {response.status}")
                    return None
        except aiohttp.ClientOSError as e:
            print(f"Erro na conexão com API do Ibge: {e}")
            return None
