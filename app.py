from flask import Flask, render_template, request, redirect

app = Flask(__name__)

items = {}
next_id = 1

@app.route("/")
def index():
    return render_template("index.html", items=items)

@app.route("/add", methods=["POST"])
def add():
    global next_id
    items[next_id] = request.form["name"]
    next_id += 1
    return redirect("/")

@app.route("/delete/<int:id>")
def delete(id):
    items.pop(id, None)
    return redirect("/")

@app.route("/edit/<int:id>", methods=["POST"])
def edit(id):
    items[id] = request.form["name"]
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)