import csv
import random
from flask import Flask, render_template
app = Flask(__name__)

#code to read a csv and convert into dictionary 
OCCUPATIONS = {}
with open('./static/occupations.csv') as csv_file:  # open CSV file
    # instantiate CSV reader object
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0  # make sure header isn't included in dictionary
    for row in csv_reader:  # populate dictionary with keys and values
        if(line_count == 0):
            line_count += 1
        else:
            OCCUPATIONS[row[0]] = float(row[1])


def selector():  # function to randomly select an occupation
    randomValue = random.random() * 99.8  # Pick a random number from 0 to 99.8
    threshold = 0  # establish a counter
    for x, y in OCCUPATIONS.items():  # for every entry in the dictionary (key, value)
        if(randomValue < threshold):  # if the random number is less than the threshold
            return(x, y)  # return that entry
        else:
            threshold += y  # otherwise add this value to the threshold

@app.route("/")
def hello_world():
    print(__name__)
    return "no hablo queso!"


@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/occupyflaskst")  # route traffic to http://localhost:5000/occupyflaskst
def test_tmplt():
    selected = selector()  # select a weighted random occupation

    # Render the template with the entire ictionary to be printed, and the chosen value
    return render_template("index.html", OCCUPATIONS=OCCUPATIONS, selected=selected)

if __name__ == "__main__":
    app.debug = True
    app.run()
