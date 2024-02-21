import sys
import textwrap

assigns_global = []

with open(sys.argv[1]) as f:
  file_contents = f.readlines()
  for line in file_contents:
    listify = line.split()
    assigns_global = [x for x in listify if "-" not in x]
    
unencoded = [x[2:] for x in assigns_global]

w = open(sys.argv[2],"w")
as_one = "".join(unencoded)
as_rows = textwrap.wrap(as_one,9)
for row in as_rows:
  split_row = [row[i:i+3] for i in range (0, len(row),3)]
  final = " ".join(split_row) + "\n"
  w.write(final)