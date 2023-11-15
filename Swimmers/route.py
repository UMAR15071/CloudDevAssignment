from Swimmers import app
from flask import render_template, request, session
import os
from Swimmers.swim_utils import get_swimmers_data
from Swimmers.hfpy_utils import convert2range

FOLDER = "swimdata"
files = os.listdir(FOLDER)


names = set()
for file in files:
    data = []
    data = get_swimmers_data(file)
    names.add(data[0])


@app.route("/")
def name_page():
    return render_template("Names.html", names=names)


@app.route("/event", methods=["GET", "POST"])
def event_name():
    data = []
    events = set()
    if request.method == "POST":
        selected_name = request.form.get("name")
        session["selected_name"] = selected_name

        for file in files:
            data = get_swimmers_data(file)
            if selected_name in data[0]:
                events.add(data[1] + " " + data[2] + " " + data[3])

    return render_template("Events.html", events=events)


@app.route("/show_graphs", methods=["GET", "POST"])
def show_graphs():
    selected_name = session.get("selected_name")

    if request.method == "POST":
        swimmer = (selected_name + " " + request.form.get("event")).strip().split(" ")
        name, age, distance, stroke = swimmer
        filename = f"{name}-{age}-{distance}-{stroke}.txt"
        data = get_swimmers_data(filename)
        name, age, distance, stroke, times, values, average = data

        title = f"{name} (Under {age}) - {distance} - {stroke}"

        converts = []
        for n in values:
            converts.append(convert2range(n, 0, max(values) + 50, 0, 400))

        times.reverse()
        converts.reverse()
        tc = zip(times, converts)

    return render_template("Graphs.html", title=title, tc=tc, average=average)
