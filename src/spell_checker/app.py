from flask import Flask
from pathlib import Path

app = Flask(__name__)


def load_words():
    data_path = Path(__file__).resolve().parents[2] / "data" / "finnish_words_kotus.txt"

    with open(data_path, "r") as f:
        return [word.strip() for word in f]


@app.route("/")
def index():
    words = load_words()
    return "\n".join(words)


if __name__ == "__main__":
    app.run(debug=True)