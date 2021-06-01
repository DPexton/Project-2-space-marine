@app.route('/', methods=['GET', 'POST'])
def index():

    chapter = requests.get("http://service-2:5001/chapter")

    role = requests.get("http://service-3:5002/role")

    name = requests.post("http://service-4:5003/name", data=result)
    result = str(chapter.text) + " " + str(role.text)

    return render_template(
        'layout.html', 
        title= 'Home', 
        role=role.txt, 
        chapter=chapter.txt, 
        result=result, 
        name=name.text
        )