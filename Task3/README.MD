## Films analytics program

Program analise films dataset, counts ratings and print top films searched by filters.

### Program structure

* main.py - execution file
* /db - sql scripts structure
* /data - dataset folder

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


``` shell
python main.py -N 3 -year_to 2007 -year_from 1900 -regexp "Life" -genres "Drama|Comedy"
```
``` shell
genre,title,year,rating
Drama,My Life as McDull (Mak dau goo si),2001,5.0
Drama,Train of Life (Train de vie),1998,4.5
Drama,Lifeboat,1944,4.28571
Comedy,My Life as McDull (Mak dau goo si),2001,5.0
Comedy,George Carlin: Life Is Worth Losing,2005,5.0
Comedy,Train of Life (Train de vie),1998,4.5
```