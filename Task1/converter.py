import pandas as pd
import pyarrow as pa
import logging

logging.basicConfig(format="", level=logging.DEBUG)


class Converter:
    def __init__(self, index, compression):
        self.index = index
        self.compression = compression

    def write_csv_file(self, file, out):
        try:
            df = pd.read_parquet(file)
            if out == '':
                out = file.rsplit('.', 1)[0]
            else:
                out = out.rsplit('.', 1)[0]
            out = out + '.csv'
            df.to_csv(out, index=self.index)
        except FileNotFoundError:
            logging.error("Failed! No such file " + file)
        else:
            logging.info("Success! File " + out)

    def write_parquet_file(self, file, out):
        try:
            df = pd.read_csv(file)
            if out == '':
                out = file.rsplit('.', 1)[0]
            else:
                out = out.rsplit('.', 1)[0]
            out = out + '.parquet'
            df.to_parquet(out, compression=self.compression)
        except FileNotFoundError:
            logging.error("Failed! No such file " + file)
        except pa.lib.ArrowException:
            logging.error("Failed! No such compression " + self.compression + " Only [none, snappy, gzip] supports")
        else:
            logging.info("Success! File " + out)

    def write_parquet_schema(self, file):
        try:
            df = pd.read_parquet(file)
            print(df)
        except FileNotFoundError:
            logging.error("Failed! No such file " + file)
        except OSError:
            logging.error("Failed! Not a parquet file")
