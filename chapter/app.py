from flask import Flask 

app = Flask(__name__)

@app.route('/chapter', methods=['GET'])
def chapter():
    chapters = ["Space Wolves", "Ultramarines", "Imperial Fists", "Dark Angels"]
    chapter = chapters[random.randrange(0,4)]
    return Response(chapter)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port= 5000)