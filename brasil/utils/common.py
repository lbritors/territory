from .csv_utils import look_csv
from brasil.db.sqlite_access import get_dimensao_from_db
from brasil.api.ibge_api import get_territory_api_ibge
from typing import Dict

async def get_territory_data(area:str):
    ter_dict = look_csv()

    try:
        ter_id = int(area)
        if ter_id not in ter_dict:
            print(f"ID não encontrado em csv")
            return None
        ter_nome = ter_dict[ter_id]
    except ValueError:
        ter_id = next((key for key, value in ter_dict.items() if value.lower() == area.lower()), None)
        if ter_id is None:
            print(f"Territorio {area}  não encontrado em csv")
            return None
        ter_nome = ter_dict[ter_id]

    dimensao = await get_dimensao_from_db(ter_id)
    if dimensao is not None:
        return {"id": ter_id, "nome": ter_nome, "dimensao": dimensao, "from": "DB"}
    return await get_territory_api_ibge(ter_id, ter_nome)


async def get_territory_id(area: str, ter_dict: Dict[int, str]):
    try:
        ter_id = int(area)
        if ter_id not in ter_dict:
            return None
        return ter_id, ter_dict[ter_id]
    except ValueError:
        ter_id = next((key for key, value in ter_dict.items() if value.lower() == area.lower()), None)
        return {ter_id, ter_dict[ter_id]} if ter_id else None