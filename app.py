from flask import Flask, render_template

app = Flask(__name__)

recipes = [
    {
        "id": 1,
        "name": "Яєчня",
        "ingredients": "Яйця, сіль",
        "steps": "Розбити яйця і посмажити"
    },
    {
        "id": 2,
        "name": "Бутерброд",
        "ingredients": "Хліб, сир",
        "steps": "Покласти сир на хліб"
    }
]

@app.route("/")
def index():
    return render_template("index.html", recipes=recipes)

@app.route("/recipe/<int:id>")
def recipe(id):
    recipe = next((r for r in recipes if r["id"] == id), None)
    return render_template("recipe.html", recipe=recipe)

if __name__ == "__main__":
    app.run(debug=True)