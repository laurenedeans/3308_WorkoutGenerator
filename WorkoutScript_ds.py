#!/usr/bin/env python3
import os
import sys
import csv
import random
from collections import OrderedDict

muscle_group = { 
    'Arms': [],
    'Legs': [],
    'Back': [],
    'Abdominals': [],
    'Cardio': [],
    'Chest': [],
    }

with open('Exercises.csv', 'r') as f:
    csv_f = csv.reader(f)

    # group exercises by muscle group
    for row in csv_f:
        muscle_group.get(row[1], []).append(row)

# main function catches any errors in calling on program.
def main():
    if len(sys.argv)==1:
        print("\nUsage: ./WorkoutScript_ds.py WORKOUT_LENGTH TARGET_AREA EXPERIENCE GOAL EQUIPMENT")
        print(" -- WORKOUT_LENGTH = short (30min), medium (45min), long (60min)")
        print(" -- TARGET_AREA = Arms, Legs, Chest, Back, Abdominals, NONE")
        print(" -- EXPERIENCE = Beginner, Intermediate, Advanced")
        print(" -- GOAL = Mass, Strength, Endurance")
        print(" -- EQUIPMENT = Dumbells, Bar, Machine, Body Weight, Medicine Ball, Jump rope, Pool, Bicycle, ANY, NONE\n")
    else:
        length = sys.argv[1]
        EXPERIENCE = sys.argv[3]
        GOAL = sys.argv[4]
        argc = len(sys.argv)
        EQUIPMENT = ["Body Weight"]
        for i in range(5,argc):
            EQUIPMENT.append(sys.argv[i])
        #print(length, EXPERIENCE, GOAL, EQUIPMENT, "\n")
        filter_exer(muscle_group, EQUIPMENT, EXPERIENCE)
        start_wkout(length)

# This is part of the program that captures the person's choices.
# to add focus area, create a separate function.
def start_wkout(length_choice):
    WORKOUT_LENGTH = length_choice
    if WORKOUT_LENGTH == "short": predefined_set = (2,2,1,1,0)
    elif WORKOUT_LENGTH == "medium": predefined_set = (2,3,1,1,2)
    elif WORKOUT_LENGTH == 'long': predefined_set = (3,2,2,3,2)
    return make_workout(*predefined_set)

# Uses one function to create workouts of different lengths
def make_workout(arm_no, leg_no, back_no, chest_no, abs_no):
    Workout = []

    # adds additional exercises for targetted muscle group
    TARGET_AREA = sys.argv[2] # does nothing if NONE is selected
    if TARGET_AREA == "Arms": arm_no = arm_no + 2
    elif TARGET_AREA == "Legs": leg_no = leg_no + 2
    elif TARGET_AREA == "Back": back_no = back_no + 2
    elif TARGET_AREA == "Chest": chest_no = chest_no + 2
    elif TARGET_AREA == "Abdominals": abs_no = abs_no + 2

    focus_num = OrderedDict({
        'Arms': arm_no,
        'Legs': leg_no,
        'Back': back_no,
        'Abdominals': chest_no,
        'Chest': abs_no,
        })

    # creates a list of chosen workouts in list: Workout
    for area, num in focus_num.items():
        sample = random.sample(muscle_group[area], min(num, len(muscle_group[area])))
        Workout.extend(sample)
    
    # prints (or sends to another txt file) the proper, formatted list 
     
    wkout_list_idx = -1
    for exercise in Workout:
        print("\t" + exercise[0] + " -- " +  exercise[1] + " (" + exercise[2] + ")" + 
                " -- " + exercise[3] + ", " + exercise[4] + "\n")
	
    return Workout

# Filter list of exercises 
def filter_exer(MuscleGroup, Equipment, Experience):
    print("Filtered Exercises:")
    for area, exercise_list in MuscleGroup.items():
        for exercise in exercise_list:
            if Experience == "Advanced":
                if exercise[3] in Equipment:
                    print(exercise[0], "\n\t -- ", exercise[3], " -- ", exercise[5])
            elif Experience == "Intermediate":
                if (exercise[3] in Equipment) & (exercise[5] != "Advanced"):
                    print(exercise[0], "\n\t -- ", exercise[3], " -- ", exercise[5])
            else:
                if (exercise[3] in Equipment) & (exercise[5] == "Beginner"):
                    print(exercise[0], "\n\t -- ", exercise[3], " -- ", exercise[5])
    print("\n\n")

#if __name__ == "__main__":
 #   main()
main()

