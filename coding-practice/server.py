from flask import Flask, render_template, session, request

app = Flask(__name__)
app.secret_key = "blahhhhhhhh"

@app.route('/')
def show_homepage():
    return render_template('homepage.html')


@app.route('/form')
def show_form():
    return render_template('form.html')


@app.route('/results')
def show_results():
    return render_template('results.html')


@app.route('/save-name', methods=['POST'])
def saves_name():
    persons_name = request.form.get('name')
    return render_template('homepage.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
