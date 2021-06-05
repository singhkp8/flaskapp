from flask import Flask, jsonify, request


app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'contact': '9922334455',
        'name': 'raju',
        'done': False
    },
    {
        'id': 2,
        'contact': '1122334455',
        'name': 'rahul',
        'done': False
    }
]


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide the data!"
        }, 400)

    contact = {
        'id': contact[-1]['id'] + 1,
        'contact': request.json['contact'],
        'name': request.json.get('name', ""),
        'done': False
    }
    tasks.append(contact)
    return jsonify({
        "status": "success",
        "message": "contact added succesfully!"
    })


@app.route("/get-data")
def get_task():
    return jsonify({
        "data": tasks
    })


if (__name__ == "__main__"):
    app.run(debug=True)
