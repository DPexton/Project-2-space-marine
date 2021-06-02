from flask import Flask

app = Flask(__name__)

@app.route('/name', methods=['GET','POST'])
def name():

    info = request.data.decode('utf-8')
    data = info.split(" ")
    role = data[0]
    team = data[1]

    if chapter == "Space Wolves":
        if role == "Tactical Marine":
            name =="Grimolf Ulfsson"
        elif role == "Assault Marine":
            name =="Ragnar Blackmane"
        elif role == "Devastator Marine":
            name == "Gunbjorn Ironmaw"
        elif role == "Scout Marine":
            name == "One-Eye Frodi"
    
    elif chapter == "Ultramarines":
        if role == "Tactical Marine"
            name =="Titus Grimaldus"
        elif role == "Assault Marine":
            name =="Maximus Tarimus"
        elif role == "Devastator Marine":
            name == "Jonah Sidonis"
        elif role == "Scout Marine":
            name == "Barachiel Sadros"
    
    elif chapter == "Imperial Fists":
            if role == "Tactical Marine":
            name =="Shal Cestros"
        elif role == "Assault Marine":
            name =="Uziel Aryabhon"
        elif role == "Devastator Marine":
            name == "Klordath Aglibesco"
        elif role == "Scout Marine":
            name == "Kazryn Batariar"
    
    elif chapter == "Dark Angels":
            if role == "Tactical Marine":
            name =="Baelar Sadross"
        elif role == "Assault Marine":
            name =="Gabriel Manuzanus"
        elif role == "Devastator Marine":
            name == "Lutheon Alcane"
        elif role == "Scout Marine":
            name == "Cassias Gabrun"
    
    else: 
        return "Please Press Again"

    return Response(name)
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port= 5000)