import argparse

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
        consultar_dimensao(args.area)
    elif args.comando == "compara":
        comparar_dimensoes(args.area1, args.area2)


if __name__ == "__main__":
    main()


