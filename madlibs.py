from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return "Hi! This is the home page."

# route to display a simple web page
@app.route('/hello')
def say_hello():
    return render_template("hello.html")

@app.route('/greet')
def greet_person():
    player = request.args.get("person")

    AWESOMENESS = [
        'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
        'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)

@app.route("/game")
def show_game_form():
    response = request.args.get("decison")
    if response == "yes":
        return render_template("game.html")
    else:
        return render_template("goodbye.html")

    pass
@app.route("/madlib", methods=["POST", "GET"])
def show_madlib():
    print request.method
    if request.method == "post":  
        the_car = request.form.getlist("car")
        the_weather = request.form.get("weather")
        the_mood = request.form.get("mood")
        the_person = request.form.get("person")
        the_color = request.form.get("color")
        the_noun = request.form.get("noun")
        the_adjective = request.form.get("adjective")
    else:
        the_car = request.args.getlist("car")
        the_weather = request.args.get("weather")
        the_mood = request.args.get("mood")
        the_person = request.args.get("person")
        the_color = request.args.get("color")
        the_noun = request.args.get("noun")
        the_adjective = request.args.get("adjective")

    return render_template(
    "madlib.html", person=the_person, color=the_color, 
    noun=the_noun, adjective=the_adjective, weather=the_weather, 
    mood=the_mood, car=the_car)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
