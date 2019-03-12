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
        print("\nUsage: ./WorkoutScript_ds.py WORKOUT_LENGTH")
        print(" -- WORKOUT_LENGTH = short (30min), medium (45min), long (60min)\n")
    else:
        length = sys.argv[1]
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



#if __name__ == "__main__":
 #   main()
main()

