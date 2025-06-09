async function sendMessage() {
  const input = document.getElementById("user-input");
  const chatBox = document.getElementById("chat-box");

  const userMsg = input.value;
  if (!userMsg.trim()) return;

  // Tampilkan pesan user
  chatBox.innerHTML += `<div class="msg user">${userMsg}</div>`;
  input.value = "";

  // Kirim ke backend
  const res = await fetch("/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: userMsg }),
  });

  const data = await res.json();

  // Tampilkan balasan bot
  chatBox.innerHTML += `<div class="msg bot">Bibi: ${data.response}</div>`;
  chatBox.scrollTop = chatBox.scrollHeight;
}
