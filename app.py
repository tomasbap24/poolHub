import streamlit as st
import pandas as pd
import sqlite3

# Function to create the database connection
def get_db_connection():
    conn = sqlite3.connect('pool_matches.db')
    conn.row_factory = sqlite3.Row
    return conn

# Function to add a new match record
def add_match(player1, player2, winner):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO matches (player1, player2, winner) VALUES (?, ?, ?)
    ''', (player1, player2, winner))
    conn.commit()
    conn.close()

# Function to load matches
def load_matches():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM matches')
    matches = cursor.fetchall()
    conn.close()
    return pd.DataFrame(matches, columns=['ID', 'Player 1', 'Player 2', 'Winner'])

# Function to delete a match
def delete_match(match_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM matches WHERE id = ?', (match_id,))
    conn.commit()
    conn.close()

# Title of the app
st.title('TORO VS COCO')

# Input form for new match
player1 = st.text_input('Player 1')
player2 = st.text_input('Player 2')
winner = st.selectbox('Winner', [player1, player2])

if st.button('Add Match'):
    if player1 and player2 and winner:
        add_match(player1, player2, winner)
        st.success('Match added!')
        st.experimental_rerun()
    else:
        st.error('Please fill in all fields')

# Display the match records
st.write("Match Records:")
matches_df = load_matches()

if not matches_df.empty:
    for index, row in matches_df.iterrows():
        st.write(f"Match ID: {row['ID']}, Player 1: {row['Player 1']}, Player 2: {row['Player 2']}, Winner: {row['Winner']}")
        if st.button(f"Delete Match {row['ID']}", key=row['ID']):
            delete_match(row['ID'])
            st.success(f"Match {row['ID']} deleted!")
            st.experimental_rerun()
else:
    st.write("No matches found.")
