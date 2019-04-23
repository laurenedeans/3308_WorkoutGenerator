#!/usr/bin/env python3
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
    if len(sys.argv)==1:    # Usage statement to show how to call the script (type "./WorkoutScript_ds.py")
        print("\nUsage: ./WorkoutScript_ds.py WORKOUT_LENGTH TARGET_AREA EXPERIENCE GOAL EQUIPMENT")
        print(" -- WORKOUT_LENGTH = short (30min - 6 exercises), medium (45min - 9 exercises), long (60min - 12 exercises)")  # sys.argv[1]
        print(" -- TARGET_AREA = Arms, Legs, Chest, Back, Abdominals, NONE")  # sys.argv[2]
        print(" -- EXPERIENCE = Beginner, Intermediate, Advanced")  # sys.argv[3]
        print(" -- GOAL = Mass, Strength, Endurance")  # sys.argv[4]  (Sets & Reps & Weight choices)
        print(" -- EQUIPMENT = Dumbells, Bar, Machine, Body Weight, Medicine Ball, Jump rope, Pool, Bicycle, ANY, NONE\n")  # sys.argv[5] ....
        # bicep curls "bar, dumbell, kettlebell" --> EQUIPMENT "bar, dumbell" --> bicep curls "bar, dumbell" 
    else:
        # Command line arguments
        if (sys.argv[1] == "short"):
            WORKOUT_LENGTH = 6
        elif (sys.argv[1] == "medium"):
            WORKOUT_LENGTH = 9
        else:
            WORKOUT_LENGTH = 12
        TARGET_AREA = (1,0,1,0,1)
        EXPERIENCE = sys.argv[3]
        GOAL = sys.argv[4]
        argc = len(sys.argv)
        EQUIPMENT = ["Body Weight"]
        for i in range(5,argc):                           # appends list of equipment options from command line input
            EQUIPMENT.append(sys.argv[i])
        filter_exer(muscle_group, EQUIPMENT, EXPERIENCE)  # filters existing dictionary to only contain valid exercises
        workout_dist = distribute_exercise(WORKOUT_LENGTH, np.array(TARGET_AREA)) # returns np.array that gives number of exercises for each muscle group                            
        print(workout_dist)
        make_workout(workout_dist[0], workout_dist[1], workout_dist[2], workout_dist[3], workout_dist[4]) # pulls exercises from exercise dictionary
        

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

