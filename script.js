function addMatch() {
  var player1 = document.getElementById('player1').value;
  var player2 = document.getElementById('player2').value;
  var winner = document.getElementById('winner').value;

  // Send data to Streamlit
  var streamlitEvents = window.streamlitEvents || (window.streamlitEvents = []);
  streamlitEvents.push(function() {
      window.streamlitEvents.broadcast({player1: player1, player2: player2, winner: winner});
  });
}
