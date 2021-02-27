### Program structure

* main.py - execution file
* film.py - file with films class

### Execution

Program runs using command line or terminal  


**main.py**  

`usage: main.py [-h] [-N N] [-genres GENRES] [-year_from YEAR_FROM] [-year_to YEAR_TO] [-regexp REGEXP]`

**Optional**

| Argument | Help |
| ------------------------ | ----------------------------------- |
|  -h, --help            | show this help message and exit |
|  -N N                  | number of max rating films |
|  -genres GENRES        | filter by genres |
|  -year_from YEAR_FROM  | number of min year to filter |
|  -year_to YEAR_TO      | number of max year to filter |
|  -regexp REGEXP        | regular expression to filter |
|  -to_csv               | Print result to csv |


`python main.py -N 10 -year_to 2007 -year_from 1900 -regexp Waiting -genres Drama`
