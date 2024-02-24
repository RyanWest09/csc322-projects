#!/usr/bin/env python3

import fileinput
import textwrap
import sys

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

#newfunction
def most_one_number_in_cell(row, column,value):
  temp_list = []
  for i in range(value+1,10):
    temp_list.append(["-" + str(row) + str(column) + str(value) , "-" + str(row) + str(column) + str(i)])
  for pair in temp_list:
    clause_list.append(pair)

#extended encoding constraint 2
def least_once_per_row(row, value):
  temp_list = []
  for column in range(1,10):
    temp_list.append(str(row) + str(column) + str(value))
  for clause in temp_list:
    clause_list.append(clause) 

#extended encoding constraint 3
def least_once_per_column(column, value):
  temp_list = []
  for row in range(1,10):
    temp_list.append(str(row) + str(column) + str(value))
  for clause in temp_list:
    clause_list.append(clause) 

#extended encoding constraint 4
#when this function is called we're looping through all 9 possible top left starting positions
#of the subgrid, so this function creates a clause for all cells in the subgrid relative to that starting position
def least_once_per_subgrid(row, column, value):
  temp_list = []
  for i in range(0, 3):
    for j in range(0, 3):
      temp_list.append(str(row+i)+str(column+j)+str(value))
  for clause in temp_list:
    clause_list.append(clause)


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


def write_to_output():
  w = open(sys.argv[2],"w")
  w.write("p cnf 729 " + (str(len(clause_list)) + "\n"))
  for row in clause_list:
    s = ' '.join(row)
    s = s + " 0\n"
    w.write(s)        
  

#processing order
with open(sys.argv[1]) as f:
  # with open("puzzle.txt") as f:
  file_contents = f.readlines()
for line in file_contents:
  if len(line) > 10:
    parse_one_line(line) #if input is in single line
  else:
    parse_many_lines(line) #if input is in multiple lines

create_base_clauses() #creates xyz encoding for each assigned digit (x-row number, y- column number and z- value)
#32 base clauses

#Every cell contains at least one number
#for each row, column we encode 1 or 2 or ... 9
#here each line of cnf = 1 cell 
# so total 81 clauses  
for row in range(1,10):
  for column in range(1,10):
    every_cell_contains_one_number(row,column)
#total - 113 clauses (including base)

#Each number appears at most once in every column
#9X9X8X9/2+113 = 3029
#2916 clauses for this
for row in range(1,10):
  for value in range(1,10):
    for column in range(1,9):
      once_per_column(row,column,value)
#total - 3029 clauses 


#Each number appears at most once in every row
#9X9X8X9/2 = 2916
#2916 clauses for this
for column in range(1,10):
  for value in range(1,10):
    for row in range(1,9):
      once_per_row(row,column,value)
#total - 5945 clauses 

for value in range(1,10):
  for row in range(0,3):
    for column in range(0,3):
      once_per_sub_grid1(row,column,value)

for value in range(1,10):
  for row in range(0,3):
    for column in range(0,3):
      once_per_sub_grid2(row,column,value)
##total - 8861 clauses
       
#new function  
#efficient code 
for row in range(1,10):
  for column in range(1,10):
    for value in range(1,9):
      most_one_number_in_cell(row,column,value)


#extended encoding 
#least once per row constraint
for row in range(1,10):
  for value in range(1,10):
    least_once_per_row(row,value)

#least once per column constraint
for column in range(1,10):
  for value in range(1,10):
    least_once_per_column(column,value)

#least once per subgrid constraint
#we iterate through 1, 4, 7 as the top left starting points of the subgrid for each row and column
for row in range(1, 8, 3):  
  for column in range(1, 8, 3):
    for value in range(1,10):
      least_once_per_subgrid(row, column, value)


    
write_to_output()



