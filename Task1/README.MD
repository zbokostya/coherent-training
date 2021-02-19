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
* -s Print parquet schema
* -tocsv Convert parquet to csv
* -topar Convert csv to parquet

**Optional**

* -o Name of file to output
* -i Use index or not. Default false
* -c Compression to use [none, snappy, gzip, brotli]. Default none
* -h To get help

`python main.py -f data/dataset.csv -o data/converted -topar -c gzip`  
`python main.py -f data/dataset.parquet -tocsv`  
`python main.py -f data/dataset.parquet -s`
