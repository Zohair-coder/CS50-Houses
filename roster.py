# TODO
import cs50
from sys import argv
from sys import exit
import csv

if len(argv) != 2:
    print("Incorrect number of arguments")
    exit()

house = argv[1]
db = cs50.SQL("sqlite:///students.db")

filtered_list = db.execute("SELECT first, middle, last, birth FROM students WHERE house = ? ORDER BY last ASC, first ASC", house)

for student in filtered_list:
    if student["middle"] is None:
        print("{} {}, born {}".format(student["first"], student["last"], student["birth"]))
    else:
        print("{} {} {}, born {}".format(student["first"], student["middle"], student["last"], student["birth"]))