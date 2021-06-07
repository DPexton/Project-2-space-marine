from flask import Flask, Response, request
import random

app = Flask(__name__)

@app.route('/role', methods=['GET'])
def role():
    roles = ["Tactical Marine", "Assault Marine", "Devastator Marine", "Scout Marine", "Terminator Marine"]
    role = random.choice(roles)

    return role


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port= 5000)