from flask import Flask
from pathlib import Path
from trie import Trie

app = Flask(__name__)

def load_words():
    data_path = Path(__file__).resolve().parents[2] / "data" / "finnish_words_kotus.txt"

    trie = Trie()

    trie.insert("moi")
    trie.insert("moikka")
    trie.insert("moro")

    return str(trie.search("mo"))

@app.route("/")
def index():
    return load_words()


if __name__ == "__main__":
    app.run(debug=True)