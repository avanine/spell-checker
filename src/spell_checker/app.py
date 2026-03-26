from flask import Flask, request, render_template, jsonify
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
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check():
    data = request.get_json()
    words = data.get("words", [])
    results = {}
    for word in words:
        cleaned = word.lower().strip()
        if cleaned:
            results[word] = trie.search(cleaned)
    return jsonify(results)


if __name__ == "__main__":
    app.run(debug=True, port=5001)