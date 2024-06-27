import streamlit as st
import pandas as pd

# Title of the app
st.title('Pool Matches Record')

# Initialize session state to store match data
if 'matches' not in st.session_state:
    st.session_state.matches = []

# Function to add a new match record
def add_match(player1, player2, winner):
    match = {
        'Player 1': player1,
        'Player 2': player2,
        'Winner': winner
    }
    st.session_state.matches.append(match)

# Load the HTML file
with open('custom_ui.html', 'r') as f:
    html = f.read()
st.markdown(html, unsafe_allow_html=True)

# Capture JavaScript event
event = st.event('streamlitEvents')
if event:
    add_match(event.player1, event.player2, event.winner)
    st.success('Match added!')

# Display the match records
if st.session_state.matches:
    df = pd.DataFrame(st.session_state.matches)
    st.table(df)
