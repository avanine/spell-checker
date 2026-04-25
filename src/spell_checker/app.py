"""Flask-sovellus kirjoitusvirheiden tarkistukseen."""

from pathlib import Path
from flask import Flask, request, render_template, jsonify
from spell_checker.trie import Trie
from spell_checker.suggestions import suggest

app = Flask(__name__)

def load_words():
    """Lataa sanalistan tiedostosta ja tallentaa sen trieen."""
    data_path = Path(__file__).resolve().parents[2] / "data" / "english_words.txt"

    word_trie = Trie()

    with open(data_path, encoding='utf-8') as file:
        for rank, line in enumerate(file):
            word = line.strip()
            if word:
                word_trie.insert(word, frequency_rank=rank)
    return word_trie

trie = load_words()

@app.route("/")
def index():
    """Palauttaa etusivun."""
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check():
    """Tarkistaa listan sanoja ja palauttaa tulokset JSON-muodossa."""
    data = request.get_json()
    words = data.get("words", [])
    results = {}
    for word in words:
        cleaned = word.lower().strip()
        if cleaned:
            results[word] = trie.search(cleaned)
    return jsonify(results)

@app.route("/suggest")
def get_suggestions():
    """Palauttaa korjausehdotukset annetulle sanalle."""
    word = request.args.get("word", "")
    if word:
        results = suggest(trie, word.lower())
        return jsonify({"suggestions": results})
    return jsonify({"suggestions": []})

@app.route("/add", methods=["POST"])
def add_word():
    """Lisää sanan sanakirjaan."""
    data = request.get_json()
    word = data.get("word", "").lower().strip()
    if word:
        trie.insert(word)
        return jsonify({"added": True})
    return jsonify({"added": False})

if __name__ == "__main__":
    app.run(debug=True, port=5001)
