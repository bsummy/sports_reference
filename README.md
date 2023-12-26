# sports_reference

## Hello!

I designed my solution to be very straightforward and clean, while also being somewhat defensive to the user. If this was a larger scale project, there'd be a whole different set of defensive concerns (data validity, table design, increased error checking)

I built a table data structure as an array of arrays by looping over the json data. I use indices to determine if the table is self referencing in a given row/col pair. Doing it this way allowed the table to be flexible given different sizes of data while allowing for clean code.

To print the table, I used a module called tabulate which displays our table in a neat grid. This module can be installed with `pip3 install tabulate`

If you wish to give the program a different file as input, you can do so following the execution command. Otherwise, the default name is
sr.json.
```
USAGE:
./sr.py <json filename>
```

## To run
Give the user execution permissions, then run the file with a filename argument.
```
chmod u+x sr.sh

./sr.sh sr.json
```
