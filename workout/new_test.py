#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Thanks to Andy Sayler for format
# Bret L. Murray
#
#
#
# CSCI 3308
# Spring 2019 Semester Project Group 2
# Tests for original script

import argparse
import os
import sys
import numpy as np
import csv
import unittest
import WorkoutScript_ds
from collections import OrderedDict


#import Excercises.csv

class WorkoutTestCase(unittest.TestCase):

    def test_one_wkout(self):
        db = WorkoutScript_ds.load_exercise_db()
        num_of_ex = WorkoutScript_ds.make_workout(db,1,0,0,0,0)
        test = 1 
        self.assertEqual(len(num_of_ex),test)


    def test_arms_wkout(self):
        db = WorkoutScript_ds.load_exercise_db()
        arms = WorkoutScript_ds.make_workout(db,12,0,0,0,0)
        all_arms = 0
        for part in arms:
            if "Arms" not in part:
                all_arms = all_arms + 1
        self.assertEqual(all_arms,0)

    def test_legs_wkout(self):
        db = WorkoutScript_ds.load_exercise_db()
        legs = WorkoutScript_ds.make_workout(db,0,7,0,0,0)
        all_legs = 0
        for part in legs:
            if "Legs" not in part:
                all_legs = all_legs + 1
        self.assertEqual(all_legs,0)

    def test_back_wkout(self):
        db = WorkoutScript_ds.load_exercise_db()
        back = WorkoutScript_ds.make_workout(db,0,0,5,0,0)
        all_back = 0
        for part in back:
            if "Back" not in part:
                all_back = all_back + 1
        self.assertEqual(all_back,0)

    def test_distribute_shortwkout(self):
        muscle_group = {
            'Arms': [],
            'Legs': [],
            'Back': [],
            'Abdominals': [],
            'Cardio': [],
            'Chest': [],
        }
        with open('Exercises.csv','r') as f:
            csv_f = csv.reader(f)
            for row in csv_f:
                muscle_group.get(row[1], []).append(row)

        length_map = {
                'short': 6,
                'medium': 9,
                'long': 12,
                }
        workout_length = length_map['short']
        test_array_short = np.array([1,0,1,1,0])  
        test_val_short = WorkoutScript_ds.distribute_exercise(workout_length,test_array_short)
        short = 6
        self.assertEqual(short,sum(test_val_short))


    def test_distribute_medwkout(self):
        muscle_group = {
                'Arms': [],
                'Legs': [],
                'Back': [],
                'Abdominals': [],
                'Cardio': [],
                'Chest': [],
                }
        with open('Exercises.csv','r') as f:
            csv_f = csv.reader(f)
            for row in csv_f:
                muscle_group.get(row[1], []).append(row)

        length_map = {
                'short': 6,
                'medium': 9,
                'long': 12,
                }
        workout_length = length_map['medium']
        test_array = np.array([1,0,1,1,0])
        test_val = WorkoutScript_ds.distribute_exercise(workout_length,test_array)
        self.assertEqual(workout_length,sum(test_val))


    def test_distribute_longwkout(self):
        muscle_group = {
                'Arms': [],
                'Legs': [],
                'Back': [],
                'Abdominals': [],
                'Cardio': [],
                'Chest': [],
                }
        with open('Exercises.csv','r') as f:
            csv_f = csv.reader(f)
            for row in csv_f:
                muscle_group.get(row[1], []).append(row)

        length_map = {
                'short': 6,
                'medium': 9,
                'long': 12,
                }
        workout_length = length_map['long']
        test_array = np.array([1,0,1,1,0])
        test_val = WorkoutScript_ds.distribute_exercise(workout_length,test_array)
        self.assertEqual(workout_length,sum(test_val))



if __name__ == '__main__':
    unittest.main()
