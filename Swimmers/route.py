from Swimmers import app
from flask import render_template, request
import os
from Swimmers.swim_utils import get_swimmers_data

FOLDER = 'swimdata'
files = os.listdir(FOLDER)


names = set()
for file in files:
    data = []
    data = get_swimmers_data(file)
    names.add(data[0])



@app.route('/')
def name_page():
    return render_template('Names.html', names = names)

@app.route('/event', methods=['GET', 'POST'])
def event_name():
    
    data = []
    events = set()
    if request.method == 'POST':
        selected_name = request.form.get("name")
        
        for file in files:
            data = get_swimmers_data(file)
            if selected_name in data[0]:
                events.add(data[1] + " " +data[2] + " " + data[3])

    return render_template('Events.html', events = events)