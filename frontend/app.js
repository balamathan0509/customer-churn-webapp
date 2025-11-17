const form = document.getElementById("churn-form");
const resultDiv = document.getElementById("result");
const submitBtn = document.getElementById("submit-btn");

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const tenure = parseInt(document.getElementById("tenure").value, 10);
  const monthly_charges = parseFloat(
    document.getElementById("monthly_charges").value
  );
  const contract = parseInt(document.getElementById("contract").value, 10);
  const support_calls = parseInt(
    document.getElementById("support_calls").value,
    10
  );

  const payload = {
    tenure,
    monthly_charges,
    contract,
    support_calls,
  };

  submitBtn.disabled = true;
  submitBtn.textContent = "Predicting...";
  resultDiv.classList.add("hidden");

  try {
    const response = await fetch("http://127.0.0.1:8000/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    });

    if (!response.ok) {
      throw new Error("Request failed");
    }

    const data = await response.json();

    const percentage = (data.churn_probability * 100).toFixed(1);
    resultDiv.innerHTML = `
      <strong>Result:</strong> ${data.churn_label}<br />
      <span>Churn probability: ${percentage}%</span>
    `;

    resultDiv.classList.remove("hidden", "high", "low");
    resultDiv.classList.add(
      data.churn_label === "High risk" ? "high" : "low"
    );
  } catch (err) {
    resultDiv.innerHTML =
      "Error contacting prediction API. Please check if the backend is running.";
    resultDiv.classList.remove("hidden", "high", "low");
  } finally {
    submitBtn.disabled = false;
    submitBtn.textContent = "Predict Churn";
  }
});
