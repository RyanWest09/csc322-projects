#!/usr/bin/env python
#To run:
#python sud2sattest.py p96sudoku.txt
#This will create a directory called cnf_files and have all 50 cnf files in there
#Then run this script ./minisattest.sh to input all 50 cnf at once to minisat

import fileinput
import textwrap
import sys
import os

row_list = []
clause_list = []
test_list = []


def parse_one_line(all_chars):
  split_groups = textwrap.wrap(all_chars,9)
  for line in split_groups:
    parse_many_lines(line)

def parse_many_lines(line):
  line = line.strip()
  row = [char for char in line]
  row_list.append(row)

def create_base_clauses():
  for count,row in enumerate(row_list):
    for column, value in enumerate(row):
      if value not in ["0",",",".","o"]:
        clause_list.append([str(count+1)+str(column+1)+str(value)])

def every_cell_contains_one_number(row,column):
  temp_list = []
  for value in range(1,10):
    temp_list.append(str(row)+str(column)+str(value))
  clause_list.append(temp_list)


def once_per_row(row, column,value):
  temp_list = []
  for i in range(row+1,10):
    temp_list.append(["-" + str(row) + str(column) + str(value) , "-" + str(i) + str(column) + str(value)])
  for pair in temp_list:
    clause_list.append(pair)

def once_per_column(row, column,value):
  temp_list = []
  for i in range(column+1,10):
    temp_list.append(["-" + str(row) + str(column) + str(value) , "-" + str(row) + str(i) + str(value)])
  for pair in temp_list:
    clause_list.append(pair)


def once_per_sub_grid1(grid_row,grid_column,value):
  temp_list = []
  for x in range(1,4):
    for y in range(1,4):
      for k in range(y+1,4):
        temp_list.append(["-" + str(3*grid_row + x) + str(3*grid_column + y) + str(value) , "-" + str(3*grid_row + x) + str(3*grid_column + k) + str(value)])
  for sub_list in temp_list:
    clause_list.append(sub_list)
  
def once_per_sub_grid2(grid_row,grid_column,value):
  temp_list = []
  for x in range(1,4):
    for y in range(1,4):
      for k in range(x+1,4):
        for l in range(1,4):
          temp_list.append(["-" + str(3*grid_row + x) + str(3*grid_column + y) + str(value) , "-" + str(3*grid_row + k) + str(3*grid_column + l) + str(value)])
  for sub_list in temp_list:
    clause_list.append(sub_list)


def write_to_output(filename):
    with open(filename, "w") as w:
        w.write("p cnf 729 " + (str(len(clause_list)) + "\n"))
        for row in clause_list:
            s = ' '.join(row) + " 0\n"
            w.write(s)       


def process_grid(grid, grid_number, output_dir):
    global row_list, clause_list
    row_list = []
    clause_list = []
    for line in grid.split('\n'):
        if len(line) > 0:
            parse_one_line(line)
    create_base_clauses()
    
    for row in range(1,10):
      for column in range(1,10):
        every_cell_contains_one_number(row,column)

    for row in range(1,10):
      for value in range(1,10):
        for column in range(1,9):
          once_per_column(row,column,value)

    for column in range(1,10):
      for value in range(1,10):
        for row in range(1,9):
          once_per_row(row,column,value)


    for value in range(1,10):
      for row in range(0,3):
        for column in range(0,3):
          once_per_sub_grid1(row,column,value)

    for value in range(1,10):
      for row in range(0,3):
        for column in range(0,3):
          once_per_sub_grid2(row,column,value)

    filename = 'puzzle{}.cnf'.format(grid_number)
    filepath = os.path.join(output_dir, filename)
    write_to_output(filepath)

#processing order
with open(sys.argv[1]) as f:
  file_contents = f.readlines()
for line in file_contents:
  if len(line) > 10:
    parse_one_line(line)
  else:
    parse_many_lines(line)


def main(output_dir='cnf_files'):
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    with open('p96sudoku.txt') as f:
        content = f.read().strip()
    grids = content.split('Grid')[1:]  #Split and remove the first empty entry
    for i, grid in enumerate(grids, start=1):
        grid_number = grid.split('\n', 1)[0].strip()
        grid_content = grid.split('\n', 1)[1].strip()
        process_grid(grid_content, grid_number, output_dir)

if __name__ == "__main__":
    main()

