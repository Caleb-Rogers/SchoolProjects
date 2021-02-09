from flask import Flask
from flask.globals import request
app = Flask(__name__)


@app.route('/poll-question', methods=['GET', 'POST'])
def poll_question():
    choice = request.form.get('preference')

    print("Do you enjoy pineapple on pizza?")
    if choice == "yes":
        print("You chose YES, you love it!")
        selection = "You chose YES, you love pineapple on pizza!"
    elif choice == "no":
        print("You chose NO, you hate it!")
        selection = "You chose NO, you hate pineapple on pizza!"
    elif choice == "other":
        print("You chose OTHER, you could take it or leave it.")
        selection = "You chose OTHER, you could take or leave pineapple on pizza"
    else:
        selection = "Uh oh, couldn't find your answer."

    return selection


if __name__ == "__main__":
    app.run()
