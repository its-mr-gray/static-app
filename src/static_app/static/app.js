const button = document.getElementById("my-button");
const responsePara = document.getElementById("response");

button.addEventListener("click", async () => {
  const response = await fetch("/api/message");
  const data = await response.json();

  responsePara.textContent = data.message;
});
