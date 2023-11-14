from statistics import mean

FOLDER = "swimdata/"

def convert2hundreths(timestring):

    """Given function convert given string to int using split() and int() methods"""
    if ":" in timestring:
        mins, rest = timestring.split(":")
        secs, hundreths = rest.split(".")
    else:
        mins = 0
        secs, hundreths = timestring.split(".")
    return int(hundreths) + (int(secs) * 100) + (int(mins) * 60 * 100)

def build_time_string(num_time):
    secs, hundreths = f"{(num_time / 100):.2f}".split(".")
    mins = int(secs) // 60
    seconds = int(secs) - mins*60
    return f"{mins}:{seconds}.{hundreths}"

def get_swimmers_data(filename):
    name, age, distance, stroke = filename.removesuffix(".txt").split("-")

    with open(FOLDER + filename) as fh:
        data = fh.read()
    times = data.strip().split(",")
    convert = []
    for t in times:
        convert.append(convert2hundreths(t))
    average = build_time_string(mean(convert))

    return name, age, distance, stroke, times, convert, average
