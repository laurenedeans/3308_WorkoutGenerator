#!/usr/bin/env python3
import os
import sys
import csv

argc = len(sys.argv)

if argc == 1:
	print("\nUsage: ./exercies-query.py FILENAME MUSCLEGROUP ")
	print("\t MUSCLEGROUP : Arms, Back, Legs, Abdominals, Full body\n") 
else:
	fname = sys.argv[1]
	muscle_group = sys.argv[2]

	exercises = []

	with open(fname) as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		print("\nExercises focused on", muscle_group+":\n")
		for row in readCSV:
			if row[1] == muscle_group:
				print(row[0], ": \t", row[1], "("+row[2]+")")
