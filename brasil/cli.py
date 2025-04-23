import argparse
import asyncio
import sys
from brasil.utils.csv_utils import look_csv
from brasil.utils.common import get_territory_data, get_territory_id
from brasil.utils.plot import generate_dimension_plot, generate_difference_plot

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def consult_dimension(area: str):
    result = await get_territory_data(area)
    if result:
        print(f"Território: {result['nome']}")
        print(f"Dimensao: {result['dimensao']} km2")
        output_path = generate_dimension_plot(result['nome'], result['dimensao'])
        print(f"Gráfico salvo em: {output_path}")
    else:
        print("Falha ao buscar dados de território")


async def compare_dimensions(area1: str, area2:str):
    ter_dict = look_csv()
    ter_id1, ter_nome1 = await get_territory_id(area1, ter_dict) or (None, None)
    ter_id2, ter_nome2 = await get_territory_id(area2, ter_dict) or (None, None)

    if ter_id1 is None or ter_nome1 is None or ter_id2 is None or ter_nome2 is None:
        print(f"Território inválido: {area1}, {area2}")
        return

    result1 = await get_territory_data(ter_id1)
    result2 = await get_territory_data(ter_id2)

    if result1 is None or result2 is None:
        print(f"Falha ao buscar dados para um ou ambos os territórios: {ter_nome1}, {ter_nome2}")
        return

    diff = abs(result1["dimensao"] - result2["dimensao"])
    print(f"Território 1: {result1['nome']} ({result1['dimensao']})")
    print(f"Território 2: {result2['nome']} ({result2['dimensao']})")
    print(f"Diferença: {diff} km2")

    output_path = generate_difference_plot(
        result1["nome"], result1["dimensao"],
        result2["nome"], result2["dimensao"]
    )
    print(f"Gráfico salvo em: {output_path}")


def main():
    parser = argparse.ArgumentParser("Ferramenta para consultar e "
                                     "comparar dimensões de áreas do Brasil")

    subparser = parser.add_subparsers(dest="comando", required=True)

    arg_dimension = subparser.add_parser(name="dimensao", help="Consulta a dimensão da área")
    arg_dimension.add_argument("area", help="Nome da area ou ID")

    arg_compare = subparser.add_parser(name="compara", help="Compara a diferença"
                                                            " de dimensões de duas áreas")
    arg_compare.add_argument("area1", help="Nome ou ID da primeira área")
    arg_compare.add_argument("area2", help="Nome ou ID da segunda área")

    args = parser.parse_args()

    if args.comando == "dimensao":
        asyncio.run(consult_dimension(args.area))
    elif args.comando == "compara":
        asyncio.run(compare_dimensions(args.area1, args.area2))


if __name__ == "__main__":
    main()


