import streamlit as st
import random
import time

#משתנים קבועים
ROWS = 6
COLS = 7

PLAYER = "🟡"
COMPUTER = "⚫"
EMPTY = "⚪"

def computerTurn():
    time.sleep(1)
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

def checkWinner(check_row, check_col):
    #for row in range(ROWS):
    row = check_row
    for cell in range(COLS - 3):
        if board[row][cell] == EMPTY:
            continue
        for i in range(cell,cell+4):
            if board[row][i] != board[row][cell]:
                print(f"No Win starts with row {row} cell {cell}")
                break
        else:
            print("הגיעה לסיום")
            print(board[row][cell])
            return board[row][cell]

    col = check_col
    for cell in range(ROWS - 3):
        if board[cell][col] == EMPTY:
            continue
        for i in range(cell,cell+4):
            if board[i][col] != board[cell][col]:
                print(f"No Win starts with row {row} cell {cell}")
                break
        else:
            print("הגיעה לסיום")
            print(board[cell][col])
            return board[cell][col]

    offset = min (check_row,check_col)
    start_row = check_row - offset
    start_col = check_col-offset

    if start_row + 4 >ROWS or start_col + 4 >COLS:
        print("אין ניצחון באלכסון הזה")
    else:
        for i in range(ROWS):
            row = start_row + i
            col = start_col + i

            print(f"start checking: {row} {col}")

            if col == COLS or row == ROWS:
                break
            elif board[row] [col] == EMPTY:
                count = 0
            elif board[row] [col] != board[check_row][check_col]:
                count = 0
            else:
                count += 1
            if count == 4:
                print("ניצחון")
                print(board[row][col])
                return board[row][col]

    dist_bottom = ROWS - 1 - check_row
    dist_left = check_col
    offset = min (dist_left,dist_bottom)

    start_row = check_row + offset
    start_col = check_col - offset

    if start_row - 4 > 0 or start_col + 4 >COLS:
        print("אין ניצחון באלכסון זה")
    else:
        count = 0
        for cell in range(ROWS):
            row = start_row - i
            col = start_col + i
            print(f"start checking: {row} {col}")

            if col == COLS or row == ROWS or row<0:
                break
            elif board[row] [col] == EMPTY:
                count = 0
            elif board[row] [col] != board[check_row][check_col]:
                count = 0
            else:
                count += 1
            if count == 4:
                print("ניצחון")
                print(board[row][col])
                return board[row][col]

    return None

def click(col):
    if board[0][col] != EMPTY:
        return

    #st.write(col)
    for i in range(ROWS - 1,-1, -1):
        if board[i][col]==EMPTY:
            board[i][col] = turn
            st.session_state.winner = checkWinner(i,col)
            break
    st.session_state.board = board
    switchTurn()
    st.rerun()

winner =None
if "winner" in st.session_state:
    winner = st.session_state.winner

can_play = True


has_empty = True
for col in range(COLS):
    if board[0][col] == EMPTY:
        has_empty = True
        break

if winner == PLAYER:
    st.info("ניצחת!")
    can_play = False
elif winner == COMPUTER:
    st.info("המחשב ניצח")
    can_play = False
else:
    if turn == PLAYER:
        st.info("עכשיו תור השחקן")
    else:
        st.status("המחשב חושב")

for r in range(ROWS):
    columns = st.columns(COLS)
    for c in range(COLS):
        with columns[c]:
            cell = board[r][c]
            if st.button(cell,key= f"row_{r}_col_{c}",use_container_width=True, disabled= turn==COMPUTER or not can_play):
                click(c)

if turn == COMPUTER and can_play:
    computerTurn()