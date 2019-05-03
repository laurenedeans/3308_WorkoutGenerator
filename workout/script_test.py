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

import unittest
import WorkoutScript_ds


#import Excercises.csv

class WorkoutTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass


# Test cases:
    
    # Case 1: Person wants a random arm exercise
    # Input: 1 arm exercise
    test_list = WorkoutScript_ds.make_workout(1,0,0,0,0)
#    print("A selection of a short workout returned: ")
    test_len = len(test_list)
    if test_len == 1:
        print("Case 1 PASSED! One exercise has 1 line!")
    else:
        print("Case 1 FAILED. Produced too many lines.")

    # Case 2: Person wants a short workout
    # Input: "short" as an argument
    # short workouts = 2,2,1,1,0
    test2_list = WorkoutScript_ds.start_wkout("short")
    test_len = len(test2_list)
    if test_len == 6:
        print("Case 2 PASSED! The short workout has correct # of lines!")
    else:
        print("Case 2 FAILED. The short workout did not produce right # of lines.")


    # Case 3: Does the program produce different workouts?
    # Input: 2 different "medium" workouts
    # method: compare same lines in both documents.
    # medium workouts = 2,2,1,1,3
    diffTest_1 = WorkoutScript_ds.start_wkout("medium")
    
    diffTest_2 = WorkoutScript_ds.start_wkout("medium")

    if diffTest_1 == diffTest_2:
        print("Case 3 FAILED. All lines matched. Workouts are identical.")
    else:
        print("Case 3 PASSED! Workouts are different.")



# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()
