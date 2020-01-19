"""
Convert all txt files in current directory to csvs with the same file name.
"""
import sys
sys.path.append('../')
from convert_eprime import convert
import os

for file in os.listdir("."):
	if file.endswith(".txt"):
		out_file = file[:-3] + "csv"
		convert.text_to_csv(file, out_file)

