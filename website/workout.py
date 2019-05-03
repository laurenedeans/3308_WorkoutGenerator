from flask import Flask, render_template, request
import numpy as np
import WorkoutScript_ds as wds

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    return render_template('workoutpage.html', workout_text='')

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        focus = [str(i) for i in request.form.getlist('focus')]
        equip = [str(i) for i in request.form.getlist('equip')] + ["Body Weight"]
        length = request.form['length']
        experience = request.form['level']

        target_area = wds.target_areas(focus)
        db = wds.load_exercise_db()
        wds.filter_exer(db, equip, experience)
        workout_dist = wds.distribute_exercise(wds.length(length), np.array(target_area))
        workout_list = wds.make_workout(db, *workout_dist)

        workout_str = format_workout(workout_list)

        return render_template('workoutpage.html', workout_text=workout_str)

def format_workout(workout_list):
    header = f"Do 12 reps of each of the following exercises. <br> "
    header = header + "Repeat circuit for a total of 3 times. <br><br> "
    names = [i[0] for i in workout_list]
    return header + '<br>'.join(names)



if __name__ == "__main__":
    app.run()
