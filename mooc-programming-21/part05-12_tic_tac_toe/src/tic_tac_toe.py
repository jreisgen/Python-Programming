def play_turn(game_board: list, x: int, y: int, piece: str):
    if y < len(game_board) and x < len(game_board[0]) and x >= 0 and y >=0:
        if game_board[y][x] == "":
            game_board[y][x] = piece
            return True
        else:
            return False
    else:
        return False

if __name__ == "__main__":
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(play_turn(game_board, 2, 0, "X"))
    print(game_board)