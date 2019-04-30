#!/usr/bin/env python3
import argparse
import os
import sys
import csv
import random
import numpy as np
from collections import OrderedDict

muscle_group = { 
    'Arms': [],
    'Legs': [],
    'Back': [],
    'Abdominals': [],
    'Cardio': [],
    'Chest': [],
    }

# group exercises by muscle group
with open('Exercises.csv', 'r') as f:
    csv_f = csv.reader(f)
    for row in csv_f:
        muscle_group.get(row[1], []).append(row)

# Calling w/ 1 arg: ./WorkoutScript_ds.py
# main function catches any errors in calling on program.
def main():
    areas = 'Arms,Legs,Chest,Back,Abdominals'.split(',')
    equipment = 'Dumbells, Bar, Machine, Body Weight, Medicine Ball, Jump rope, Pool, Bicycle'
    parser = argparse.ArgumentParser(description='Workout generator')
    parser.add_argument('-L', '--WORKOUT_LENGTH',
            choices=['short', 'medium', 'long'],
            required=True,
            help='Lenght of workout: short (30min - 6 exercises), medium (45min - 9 exercises), long (60min - 12 exercises)',
            )
    parser.add_argument('-E', '--EXPERIENCE',
            choices=['Beginner', 'Intermediate', 'Advanced'],
            required=True,
            help='User experience level',
            )
    parser.add_argument('-A', '--TARGET_AREA',
            nargs='*', # All input args are gathered into a list
            help=f'Target areas: {areas}',
            )
    parser.add_argument('-G', '--GOAL',
            choices=['Mass', 'Strength', 'Endurance'],
            required=True,
            help='Workout target areas',
            )
    parser.add_argument('-Q', '--EQUIPMENT',
            required=True,
            nargs='*', # All input args are gathered into a list
            help=f'List of equipment user has access to: {equipment}',
            )
    args = parser.parse_args()


    length_map = {
        'short': 6,
        'medium': 9,
        'long': 12,
        }
    WORKOUT_LENGTH = length_map[args.WORKOUT_LENGTH]

    TARGET_AREA = [1 if area in args.TARGET_AREA else 0 for area in areas]
    EXPERIENCE = args.EXPERIENCE
    GOAL = args.GOAL
    EQUIPMENT = ["Body Weight"] + args.EQUIPMENT

    filter_exer(muscle_group, EQUIPMENT, EXPERIENCE)  # filters existing dictionary to only contain valid exercises
    workout_dist = distribute_exercise(WORKOUT_LENGTH, np.array(TARGET_AREA)) # returns np.array that gives number of exercises for each muscle group
    print(workout_dist)
    make_workout(*workout_dist)


def distribute_exercise(len_choice, target_choice):

    ret = target_choice * len_choice
    bound = len_choice / sum(target_choice) - 1

    # Put some bounds on the distribution
    # Don't allow large numbers, large differences between min/max, or zeros where they shouldn't be
    too_large = ret > (len_choice - bound)
    zeroed = np.logical_xor(target_choice, ret)
    big_diffs = (np.max(ret[ret>0]) - np.min(ret[ret>0])) > bound + 1
    one_target_area = sum(target_choice) == 1

    # Pull from a random multinomial distribution until conditions are met
    while (not one_target_area and any(too_large)) or any(zeroed) or big_diffs:
        ret = np.random.multinomial(len_choice, target_choice/sum(target_choice))
        too_large = ret > (len_choice - bound)
        zeroed = np.logical_xor(target_choice, ret)
        big_diffs = (np.max(ret[ret>0]) - np.min(ret[ret>0])) >= bound + 1
    return ret



def make_workout(arm_no, leg_no, back_no, chest_no, abs_no):
    #  -- Input: predefined_set (from distribute_exercise())
    #  -- Output: List in the form [sets, reps, weight, exercise_list]
    
    Workout = []

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
    #print("Filtered Exercises:")
    for area, exercise_list in MuscleGroup.items():
        valid_exercises = []
        for exercise in exercise_list:
            if EXPERIENCE == "Advanced":
                if (exercise[3] in EQUIPMENT):
                    #print(exercise[0], "\n\t -- ", exercise[1], " -- ", exercise[3], " -- ", exercise[5])
                    valid_exercises.append(exercise)
            elif EXPERIENCE == "Intermediate":
                if (exercise[3] in EQUIPMENT) & (exercise[5] != "Advanced"):
                    #print(exercise[0], "\n\t -- ", exercise[1], " -- ",exercise[3], " -- ", exercise[5])
                    valid_exercises.append(exercise)
            else:
                if (exercise[3] in EQUIPMENT) & (exercise[5] == "Beginner"):
                    #print(exercise[0], "\n\t -- ", exercise[1], " -- ",exercise[3], " -- ", exercise[5])
                    valid_exercises.append(exercise)
        muscle_group[area] = valid_exercises
    #print("\n\n")

#if __name__ == "__main__":
 #   main()
main()

