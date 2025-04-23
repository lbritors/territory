import asyncio
import sys
from brasil.utils.common import get_territory_data
from brasil.api.ibge_api import get_territory_api_ibge
from brasil.utils.csv_utils import look_csv

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def main():
    nome = "Pará"
    id = 41
    # ter_dict = look_csv()
    # if nome in ter_dict.values():
    #     ter_id = next(key for key, value in ter_dict.items() if value == nome)
    #     dimensao = await get_dimensao_from_db(ter_id)
    #     if dimensao is not None:
    #         print(f" Territorio: {nome}, Dimensão: {dimensao}")
    #         return

    result = await get_territory_data(41)
    if result:
        print(f" Territorio: {result['nome']}, Dimensão: {result['dimensao']}")
    else:
        print(f"Falha ao buscar dados na api")


if __name__ == "__main__":
    asyncio.run(main())


