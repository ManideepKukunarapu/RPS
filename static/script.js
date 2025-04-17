function play(choice) {
    fetch('/play', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ choice: choice })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('result').innerText =
            `🤖 Computer chose: ${data.computer}\n💥 You ${data.result}!`;
    });
}

function resetGame() {
    document.getElementById('result').innerText = "🎮 Make your move!";
}