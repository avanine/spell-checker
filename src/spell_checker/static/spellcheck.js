const textarea = document.getElementById("textarea");
const highlights = document.getElementById("highlights");
const suggestions = document.getElementById("suggestions");
const errorCount = document.getElementById("error-count");
let checkResults = {};

textarea.addEventListener("input", checkWords);

textarea.addEventListener("scroll", () => {
    highlights.scrollTop = textarea.scrollTop;
});

async function checkWords() {
    const text = textarea.value;
    const endsWithSpace = /\s$/.test(text);
    const words = text.match(/[a-zA-Z]+/g) || [];
    const wordsToCheck = endsWithSpace ? words : words.slice(0, -1);

    if (wordsToCheck.length > 0) {
        const response = await fetch("/check", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ words: wordsToCheck })
        });
        checkResults = await response.json();
        updateHighlights(text, checkResults);
        updateErrorCount(checkResults);
    } else {
        checkResults = {};
        updateHighlights(text, {});
        updateErrorCount({});
    }
}

function updateHighlights(text, results) {
    const html = text.replace(/[a-zA-Z]+/g, (match) => {
        if (results[match] === false) {
            return `<mark>${match}</mark>`;
        }
        return match;
    });
    highlights.innerHTML = html + "\n";
}

function updateErrorCount(results) {
    const words = textarea.value.match(/[a-zA-Z]+/g) || [];
    const count = words.filter(w => results[w] === false).length;
    if (count > 0) {
        errorCount.textContent = `⚠️ ${count} misspelled word${count > 1 ? "s" : ""}`;
        errorCount.style.opacity = "1";
    } else {
        errorCount.textContent = "";
        errorCount.style.opacity = "0";
    }
}

function getWordAtCursor() {
    const pos = textarea.selectionStart;
    const text = textarea.value;
    const before = text.slice(0, pos);
    const after = text.slice(pos);
    const wordBefore = (before.match(/[a-zA-Z]+$/) || [""])[0];
    const wordAfter = (after.match(/^[a-zA-Z]+/) || [""])[0];
    const word = wordBefore + wordAfter;
    const start = pos - wordBefore.length;
    return { word, start, end: start + word.length };
}

textarea.addEventListener("click", async () => {
    const { word, start, end } = getWordAtCursor();
    if (!word || checkResults[word] !== false) {
        suggestions.style.opacity = "0"; suggestions.style.pointerEvents = "none";
        return;
    }

    suggestions.innerHTML = `<strong>${word}:</strong> Loading...`;
    suggestions.style.opacity = "1"; suggestions.style.pointerEvents = "auto";

    const response = await fetch(`/suggest?word=${encodeURIComponent(word)}`);
    const data = await response.json();

    const addBtn = `<span class="add-to-dict" data-word="${word}">+ Add to dictionary</span>`;
    if (data.suggestions.length > 0) {
        const links = data.suggestions.map(s =>
            `<span class="suggestion" data-word="${s}" data-start="${start}" data-end="${end}">${s}</span>`
        ).join(" ");
        suggestions.innerHTML = `<div><strong>${word}:</strong> ${links} ${addBtn}</div>`;
    } else {
        suggestions.innerHTML = `<div><strong>${word}:</strong> <span class="no-suggestions">No suggestions</span> ${addBtn}</div>`;
    }
});

suggestions.addEventListener("click", async (e) => {
    const addBtn = e.target.closest(".add-to-dict");
    if (addBtn) {
        await fetch("/add", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ word: addBtn.dataset.word })
        });
        suggestions.style.opacity = "0"; suggestions.style.pointerEvents = "none";
        checkWords();
        return;
    }

    const el = e.target.closest(".suggestion");
    if (!el) return;
    const replacement = el.dataset.word;
    const start = parseInt(el.dataset.start);
    const end = parseInt(el.dataset.end);
    const text = textarea.value;
    textarea.value = text.slice(0, start) + replacement + text.slice(end);
    suggestions.style.opacity = "0"; suggestions.style.pointerEvents = "none";
    checkWords();
});
