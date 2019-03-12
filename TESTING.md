# Project Title:

<<<<<<< HEAD
# Use case name
Fill out form.

# Description
User can fill out form to receive an explanation of the backend work to be done.

# Pre-conditions
Load the website/workoutpage.html file into a browser. No selections have been made.

# Test steps (numbered)
1. Click one or more focus area preferences.
2. Click any relevant gym equipment items you have available.
3. Choose a workout length from the drop down box.
4. Choose an experience level from the drop down menu.
5. Click submit.

# Expected Result
An alert box will pop up with an explanation of what will be returned from the backend. It should say:

This page says
You will get a(n) [length] [level] workout for your: [focus areas selected]
Using the following equipment: [equipment selected]

Clicking "OK" should close the alert box.
=======
Customized Workout Generator

# Team

Lauren Deans, Derek Sessions, Christina Holt, Bret Murray

# Automated Test Cases

To run the automated test cases, type the following onto the command line:
>>>>>>> 5dd534953a200f05b0af17b6675ecf7c00302a13

				python script_test.py

# User Acceptance Testing

## CASE 1:

### Use case name
Web Form

### Description
User can fill out form to receive an explanation of the backend work to be done.

### Pre-conditions
Load the website/workoutpage.html file into a browser. No selections have been made.

### Test steps (numbered)
1. Click one or more focus area preferences.
2. Click any relevant gym equipment items you have available.
3. Choose a workout length from the drop down box.
4. Choose an experience level from the drop down menu.
5. Click submit.

### Expected Result
An alert box will pop up with an explanation of what will be returned from the backend. It should say:

This page says
You will get a(n) [length] [level] workout for your: [focus areas selected]
Using the following equipment: [equipment selected]

Clicking "OK" should close the alert box.

### Actual Result

### Status

### Notes

### Post-conditions

Form is reset.

---

## CASE 2:
...
### Use case name
Usage message.

### Description
Running the script Workout\_ps.py with no command line options to determine what the command line usage is.

### Pre-conditions
The user should have Python version 3 installed.

### Test steps (numbered)
1. Move into the top level of the repository clone.
2. Run the script by typing:
       `python Workflow_ds.py`

### Expected Result
The following usage statement will be written to the screen:

```
Usage: ./WorkoutScript_ds.py WORKOUT_LENGTH
 -- WORKOUT_LENGTH = short (30min), medium (45min), long (60min)
```

### Actual Result

### Status

### Notes

### Post-conditions.

---


## CASE 3:


### Use case name
Generate Workout

### Description
Run the script Workout\_ds.py to get a list of exercises. This list is randomized. Each time the test is performed, a
new list should be generated.

### Pre-conditions
The user should have Python version 3 installed.

### Test steps (numbered)
1. Move into the top level of the repository clone.
2. Run the script by typing:
       `python Workflow_ds.py medium`

### Expected Result
A list of exercises is printed to the screen. This list is a mix of exercises that is randomly selected, and masterfully
combined to give the appropriate mix to the focus areas during the workout. In other words, there should be a mix of
arms, legs, back, abdominals, and chest. The number chosen from each category varies with length of workout.

The format of the output should look like the following:

```
	Shoulder Press -- Arms (Deltoids) -- Machine, Resistance Training

	Tricep Extensions -- Arms (Triceps) -- Dumbells, Resistance Training

	Leg Extension -- Legs (Quadriceps) -- Machine, Resistance Training

	Dead-Lift -- Legs (Quadriceps, Glutes, Hamstrings) -- Bar, Resistance Training

	Seated Row -- Back (Latissimus Dorsi, Biceps, Triceps) -- Machine, Resistance Training

	V-ups -- Abdominals (Hip Flexors) -- Body Weight, Abs
```

### Actual Result

### Status

### Notes

### Post-conditions

<<<<<<< HEAD
# Post-conditions.
Form is reset.
=======
>>>>>>> 5dd534953a200f05b0af17b6675ecf7c00302a13
