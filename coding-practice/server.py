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
    cheery = request.args.get('cheery')
    honest = request.args.get('honest')
    dreary = request.args.get('dreary')

    if cheery and honest and dreary:
        message = "How so?"
    elif cheery and honest and not dreary:
        message = "I love that for you."
    elif honest and dreary:
        message = "Oh no! What's wrong?"
    elif cheery and dreary and not honest: 
        message = "Well that is a bit confusing!"
    elif honest:
        message = "At least you're honest!"
    else:
        message = "Would you like some wine?"

    return render_template('results.html', msg=message)


@app.route('/save-name', methods=['POST'])
def saves_name():
    persons_name = request.form.get('name')
    session['name'] = persons_name
    return render_template('homepage.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
