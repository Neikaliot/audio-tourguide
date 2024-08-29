from flask import Flask, render_template, url_for, redirect

from dataLayer import main_menu
from dataLayer import human

app = Flask(__name__)

@app.route("/")
def home():

    menu = main_menu.main_menu()

    return render_template("index.html", menu=menu)

@app.route("/people")
def people():
    menu = main_menu.main_menu()

    return render_template("people.html", menu=menu)

@app.route("/tayho")
def tayho():
    menu = main_menu.main_menu()

    return render_template("tayho.html", menu=menu)

@app.route("/dongda")
def dongda():
    menu = main_menu.main_menu()

    return render_template("dongda.html", menu=menu)

@app.route("/hoankiem")
def hoankiem():
    menu = main_menu.main_menu()

    return render_template("hoankiem.html", menu=menu)

@app.route("/history")
def history():
    menu = main_menu.main_menu()

    return render_template("history.html", menu=menu)
@app.route("/about")
def about():
    menu = main_menu.main_menu()

    people = human.people_list()

    return render_template("about.html", menu=menu)

@app.route("/tayhofood")
def tayhofood():
    menu = main_menu.main_menu()
    return render_template("tayhofood.html", menu=menu)

@app.route("/tayhoattractions")
def tayhoattractions():
    menu = main_menu.main_menu()
    return render_template("tayhoattractions.html", menu=menu)
@app.route("/hoankiemfood")
def hoankiemfood():
    menu = main_menu.main_menu()
    return render_template("hoankiemfood.html", menu=menu)

@app.route("/hoankiemattractions")
def hoankiemattractions():
    menu = main_menu.main_menu()
    return render_template("hoankiemattractions.html", menu=menu)
@app.route("/dongdafood")
def dongdafood():
    menu = main_menu.main_menu()
    return render_template("dongdafood.html", menu=menu)

@app.route("/dongdaattractions")
def dongdaattractions():
    menu = main_menu.main_menu()
    return render_template("dongdaattractions.html", menu=menu)

@app.route("/districts")
def districts():
    menu = main_menu.main_menu()
    return render_template("districts.html", menu=menu)



@app.route('/redirect/<page_name>')
def redirect_to_page(page_name):
    if page_name == 'person1':
        return redirect('https://www.facebook.com/profile.php?id=100021898362437')
    elif page_name == 'person2':
        return redirect('https://www.facebook.com/HaiAnhnice')
    elif page_name == 'person3':
        return redirect('https://www.facebook.com/profile.php?id=100025569999947')
    elif page_name == 'person4':
        return redirect('https://www.facebook.com/khanh.quan.73550')
    elif page_name == 'person5':
        return redirect('https://www.facebook.com/ntmp.6867')
    elif page_name == 'person6':
        return redirect('https://www.facebook.com/tue.nguyenlam.10')
    # Add more conditions as needed
    else:
        return redirect(url_for('home'))

if __name__=="__main__":
    app.run(debug=True)

