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
import sys
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
    
    # Case: Person wants arm and leg workout
    # Input: 2 arms, 2 legs, 0 back, 0 chest, 0 abs
    retValue = () 
    retValue = WorkoutScript_ds.start_wkout("short")
    print("2 arm and 2 leg workout returned: ")
    print(retValue)







# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()
