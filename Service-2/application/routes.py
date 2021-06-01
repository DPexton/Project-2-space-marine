from flask import Flask, Response, request
import random
from application import app

@app.route('/role', methods=['GET'])
def role():
    roles = ["Tactical Marine", "Assault Marine", "Devastator Marine", "Scout Marine"]
    role = roles[random.randrange(0,4)]

    return Response(role)