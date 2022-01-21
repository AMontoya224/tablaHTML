from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods = ["GET"])
def render_lists():
    users = [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    return render_template("index.html", users=users)

@app.errorhandler(404)
def paginaNoEncontrada(error):
    return "¡Lo siento error 404! No hay respuesta. Inténtalo mas tarde"

if __name__ == "__main__":
    app.run(debug=True)