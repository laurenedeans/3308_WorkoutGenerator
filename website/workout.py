from flask import Flask, render_template, request
import numpy as np
import WorkoutScript_ds as wds

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    return render_template('workoutpage.html')

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

        return render_template('greeting.html', focus=workout_list)

if __name__ == "__main__":
    app.run()
