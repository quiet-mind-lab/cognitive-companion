const submitBtn = document.getElementById("submitBtn");
const clearBtn = document.getElementById("clearBtn");
const input = document.getElementById("journalInput");
const resultBox = document.getElementById("result");
const sentimentLabel = document.getElementById("sentimentLabel");
const sentimentScore = document.getElementById("sentimentScore");

// Explicit initial state
resultBox.classList.add("hidden");

submitBtn.addEventListener("click", async (event) => {
  event.preventDefault();

  const text = input.value.trim();
  if (!text) {
    alert("Write something first.");
    return;
  }

  submitBtn.disabled = true;
  submitBtn.innerText = "Saving...";

  try {
    const response = await fetch("http://127.0.0.1:8000/journal/text", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ text })
    });

    const data = await response.json();

    sentimentLabel.innerText = data.sentiment.label;
    sentimentScore.innerText = data.sentiment.score.toFixed(2);

    resultBox.classList.remove("hidden");

  } catch (err) {
    alert("Backend error. Check server.");
  }

  submitBtn.disabled = false;
  submitBtn.innerText = "Save Entry";
});


clearBtn.addEventListener("click", () => {
  input.value = "";
  resultBox.classList.add("hidden");
  sentimentLabel.innerText = "";
  sentimentScore.innerText = "";
});
