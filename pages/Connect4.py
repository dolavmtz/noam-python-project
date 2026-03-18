import streamlit as st
import random

#משתנים קבועים
ROWS = 6
COLS = 7

PLAYER = "🟡"
COMPUTER = "⚫"
EMPTY = "⚪"

def computerTurn():
    randomCol = random.randint(0,COLS-1)
    click(randomCol)

#לוח
def newBoard():
    board = []
    for r in range(ROWS):
        row = []
        for cell in range(COLS):
            row.append((EMPTY))
        board.append(row)
    return board

if "board" not in st.session_state:
    st.session_state.board = newBoard()

board = st.session_state.board

if "turn" not in st.session_state:
    st.session_state.turn = PLAYER

turn = st.session_state.turn

def switchTurn():
    if st.session_state.turn == PLAYER:
        st.session_state.turn = COMPUTER
    else:
        st.session_state.turn = PLAYER

def click(col):
    #st.write(col)
    for i in range(ROWS - 1,-1, -1):
        if board[i][col]==EMPTY:
            board[i][col] = turn
            break
    st.session_state.board = board
    switchTurn()
    st.rerun()

if turn == COMPUTER:
    computerTurn()

for r in range(ROWS):
    columns = st.columns(COLS)
    for c in range(COLS):
        with columns[c]:
            cell = board[r][c]
            if st.button(cell,key= f"row_{r}_col_{c}",use_container_width=True):
                click(c)