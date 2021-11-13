from flask import Flask, render_template, request
from helpers import find_house

app: Flask = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/quiz', methods=["GET", "POST"])
def quiz():
    if request.method == "POST":

        fname: str = request.form['fname']
        lname: str = request.form['lname']
        animal: str = request.form['animal']

        if fname == '' or lname == '':
            return render_template("quiz.html")

        house: str = find_house(animal)

        return render_template("result.html", house=house)
    return render_template("quiz.html")