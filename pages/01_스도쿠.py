import streamlit as st
import random
import copy

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

def solve_count(board, count=0):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        count = solve_count(board, count)
                        if count > 1:
                            return count
                        board[row][col] = 0
                return count
    return count + 1

def generate_full_board():
    board = [[0 for _ in range(9)] for _ in range(9)]
    def fill():
        for i in range(81):
            row, col = divmod(i, 9)
            if board[row][col] == 0:
                nums = list(range(1, 10))
                random.shuffle(nums)
                for num in nums:
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if fill():
                            return True
                        board[row][col] = 0
                return False
        return True
    fill()
    return board

def generate_unique_puzzle():
    board = generate_full_board()
    puzzle = copy.deepcopy(board)
    cells = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(cells)

    for row, col in cells:
        temp = puzzle[row][col]
        puzzle[row][col] = 0
        board_copy = copy.deepcopy(puzzle)
        if solve_count(board_copy) != 1:
            puzzle[row][col] = temp  # 해답이 2개 이상이면 복원

    return puzzle, board

# 초기화
if "puzzle" not in st.session_state:
    puzzle, solution = generate_unique_puzzle()
    st.session_state.puzzle = puzzle
    st.session_state.solution = solution

st.title("🧠 단일 해답 스도쿠")
st.write("빈 칸에 숫자를 입력하고 정답을 맞춰보세요!")

puzzle = st.session_state.puzzle
solution = st.session_state.solution
user_input = []

for i in range(9):
    cols = st.columns(9)
    row = []
    for j in range(9):
        key = f"{i}-{j}"
        if puzzle[i][j] != 0:
            cols[j].markdown(f"**{puzzle[i][j]}**")
            row.append(puzzle[i][j])
        else:
            val = cols[j].text_input("", max_chars=1, key=key)
            try:
                num = int(val)
                if 1 <= num <= 9:
                    row.append(num)
                else:
                    row.append(0)
            except:
                row.append(0)
    user_input.append(row)

if st.button("✅ 정답 확인"):
    correct = all(
        user_input[i][j] == solution[i][j]
        if puzzle[i][j] == 0 else True
        for i in range(9) for j in range(9)
    )
    if correct:
        st.success("🎉 정답입니다! 완벽히 해결했어요.")
    else:
        st.error("❌ 틀린 칸이 있어요. 다시 확인해보세요.")

if st.button("🔄 새 퍼즐"):
    st.session_state.clear()
    st.info("✅ 새 퍼즐이 준비되었습니다. 페이지를 새로고침(F5 또는 Ctrl+R) 해주세요.")
