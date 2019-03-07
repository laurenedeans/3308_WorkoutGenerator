#!/usr/bin/env python3
import os
import sys
import csv

argc = len(sys.argv)

# Test for valid input, give usage message for invalid input
if argc==1:
	print("\nUsage: ExerciseQuery.py FILE_NAME MUSCLE_GROUP EQUIPMENT")
	print(" -- FILE_NAME = Exercises.csv (for now)")
	print(" -- MUSCLE_GROUP = Arms, Legs, Back, Abdominal, Full Body")
	print(" -- EQUIPMENT = Dumbells, Bar, Body Weight, Medicine Ball, Bicycle, Pool, Jump Rope")

else:
	FILE_NAME = sys.argv[1]
	MUSCLE_GROUP = sys.argv[2]
	exercises = []

	f = open(FILE_NAME)
	csv_f = csv.reader(f)

	for row in csv_f:
		if row[1]==MUSCLE_GROUP:
			exercises.append(row)

	# This block executes if an EQUIPMENT field is provided
	if argc==4:
		EQUIPMENT = sys.argv[3]
		exercises_filter = []
		for x in exercises:
			if x[3] == EQUIPMENT:
				exercises_filter.append(x)
		print("\nExercises focused on",MUSCLE_GROUP,"using", EQUIPMENT+":")
		if len(exercises_filter)==0:
			print(" -- ERROR: No exercises found for", MUSCLE_GROUP, "using", EQUIPMENT)
		else:
			for y in exercises_filter:
				print(" --", y[0], ":", y[1], "("+y[2]+")", "--", y[3])
	
	# This block executes if no EQUIPMENT field is provided
	if argc==3:
		print("\nExercises focused on", MUSCLE_GROUP+":")
		if len(exercises)==0:
			print(" -- ERROR: No exercises found for", MUSCLE_GROUP)
		else:
			for z in exercises:
				print(" --", z[0], ":", z[1], "("+z[2]+")", "--", z[3])

	print("\n")
