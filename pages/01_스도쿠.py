import streamlit as st
import random
import copy

# 스도쿠 유효성 검사 함수
def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

# 스도쿠 퍼즐 해결 함수
def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True

# 스도쿠 퍼즐 생성 함수
def generate_puzzle():
    board = [[0 for _ in range(9)] for _ in range(9)]
    filled = 0
    while filled < 17:
        row, col = random.randint(0, 8), random.randint(0, 8)
        if board[row][col] == 0:
            num = random.randint(1, 9)
            if is_valid(board, row, col, num):
                board[row][col] = num
                filled += 1
    solution = copy.deepcopy(board)
    solve(solution)
    return board, solution

# 퍼즐 상태 초기화
def reset_puzzle():
    puzzle, solution = generate_puzzle()
    st.session_state["puzzle"] = puzzle
    st.session_state["solution"] = solution
    st.session_state["new_game"] = False

# 상태 초기화 또는 새 게임
if "puzzle" not in st.session_state or st.session_state.get("new_game", False):
    reset_puzzle()

st.title("🧩 스도쿠 게임")
st.markdown("빈 칸에 1~9 사이 숫자를 입력하세요.")

puzzle = st.session_state["puzzle"]
solution = st.session_state["solution"]
user_grid = []

# 사용자 입력 그리드 생성
for i in range(9):
    cols = st.columns(9)
    row = []
    for j in range(9):
        key = f"{i}-{j}"
        if puzzle[i][j] != 0:
            cols[j].markdown(f"**{puzzle[i][j]}**")
            row.append(puzzle[i][j])
        else:
            value = cols[j].text_input("", max_chars=1, key=key)
            try:
                num = int(value)
                if 1 <= num <= 9:
                    row.append(num)
                else:
                    row.append(0)
            except:
                row.append(0)
    user_grid.append(row)

# 정답 확인
if st.button("✅ 정답 확인"):
    correct = True
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0 and user_grid[i][j] != solution[i][j]:
                correct = False
    if correct:
        st.success("🎉 정답입니다! 완벽해요!")
    else:
        st.warning("😕 틀린 칸이 있어요. 다시 확인해보세요.")

# 새 게임
if st.button("🔄 새 퍼즐 시작"):
    st.session_state["new_game"] = True
    st.info("새 퍼즐이 준비됐습니다. 페이지를 새로고침(F5) 해주세요.")
