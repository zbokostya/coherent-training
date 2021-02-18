import argparse

from converter import Converter


def arg_parser():
    parser = argparse.ArgumentParser(description='Convert csv and parquet formats', )
    parser.add_argument('-f', '--file', required=True, type=str, help="Name of file <parquet|csv> to convert")
    parser.add_argument('-o', '--outfile', default='', type=str, help="Name of file to output")
    parser.add_argument('-i', '--index', action="store_true", help="Use index or not. Default = false")
    parser.add_argument('-c', '--compression', default='none', choices=['none', 'snappy', 'gzip'],
                        help="Compression to use [none, snappy, gzip]. Default = none")

    required_group = parser.add_mutually_exclusive_group(required=True)
    required_group.add_argument('-tocsv', '--parquet2csv', action="store_true", help="Convert parquet to csv")
    required_group.add_argument('-topar', '--csv2parquet', action="store_true", help="Convert csv to parquet")
    required_group.add_argument('-s', '--schema', action="store_true", help="Print parquet schema")
    args = parser.parse_args()

    convert = Converter(
        index=args.index,
        compression=args.compression
    )

    if args.parquet2csv:
        convert.write_csv_file(file=args.file, out=args.outfile)
    elif args.csv2parquet:
        convert.write_parquet_file(file=args.file, out=args.outfile)
    elif args.schema:
        convert.write_parquet_schema(file=args.file)


if __name__ == '__main__':
    arg_parser()
