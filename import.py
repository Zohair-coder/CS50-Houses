# TODO
import cs50
from sys import argv
from sys import exit
import csv

if len(argv) != 2:
    print("Incorrect number of arguments")
    exit()

db = cs50.SQL("sqlite:///students.db")

with open(argv[1], "r") as data:

    # Create DictReader
    reader = csv.DictReader(data)

    # Iterate over TSV file
    for row in reader:
        full_name = row["name"]
        full_name = full_name.split()
        first_name = full_name[0]

        if len(full_name) == 2:
            middle_name = None
            last_name = full_name[1]
        else:
            middle_name = full_name[1]
            last_name = full_name[2]

        db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",
                   first_name, middle_name, last_name, row["house"], row["birth"])
