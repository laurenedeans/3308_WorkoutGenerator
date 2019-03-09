#!/usr/bin/env python3
import os
import sys
import csv
import random

Arms = []
Legs = []
Back = []
Abdominals = []
Cardio = []
Chest = []

def main():
    if len(sys.argv)==1:
        print("\nUsage: ./WorkoutScript_ds.py WORKOUT_LENGTH TARGET_AREA")
        print(" -- WORKOUT_LENGTH = short (30min), medium (45min), long (60min)\n")
    else:
        length = sys.argv[1]
        start_wkout(length)

def start_wkout(length_choice):
    WORKOUT_LENGTH = length_choice
    f = open('Exercises.csv')
    csv_f = csv.reader(f)

    # group exercises by muscle group
    for row in csv_f:
        if row[1]=='Arms': Arms.append(row)
        elif row[1]=='Legs': Legs.append(row)
        elif row[1]=='Back': Back.append(row)
        elif row[1]=='Abdominals': Abdominals.append(row)
        elif row[1]=='Cardio': Cardio.append(row)
        elif row[1]=='Chest': Chest.append(row)
    print("\nHere is your", WORKOUT_LENGTH, "workout:\n")
    if WORKOUT_LENGTH == "short": make_workout(2,2,1,1,0)
    elif WORKOUT_LENGTH == "medium": make_workout(2,2,1,1,3)
    elif WORKOUT_LENGTH == 'long': make_workout(2,3,3,1,3)

# Uses one function to create workouts of different lengths
def make_workout(arm_no, leg_no, back_no, chest_no, abs_no):
	Workout = []
	for i in range(arm_no):
		Workout.append(random.choice(Arms))
	for i in range(leg_no):
		Workout.append(random.choice(Legs))
	for i in range(back_no):
		Workout.append(random.choice(Back))
	for i in range(chest_no):
		Workout.append(random.choice(Chest))
	for i in range(abs_no):
		Workout.append(random.choice(Abdominals))
	
	print("Arm Exercises ("+str(arm_no)+" randomly chosen):")
	for i in range(arm_no):
		print("\t",Workout[i][0], "--", Workout[i][1], "("+Workout[i][2]+")", "--", Workout[i][3]+",", Workout[i][4])
	
	print("\nLeg Exercises ("+str(leg_no)+" randomly chosen):")
	for i in range(leg_no):
		print("\t",Workout[i+arm_no][0], "--", Workout[i+arm_no][1], "("+Workout[i+arm_no][2]+")", "--", Workout[i+arm_no][3]+",", Workout[i+arm_no][4])
	
	print("\nBack Exercises ("+str(back_no)+" randomly chosen):")
	for i in range(back_no):
		print("\t",Workout[i+arm_no+leg_no][0], "--", Workout[i+arm_no+leg_no][1], "("+Workout[i+arm_no+leg_no][2]+")", "--", Workout[i+arm_no+leg_no][3]+",", Workout[i+arm_no+leg_no][4])
	
	print("\nChest Exercises ("+str(chest_no)+" randomly chosen):")
	for i in range(chest_no):
		print("\t",Workout[i+arm_no+leg_no+back_no][0], "--", Workout[i+arm_no+leg_no+back_no][1], "("+Workout[i+arm_no+leg_no+back_no][2]+")", "--", Workout[i+arm_no+leg_no+back_no][3]+",", Workout[i+arm_no+leg_no+back_no][4])

	print("\nAbdominal Exercises ("+str(abs_no)+" randomly chosen):")
	for i in range(abs_no):
		print("\t",Workout[i+arm_no+leg_no+back_no+chest_no][0], "--", Workout[i+arm_no+leg_no+back_no+chest_no][1], "("+Workout[i+arm_no+leg_no+back_no+chest_no][2]+")", "--", Workout[i+arm_no+leg_no+back_no+chest_no][3]+",", Workout[i+arm_no+leg_no+back_no+chest_no][4])
	print("\n")



#if __name__ == "__main__":
 #   main()
main()

