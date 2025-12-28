console.log("EL Care loaded");

const BACKEND_URL = "https://your-vercel-deployed-app.vercel.app"; // replace with your deployed FastAPI URL

function toJSON(form) {
  const data = {};
  new FormData(form).forEach((v, k) => (data[k] = Number(v)));
  return data;
}

async function submitForm(form, endpoint) {
  try {
    const res = await fetch(`${BACKEND_URL}/${endpoint}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(toJSON(form)),
    });

    const result = await res.json();
    console.log(result);

    // Display the result in the pre element
    const pre = document.getElementById("result");
    pre.textContent = JSON.stringify(result, null, 2);
  } catch (err) {
    console.error("Error:", err);
    alert("Failed to fetch prediction. Please check the backend.");
  }
}

// Attach event listener to heart form
document.getElementById("heartForm").onsubmit = (e) => {
  e.preventDefault();
  submitForm(e.target, "analyze_heart");
};
