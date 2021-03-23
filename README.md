# Movie-theater-programming-challenge
This is my solution to the "Movie Theater Seating" programming challenge.

Movie Theater Seating Challenge

Written by: Daniel Salazar

Language used: Python

Synopsis:
This program reads an input file passed from the command line argument and processes the data to reserve seats in a 10x20 movie theater. Also accounts for customer safety and satisfaction.

Customer safety: The program skips every other row and leaves a 3 space buffer between reservation groups.

Customer Satisfaction: To promote customer satisfaction, the program seats every reservation in the closest seat to the screen available, starting with row A. The reservations containing more than 1 person are also seated together. The program attempts to seat group reservations together even if that means there will be empty seats at the end of the row. For example, if there are only 4 safe empty seats at the end of row A, but a group of 5 needs to be seated, the entire group will be seated at the beginning of the next available row(row C). The 4 empty seats will still be considered for other smaller groups.

Assumptions:
-The input file is named and formatted correctly(based on the format given in instructions) with the rows in order (R001, R002...).
-The input file is called correctly: python Main.py /filepath/input.txt
-There will be no abnormally large reservations e.g: a group larger than 20
-Reservations cannot be changed after they are assigned

Instead of writing the output file to a specific directory, this program simply writes to the home directory so that it can be ran easily on any computer. Output.txt file path is displayed when the program is run to make it easier to find and open the file.

Buffer is not required for individuals within groups.

If the reservation group is abnormally large(larger than 20) or can't be seated together based on seats already being full, the program skips seating them.

How to run the program:
Navigate to program directory in command prompt
python main.py /filepath/input.txt

Command line output:
/filepath/Output.txt

Text contents of sample input file:
R001 2
R002 4
R003 2
R004 7
R005 2

Text contents of sample output file:
R001 A1,A2
R002 A6,A7,A8,A9
R003 A13,A14
R004 C1,C2,C3,C4,C5,C6,C7
R005 A18,A19

Possible Improvements:

Handle rare occasion of abnormally large group in a way that would increase customer satisfaction. Possibly split the group down the middle so they can be half & half seated together.

Go in first come-first serve order instead of attempting to fill all empty seats, to promote customer satisfaction. Keep in mind, this would split up groups.
