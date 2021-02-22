from flask import Flask, request, Request, jsonify

app = Flask(__name__)


@app.route("/fkassan", methods=["post"])
def fkassan():
    pbb = 47600
    tak = pbb*8
    data = request.args
    salary = int(data.get("salary"))
    yearsalary = salary*12
    if yearsalary > tak:
        compensation = int((tak *0.97)*0.8/365)*30
    else:
        compensation = int((yearsalary * 0.97) * 0.8 / 365) * 30
    return jsonify(compensation)

@app.route("/itppension")
def itppension():
    return "null"

@app.route("/salaryexchange")
def salaryexchange():
    return "null"

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(threaded=True, port=5000)
