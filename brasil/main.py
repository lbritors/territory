from csv_utils import look_csv
import asyncio
from titlecase import titlecase
from unidecode import unidecode
from db.sqlite_access import get_dimensao_from_db, get_all_territories
from csv_utils import look_csv


def normalize_name(area):
    print(titlecase(unidecode(area.strip().lower())))


async def main():
    nome = "Bahia"
    ter_dict = look_csv()
    if nome in ter_dict.values():
        ter_id = next(key for key, value in ter_dict.items() if value == nome)
        dimensao = await get_dimensao_from_db(ter_id)
        print(nome, dimensao)
    else:
        print("deu ruim")
    territories = await get_all_territories()
    print(territories)


if __name__ == "__main__":
    ##look_csv(r"C:\Users\lbrit\OneDrive\Documentos\Programas\python\scientificloud\dict.csv")
    asyncio.run(main())


