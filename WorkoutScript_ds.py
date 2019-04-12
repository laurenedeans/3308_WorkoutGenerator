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
    if len(sys.argv)==1:    # Usage statement to show how to call the script (type "./WorkoutScript_ds.py")
        print("\nUsage: ./WorkoutScript_ds.py WORKOUT_LENGTH TARGET_AREA EXPERIENCE GOAL EQUIPMENT")
        print(" -- WORKOUT_LENGTH = short (30min), medium (45min), long (60min)")  # sys.argv[1]
        print(" -- TARGET_AREA = Arms, Legs, Chest, Back, Abdominals, NONE")  # sys.argv[2]
        print(" -- EXPERIENCE = Beginner, Intermediate, Advanced")  # sys.argv[3]
        print(" -- GOAL = Mass, Strength, Endurance")  # sys.argv[4]  (Sets & Reps & Weight choices)
        print(" -- EQUIPMENT = Dumbells, Bar, Machine, Body Weight, Medicine Ball, Jump rope, Pool, Bicycle, ANY, NONE\n")  # sys.argv[5] ....
        # bicep curls "bar, dumbell, kettlebell" --> EQUIPMENT "bar, dumbell" --> bicep curls "bar, dumbell" 
    else:
        # Command line arguments 
        length = sys.argv[1]
        EXPERIENCE = sys.argv[3]
        GOAL = sys.argv[4]
        argc = len(sys.argv)
        EQUIPMENT = ["Body Weight"]
        for i in range(5,argc):    # creates list of equipment options
            EQUIPMENT.append(sys.argv[i])
        
        filter_exer(muscle_group, EQUIPMENT, EXPERIENCE)  # filters existing dictionary to only contain value exercises
        start_wkout(length)  # Begins process of generating workout

def start_wkout(length_choice):
    # First step in creating workout: Uses WORKOUT_LENGTH to determine predefined_set, then calls make_workout()
    #  -- predefined_set = (Arms, Legs, Back, Chest, Abs)
    #  -- Input: WORKOUT_LENGTH ("short", "medium", "long")
    #  -- Output: Same output as make_workout()
    
    #  -- short = 6, medium = 9, long = 12
    #  -- TARGET_AREA: list 0-5 muscle groups.
    #  ------ NONE: Full-body

    WORKOUT_LENGTH = length_choice
    if WORKOUT_LENGTH == "short": predefined_set = (2,2,1,1,0)      # 6 exercises
    elif WORKOUT_LENGTH == "medium": predefined_set = (2,3,1,1,2)   # 9 exercises
    elif WORKOUT_LENGTH == 'long': predefined_set = (3,2,2,3,2)     # 12 exercises

    return make_workout(*predefined_set)


def make_workout(arm_no, leg_no, back_no, chest_no, abs_no):
    # Second step in creating workout:
    #  -- Input: predefined_set (from start_workout()), TARGET_AREA (command line arg.)
    #  -- Output: List in the form [sets, reps, weight, exercise_list]
    
    Workout = []

    # adds additional exercises for targetted muscle group
    # -- This is where TARGET_AREA is implemented: Adds +2 to whatever target area selected, on top of predefined_set from WOORKOUT_LENGTH
    
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
        'Chest': chest_no,
        'Abdominals': abs_no,
        })

    # Takes random sample from dictionary, adds new exercises to workout
    for area, num in focus_num.items():
        sample = random.sample(muscle_group[area], min(num, len(muscle_group[area])))
        Workout.extend(sample)
    
    # prints (or sends to another txt file) the proper, formatted list 
     
    wkout_list_idx = -1
    for exercise in Workout:
        print("\t" + exercise[0] + " -- " +  exercise[1] + " (" + exercise[2] + ")" + 
                " -- " + exercise[3] + ", " + exercise[4] + "\n")
	
    return Workout


def filter_exer(MuscleGroup, EQUIPMENT, EXPERIENCE):
    # Modifies the existing dictionary, replacing the existing
    print("Filtered Exercises:")
    for area, exercise_list in MuscleGroup.items():
        valid_exercises = []
        for exercise in exercise_list:
            if EXPERIENCE == "Advanced":
                if exercise[3] in EQUIPMENT:
                    print(exercise[0], "\n\t -- ", exercise[1], " -- ", exercise[3], " -- ", exercise[5])
                    valid_exercises.append(exercise)
            elif EXPERIENCE == "Intermediate":
                if (exercise[3] in EQUIPMENT) & (exercise[5] != "Advanced"):
                    print(exercise[0], "\n\t -- ", exercise[1], " -- ",exercise[3], " -- ", exercise[5])
                    valid_exercises.append(exercise)
            else:
                if (exercise[3] in EQUIPMENT) & (exercise[5] == "Beginner"):
                    print(exercise[0], "\n\t -- ", exercise[1], " -- ",exercise[3], " -- ", exercise[5])
                    valid_exercises.append(exercise)
        muscle_group[area] = valid_exercises
    print("\n\n")

#if __name__ == "__main__":
 #   main()
main()

