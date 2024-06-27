import streamlit as st
import pandas as pd

# Title of the app
st.title('TORO VS COCO')

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

# Input fields for match details
player1 = st.text_input('Player 1', 'Player 1 Name')
player2 = st.text_input('Player 2', 'Player 2 Name')
winner = st.selectbox('Winner', ['Player 1', 'Player 2'])

# Button to add the match
if st.button('Add Match'):
    add_match(player1, player2, winner)
    st.success('Match added!')

# Display the match records
if st.session_state.matches:
    df = pd.DataFrame(st.session_state.matches)
    st.table(df)

