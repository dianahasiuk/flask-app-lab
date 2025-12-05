from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def resume():
    # головна сторінка "Резюме"
    return render_template("resume.html", title="Резюме")


@app.route("/contacts", methods=["GET", "POST"])
def contacts():
    # сторінка "Контакти" з формою-заглушкою
    return render_template("contacts.html", title="Контакти")


if __name__ == "__main__":
    app.run(debug=True)
