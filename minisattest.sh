#!/bin/bash

#Directory where CNF files are stored
CNF_DIR="./cnf_files"

#Output directory for assigns and stats
OUTPUT_DIR="./sat"

mkdir -p "$OUTPUT_DIR"


for cnf_file in "$CNF_DIR"/*.cnf; do
  
    puzzle_number=$(basename "$cnf_file" .cnf)
    minisat "$cnf_file" "$OUTPUT_DIR/assigns${puzzle_number}.txt" > "$OUTPUT_DIR/stat${puzzle_number}.txt"
done