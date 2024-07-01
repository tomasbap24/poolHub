function submitForm() {
  const player1 = document.getElementById('player1').value;
  const player2 = document.getElementById('player2').value;
  const winner = document.getElementById('winner').value;

  fetch('/submit', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
      },
      body: JSON.stringify({ player1, player2, winner }),
  })
  .then(response => response.json())
  .then(data => {
      if (data.success) {
          alert('Match added successfully!');
      }
  })
  .catch((error) => {
      console.error('Error:', error);
  });
}
