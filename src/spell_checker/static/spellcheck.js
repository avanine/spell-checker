const textarea = document.getElementById("textarea");
const highlights = document.getElementById("highlights");
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
        const results = await response.json();
        updateHighlights(text, results);
    } else {
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
