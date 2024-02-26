import sys
import textwrap

def main():
  with open(sys.argv[1]) as f:
    first_line = f.readline()
    if first_line == "UNSAT":
      unsatisifiable()
    else:
      file_contents = f.readlines()
      for line in file_contents:
        listify = line.split()
        assigns_global = [x for x in listify if "-" not in x]
      write_out(assigns_global)

def unsatisifiable():
  w = open(sys.argv[2],"w")
  w.write("Puzzle is not Satisfiable")


def write_out(assigns):
  unencoded = [x[2:] for x in assigns]
  print(unencoded)
  w = open(sys.argv[2],"w")
  as_one = "".join(unencoded)
  as_rows = textwrap.wrap(as_one,9)
  for row in as_rows:
    split_row = [row[i:i+3] for i in range (0, len(row),3)]
    final = " ".join(split_row) + "\n"
    w.write(final)


main()