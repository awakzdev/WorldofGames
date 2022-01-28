from flask import *

app = Flask(__name__)


@app.route('/', methods=['GET'])
def returnhtml():
    f = open("Scores.txt", "r+")
    result = f.read()
    html = open("scoreviaflask/Score.html", "r+")
    text = html.read().format(SCORE=result)
    if result != "":
        return text
    else:
        return render_template('Error.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8777)
