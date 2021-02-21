import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import logging


class Converter:
    def __init__(self, compression=None, log_level=logging.CRITICAL):
        self.compression = compression

        logging.basicConfig(format="", level=log_level)

    def convert_parquet_to_csv_file(self, in_file, out_file):
        try:
            df = pd.read_parquet(in_file)
            if out_file == '':
                out_file = '.'.join(in_file.rsplit('.', 1)[:-1])
            else:
                out_file = '.'.join(out_file.rsplit('.', 1)[:-1])
            out_file = out_file + '.csv'
            df.to_csv(out_file, index=False)
        except FileNotFoundError:
            logging.error("Failed! No such file " + in_file)
        except Exception:
            logging.error("Unknown error")
        else:
            logging.info("Success! File " + out_file)

    def convert_csv_to_parquet_file(self, in_file, out_file):
        try:
            df = pd.read_csv(in_file)
            if out_file == '':
                out_file = '.'.join(in_file.rsplit('.', 1)[:-1])
            else:
                out_file = '.'.join(out_file.rsplit('.', 1)[:-1])
            out_file = out_file + '.parquet'
            df.to_parquet(out_file, compression=self.compression)
        except FileNotFoundError:
            logging.error("Failed! No such file " + in_file)
        except pa.lib.ArrowException:
            logging.error("Failed! No such compression " + self.compression)
        except Exception:
            logging.error("Unknown error")
        else:
            logging.info("Success! File " + out_file)

    def print_parquet_schema(self, in_file):
        try:
            schema = pq.read_schema(in_file, memory_map=True)
            schema = pd.DataFrame(
                ({"column": name, "pa_dtype": str(pa_dtype)} for name, pa_dtype in zip(schema.names, schema.types)))
            schema = schema.reindex(columns=["column", "pa_dtype"], fill_value=pd.NA)
            print(schema)
        except FileNotFoundError:
            logging.error("Failed! No such file " + in_file)
        except pa.lib.ArrowInvalid:
            logging.error("Failed! Not a parquet file")
        except Exception:
            logging.error("Unknown error")
