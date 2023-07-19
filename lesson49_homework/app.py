from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    # server_message = ''
    client_message = ''
    if request.method == "POST":
        client_message = request.form.get('message')
    if client_message == "hi":
        server_message = "Hello"
    elif client_message != '':
        server_message = "How are you"
    else:
        server_message = "Write something to me"
    return render_template("index.html", message=server_message)


@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)
