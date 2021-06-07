from flask import Flask, Response, request




app = Flask(__name__)

@app.route('/name', methods=['GET','POST'])
def name():
    
    
    chapter,role = request.data.decode().split(',')
    
    #raise ValueError((role,chapter))
    if chapter == "Space Wolves":
        if role == "Tactical Marine":
            name = "Grimolf Ulfsson"
        elif role == "Assault Marine":
            name = "Ragnar Blackmane"
        elif role == "Devastator Marine":
            name = "Gunbjorn Ironmaw"
        elif role == "Scout Marine":
            name = "One-Eye Frodi"
        elif role == "Terminator Marine":
            name = "Tyreous Hengun"
    
    elif chapter == "Ultramarines":
        if role == "Tactical Marine":
            name = "Titus Grimaldus"
        elif role == "Assault Marine":
            name = "Maximus Tarimus"
        elif role == "Devastator Marine":
            name = "Jonah Sidonis"
        elif role == "Scout Marine":
            name = "Barachiel Sadros"
        elif role == "Terminator Marine":
            name = "Aecon Evidist"
    
    elif chapter == "Imperial Fists":
        if role == "Tactical Marine":
            name = "Shal Cestros"
        elif role == "Assault Marine":
            name = "Uziel Aryabhon"
        elif role == "Devastator Marine":
            name = "Klordath Aglibesco"
        elif role == "Scout Marine":
            name = "Kazryn Batariar"
        elif role == "Terminator Marine":
            name = "Kazrago Hannibia"
    
    
    elif chapter == "Dark Angels":
        if role == "Tactical Marine":
            name = "Baelar Sadross"
        elif role == "Assault Marine":
            name = "Gabriel Manuzanus"
        elif role == "Devastator Marine":
            name = "Lutheon Alcane"
        elif role == "Scout Marine":
            name = "Cassias Gabrun"
        elif role == "Terminator Marine":
            name = "Anaticus Redlici"

    elif chapter == "Salamanders":
        if role == "Tactical Marine":
            name = "Belial Iasiar"
        elif role == "Assault Marine":
            name = "Varreon Baaloss"
        elif role == "Devastator Marine":
            name = "Sappheran Petrail"
        elif role == "Scout Marine":
            name = "Ophaniel Salatis"
        elif role == "Terminator Marine":
            name = "Maximiz Zephit"  
        
    elif chapter == "Blood Angels":
        if role == "Tactical Marine":
            name = "Beler Antilochiad"
        elif role == "Assault Marine":
            name = "Azazel Annellurius"
        elif role == "Devastator Marine":
            name = "Ubaldun Chronal"
        elif role == "Scout Marine":
            name = "Azreal Berian"
        elif role == "Terminator Marine":
            name = "Sarathiel Asbeo"  
    
    else: 
        return "Please Press Again"

    return name
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port= 5000)