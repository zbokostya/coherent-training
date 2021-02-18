### Required libraries

pyarrow  
`pip install pyarrow`  
pandas  
`pip install pandas`

### Program structure

* converter.py - file with converter class
* data/dataset.csv - directory with .csv file
* data/dataset.parquet - directory with .parquet file

### Execution

Program runs using command line or terminal  
**Required**

* -f <parquet|csv> Name of file <parquet|csv> to convert
* -o Name of file to output
* -s Print parquet schema
* -tocsv Convert parquet to csv
* -topar Convert csv to parquet

**Optional**

* -i Use index or not. Default false
* -c Compression to use [none, snappy, gzip]. Default none
* -h To get help

`python console_handler.py -f data/dataset.csv -o converted -topar -c gzip`  
`python main.py -f data/dataset.parquet -tocsv`  
`python main.py -f data/dataset.parquet -s`
