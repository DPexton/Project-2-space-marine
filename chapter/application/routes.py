from flask import Flask, Response, request
import random
from application import db

@app.route('/chapter', methods=['GET'])
def chapter():
    chapters = ["Space Wolves", "Ultramarines", "Imperial Fists", "Dark Angels"]
    chapter = chapters[random.randrange(0,4)]
    return Response(chapter)