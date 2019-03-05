#!/usr/bin/env python3
import os
import sys
import csv
import random

#Exercises = 30

Arms = []
Legs = []
Back = []
Abdominals = []
Cardio = []
Chest = []

def short_workout():
    #2 arms, 2 legs, 1 back, 1 chest
    sWorkout = []
    arm1 = random.choice(Arms)
    arm2 = random.choice(Arms)
    sWorkout.append(arm1)
    sWorkout.append(arm2)
    leg1 = random.choice(Legs)
    leg2 = random.choice(Legs)
    sWorkout.append(leg1)
    sWorkout.append(leg2)
    back1 = random.choice(Back)
    sWorkout.append(back1)
    chest1 = random.choice(Chest)
    sWorkout.append(chest1)
    print("Here is your SHORT workout (30 min):")
    print("\n Arm Exercises (2 randomly chosen):")
    print("[Exercise Name, Major Muscle Groups Used, Minor Muscle Groups, Equipment, Exercise Type]")
    print(sWorkout[0])
    print(sWorkout[1])
    print("\n Leg Exercises (2 randomly chosen):")
    print("[Exercise Name, Major Muscle Groups Used, Minor Muscle Groups, Equipment, Exercise Type]")
    print(sWorkout[2])
    print(sWorkout[3])
    print("\n Back Exercises (1 randomly chosen):")
    print("[Exercise Name, Major Muscle Groups Used, Minor Muscle Groups, Equipment, Exercise Type]")
    print(sWorkout[4])
    print("\n Chest Exercises (2 randomly chosen):")
    print("[Exercise Name, Major Muscle Groups Used, Minor Muscle Groups, Equipment, Exercise Type]")
    print(sWorkout[5])
    
def med_workout():
    #2 arms, 2 legs, 1 back, 1 chest, 3 abs
    mWorkout = []
    arm1 = random.choice(Arms)
    arm2 = random.choice(Arms)
    mWorkout.append(arm1)
    mWorkout.append(arm2)
    leg1 = random.choice(Legs)
    leg2 = random.choice(Legs)
    mWorkout.append(leg1)
    mWorkout.append(leg2)
    back1 = random.choice(Back)
    mWorkout.append(back1)
    chest1 = random.choice(Chest)
    mWorkout.append(chest1)
    ab1 = random.choice(Abdominals)
    ab2 = random.choice(Abdominals)
    ab3 = random.choice(Abdominals)
    mWorkout.append(ab1)
    mWorkout.append(ab2)
    mWorkout.append(ab3)
    print("Here is your MEDIUM workout (45 min):")
    print("\n Arm Exercises (2 randomly chosen):")
    print("[Exercise Name, Major Muscle Groups Used, Minor Muscle Groups, Equipment, Exercise Type]")
    print(mWorkout[0])
    print(mWorkout[1])
    print("\n Leg Exercises (2 randomly chosen):")
    print("[Exercise Name, Major Muscle Groups Used, Minor Muscle Groups, Equipment, Exercise Type]")
    print(mWorkout[2])
    print(mWorkout[3])
    print("\n Back Exercises (1 randomly chosen):")
    print("[Exercise Name, Major Muscle Groups Used, Minor Muscle Groups, Equipment, Exercise Type]")
    print(mWorkout[4])
    print("\n Chest Exercises (2 randomly chosen):")
    print("[Exercise Name, Major Muscle Groups Used, Minor Muscle Groups, Equipment, Exercise Type]")
    print(mWorkout[5])
    print("\n Abdominal Exercises (3 randomly chosen):")
    print("[Exercise Name, Major Muscle Groups Used, Minor Muscle Groups, Equipment, Exercise Type]")
    print(mWorkout[6])
    print(mWorkout[7])
    print(mWorkout[8])
    
    
def long_workout():
    #2 arms, 3 legs, 3 back, 1 chest, 3 abs
    lWorkout = []
    arm1 = random.choice(Arms)
    arm2 = random.choice(Arms)
    lWorkout.append(arm1)
    lWorkout.append(arm2)
    leg1 = random.choice(Legs)
    leg2 = random.choice(Legs)
    leg3 = random.choice(Legs)
    lWorkout.append(leg1)
    lWorkout.append(leg2)
    lWorkout.append(leg3)
    back1 = random.choice(Back)
    back2 = random.choice(Back)
    back3 = random.choice(Back)
    lWorkout.append(back1)
    lWorkout.append(back2)
    lWorkout.append(back3)
    chest1 = random.choice(Chest)
    lWorkout.append(chest1)
    ab1 = random.choice(Abdominals)
    ab2 = random.choice(Abdominals)
    ab3 = random.choice(Abdominals)
    lWorkout.append(ab1)
    lWorkout.append(ab2)
    lWorkout.append(ab3)
    print("Here is your LONG workout (60 min):")
    print("\n Arm Exercises (2 randomly chosen):")
    print("[Exercise Name, Major Muscle Groups Used, Minor Muscle Groups, Equipment, Exercise Type]")
    print(lWorkout[0])
    print(lWorkout[1])
    print("\n Leg Exercises (3 randomly chosen):")
    print("[Exercise Name, Major Muscle Groups Used, Minor Muscle Groups, Equipment, Exercise Type]")
    print(lWorkout[2])
    print(lWorkout[3])
    print(lWorkout[4])
    print("\n Back Exercises (3 randomly chosen):")
    print("[Exercise Name, Major Muscle Groups Used, Minor Muscle Groups, Equipment, Exercise Type]")
    print(lWorkout[5])
    print(lWorkout[6])
    print(lWorkout[7])
    print("\n Chest Exercises (1 randomly chosen):")
    print("[Exercise Name, Major Muscle Groups Used, Minor Muscle Groups, Equipment, Exercise Type]")
    print(lWorkout[8])
    print("\n Abdominal Exercises (3 randomly chosen):")
    print("[Exercise Name, Major Muscle Groups Used, Minor Muscle Groups, Equipment, Exercise Type]")
    print(lWorkout[9])
    print(lWorkout[10])
    print(lWorkout[11])

workolen = sys.argv[1]
with open('Exercises.csv', newline='') as myfile:
    reader = csv.reader(myfile)
    for row in reader:
        if ((row[1] == "Arms")):
            Arms.append(row)
        if ((row[1] == "Legs")):
            Legs.append(row)
        if ((row[1] == "Back")):
            Back.append(row)
        if ((row[1] == "Abdominals")):
            Abdominals.append(row)
        if ((row[1] == "Chest")):
            Chest.append(row)
    if workolen == "short":
        short_workout()
    if workolen == "medium":
        med_workout()
    if workolen == "long":
        long_workout()
myfile.close()
    
        
    
            
    

    
    
    
    
    
            
            
        
    
        
        
