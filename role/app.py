from flask import Flask

app = Flask(__name__)

@app.route('/role', methods=['GET'])
def role():
    roles = ["Tactical Marine", "Assault Marine", "Devastator Marine", "Scout Marine"]
    role = roles[random.randrange(0,4)]

    return Response(role)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port= 5000)