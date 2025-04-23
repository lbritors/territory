import asyncio
import sys
from titlecase import titlecase
from unidecode import unidecode
from brasil.db.sqlite_access import get_dimensao_from_db
from brasil.api.ibge_api import get_territory_api_ibge
from brasil.utils.csv_utils import look_csv

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

def normalize_name(area):
    print(titlecase(unidecode(area.strip().lower())))


async def main():
    nome = "Paraíba"
    ter_dict = look_csv()
    if nome in ter_dict.values():
        ter_id = next(key for key, value in ter_dict.items() if value == nome)
        dimensao = await get_dimensao_from_db(ter_id)
        if dimensao is not None:
            print(f" Territorio: {nome}, Dimensão: {dimensao}")
            return

        result = await get_territory_api_ibge(ter_id, nome)
        if result:
            print(f" Territorio: {result['nome']}, Dimensão: {result['dimensao']}, via IBGE")
        else:
            print(f"Falha ao buscar dados na api")

    else:
        print(f"Esse território não existe: {nome}")


if __name__ == "__main__":
    asyncio.run(main())


