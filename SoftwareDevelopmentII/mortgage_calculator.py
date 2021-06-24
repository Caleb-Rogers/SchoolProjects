from flask import Flask
from flask.globals import request
app = Flask(__name__)


@app.route("/calculate-mortgage")
def calculate_mortgage():
    homeValue = request.args.get("homevalue")
    downPayment = request.args.get("downpayment")
    lengthLoan = request.args.get("lengthloan")
    interestRate = request.args.get("interestrate")

    print("Home Value: ", homeValue)
    print("Down Payment: ", downPayment)
    print("Length Loan: ", lengthLoan)
    print("Interest Loan: ", interestRate)

    homeValue = float(homeValue)
    downPayment = float(downPayment)
    lengthLoan = float(lengthLoan)
    interestRate = float(interestRate)

    monthlyRate = (interestRate/100) / 12
    loanAmount = homeValue - downPayment

    monthlyPayment = (loanAmount*monthlyRate)/(1-(1/(pow((1+monthlyRate), (lengthLoan*12)))))

    result = "Monthly Mortgage Payment will be ${:,.2f}".format(monthlyPayment)
    return result


if __name__ == "__main__":
    app.run()
