const form = document.getElementById("appointmentForm");
const message = document.getElementById("message");

form.addEventListener("submit", async function (event) {
  event.preventDefault();

  const appointmentData = {
    name: document.getElementById("name").value,
    email: document.getElementById("email").value,
    service: document.getElementById("service").value,
    date: document.getElementById("date").value,
  };

  try {
    const response = await fetch("http://localhost:8000/appointments", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(appointmentData),
    });

    const data = await response.json();

    message.textContent = data.message;
    form.reset();
  } catch (error) {
    message.textContent = "Unable to submit appointment. Please try again.";
    console.error("Error:", error);
  }
});