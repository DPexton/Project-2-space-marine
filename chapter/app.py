from flask import Flask 
import random

app = Flask(__name__)

@app.route('/chapter', methods=['GET'])
def chapter():
    chapters = ["Space Wolves", "Ultramarines", "Imperial Fists", "Dark Angels", "Salamanders", "Blood Angels"]
    chapter = random.choice(chapters)
    return chapter

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port= 5000)