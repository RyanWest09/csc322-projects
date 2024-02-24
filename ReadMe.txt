Group Members
Ryan West V00955247
Chase Cassels V00916567







Instructions to run minimal encoding implementations "sud2sat.py" and "sat2sud.py"

The script is written in python and employs for loops to generate the minimal encoding

To execute the Script on the Uvic Linux servers Use:

1. $ python sud2sat.py puzzle.txt puzzle.cnf
2. $ minisat puzzle.cnf assigns.txt > stat.txt
3. $ python sat2sud.py assigns.txt solution.txt
4. $ cat solution.txt

If the puzzle is satifiable then the solved puzzle will be written to solution.txt
If the puzzle is not satisfiable solution.txt will contain "Puzzle is not Satisfiable"





Instructions to run efficient encoding implementations "sud2sat2.py" and "sat2sud.py"

The script is written in python and employs for loops to generate the efficient encoding

To execute the Script on the Uvic Linux servers Use:

1. $ python sud2sat2.py puzzle.txt puzzle.cnf
2. $ minisat puzzle.cnf assigns.txt > stat.txt
3. $ python sat2sud.py assigns.txt solution.txt
4. $ cat solution.txt

If the puzzle is satifiable then the solved puzzle will be written to solution.txt
If the puzzle is not satisfiable solution.txt will contain "Puzzle is not Satisfiable"







Instructions to run extended encoding implementations "sud2sat3.py" and "sat2sud.py"

The script is written in python and employs for loops to generate the efficient encoding

To execute the Script on the Uvic Linux servers Use:

1. $ python sud2sat3.py puzzle.txt puzzle.cnf
2. $ minisat puzzle.cnf assigns.txt > stat.txt
3. $ python sat2sud.py assigns.txt solution.txt
4. $ cat solution.txt

If the puzzle is satifiable then the solved puzzle will be written to solution.txt
If the puzzle is not satisfiable solution.txt will contain "Puzzle is not Satisfiable"
