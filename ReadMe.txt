Instructions to run minimal encoding implementations "sud2sat.py" and "sat2sud.py"

The script is written in python and employs for loops to generate the minimal encoding

To execute the Script on the Uvic Linux servers Use

1. $ python sud2sat.py <inputFile.txt> <outputFile1.cnf>
2. $ minisat <outputFile1.cnf> <outputFile2.txt>
3. $ python sat2sud.py <outputFile2.txt> <outputFile3.txt>

The solved puzzle will be written to <outputFile3.txt>





Instructions to run efficient encoding implementations "sud2sat2.py" and "sat2sud.py"

The script is written in python and employs for loops to generate the efficient encoding

To execute the Script on the Uvic Linux servers Use

1. $ python sud2sat2.py <inputFile.txt> <outputFile1.cnf>
2. $ minisat <outputFile1.cnf> <outputFile2.txt>
3. $ python sat2sud.py <outputFile2.txt> <outputFile3.txt>

The solved puzzle will be written to <outputFile3.txt>







Instructions to run extended encoding implementations "sud2sat3.py" and "sat2sud.py"

The script is written in python and employs for loops to generate the efficient encoding

To execute the Script on the Uvic Linux servers Use

1. $ python sud2sat3.py <inputFile.txt> <outputFile1.cnf>
2. $ minisat <outputFile1.cnf> <outputFile2.txt>
3. $ python sat2sud.py <outputFile2.txt> <outputFile3.txt>

The solved puzzle will be written to <outputFile3.txt>