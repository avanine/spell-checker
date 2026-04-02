const textarea = document.getElementById("textarea");
const highlights = document.getElementById("highlights");
const suggestions = document.getElementById("suggestions");
let checkResults = {};

textarea.addEventListener("input", checkWords);

textarea.addEventListener("scroll", () => {
    highlights.scrollTop = textarea.scrollTop;
});

async function checkWords() {
    const text = textarea.value;
    const endsWithSpace = /\s$/.test(text);
    const words = text.match(/[a-zA-ZäöåÄÖÅ]+/g) || [];
    const wordsToCheck = endsWithSpace ? words : words.slice(0, -1);

    if (wordsToCheck.length > 0) {
        const response = await fetch("/check", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ words: wordsToCheck })
        });
        checkResults = await response.json();
        updateHighlights(text, checkResults);
    } else {
        checkResults = {};
        updateHighlights(text, {});
    }
}

function updateHighlights(text, results) {
    const html = text.replace(/[a-zA-ZäöåÄÖÅ]+/g, (match) => {
        if (results[match] === false) {
            return `<mark>${match}</mark>`;
        }
        return match;
    });
    highlights.innerHTML = html + "\n";
}

function getWordAtCursor() {
    const pos = textarea.selectionStart;
    const text = textarea.value;
    const before = text.slice(0, pos);
    const after = text.slice(pos);
    const wordBefore = (before.match(/[a-zA-ZäöåÄÖÅ]+$/) || [""])[0];
    const wordAfter = (after.match(/^[a-zA-ZäöåÄÖÅ]+/) || [""])[0];
    const word = wordBefore + wordAfter;
    const start = pos - wordBefore.length;
    return { word, start, end: start + word.length };
}

textarea.addEventListener("click", async () => {
    const { word } = getWordAtCursor();
    if (!word || checkResults[word] !== false) {
        suggestions.style.display = "none";
        return;
    }

    suggestions.innerHTML = `<strong>${word}:</strong> Ladataan...`;
    suggestions.style.display = "block";

    const response = await fetch(`/suggest?word=${encodeURIComponent(word)}`);
    const data = await response.json();

    if (data.suggestions.length > 0) {
        const links = data.suggestions.map(s =>
            `<span class="suggestion" data-word="${s}" data-original="${word}">${s}</span>`
        ).join(", ");
        suggestions.innerHTML = `<div><strong>${word}:</strong> ${links}</div>`;
    } else {
        suggestions.innerHTML = `<div><strong>${word}:</strong> <span class="no-suggestions">Ei ehdotuksia</span></div>`;
    }
});

suggestions.addEventListener("click", (e) => {
    const el = e.target.closest(".suggestion");
    if (!el) return;
    const replacement = el.dataset.word;
    const original = el.dataset.original;
    const text = textarea.value;
    const lastIndex = text.lastIndexOf(original);
    if (lastIndex !== -1) {
        textarea.value = text.slice(0, lastIndex) + replacement + text.slice(lastIndex + original.length);
        suggestions.style.display = "none";
        checkWords();
    }
});
