from flask import Flask, request, render_template
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
    word = request.args.get("word", "")
    result = None
    if word:
        result = trie.search(word.lower())
    return render_template("index.html", word=word, result=result)


if __name__ == "__main__":
    app.run(debug=True, port=5001)