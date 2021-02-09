from flask import Flask, render_template
from flask.globals import request

app = Flask(__name__)


@app.route('/nbaFlask', methods=['GET', 'POST'])
def poll_question():
    teams = []
    for key, value in request.values.items():
        teams.append(value)

    return render_template('checklist-template.html', result=teams)


if __name__ == "__main__":
    app.run()
