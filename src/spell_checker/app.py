from flask import Flask
from pathlib import Path
from trie import Trie

app = Flask(__name__)

def load_words():
    data_path = Path(__file__).resolve().parents[2] / "data" / "finnish_words_kotus.txt"

    trie = Trie()

    with open(data_path, encoding='utf-8') as file:
        for line in file:
            word = line.strip()
            if word:
                trie.insert(word)
    return trie

trie = load_words()

@app.route("/")
def index():
    return "<br>".join(trie)


if __name__ == "__main__":
    app.run(debug=True)