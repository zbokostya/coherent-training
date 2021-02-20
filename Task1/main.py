import argparse
import logging

from converter import Converter


def main():
    parser = argparse.ArgumentParser(description='Convert csv and parquet formats', )
    parser.add_argument('-f', '--file', required=True, type=str, help="Name of file <parquet|csv> to convert")
    parser.add_argument('-o', '--outfile', default='', type=str, help="Name of file to output")

    parser.add_argument('-c', '--compression', default='none', choices=['none', 'snappy', 'gzip', 'brotli'],
                        help="Compression to use. Default = none")
    parser.add_argument('-q', '--quiet', action="store_true", help="Print logs or not. Default = false")

    required_group = parser.add_mutually_exclusive_group(required=True)
    required_group.add_argument('-tocsv', '--parquet2csv', action="store_true", help="Convert parquet to csv")
    required_group.add_argument('-topar', '--csv2parquet', action="store_true", help="Convert csv to parquet")
    required_group.add_argument('-s', '--schema', action="store_true", help="Print parquet schema")
    args = parser.parse_args()

    if args.quiet:
        log_level = logging.CRITICAL
    else:
        log_level = logging.DEBUG

    convert = Converter(
        compression=args.compression,
        quite=log_level
    )

    if args.parquet2csv:
        convert.convert_parquet_to_csv_file(in_file=args.file, out_file=args.outfile)
    elif args.csv2parquet:
        convert.convert_csv_to_parquet_file(in_file=args.file, out_file=args.outfile)
    elif args.schema:
        convert.print_parquet_schema(in_file=args.file)


if __name__ == '__main__':
    main()
