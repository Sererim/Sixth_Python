_board = [[0]*8 for _ in range(8)]

def solution(queens: list[list[int]]) -> bool | None:
    """Solution function for eight queens puzzle.

    Args:
        queens (list[list[int]]):
        Coordinate list of 8 queens palcments on 8x8 board.
        Coordinates e [1;8]

    Returns:
        bool: True if queens are not under attack.
        False if queens are under attack.
    """
    # Date checking
    if len(queens) != 8:
        return None
    for i in queens:
        if (len(i)) != 2:
            return None
    
    for x in queens:
        _board[x[0]][x[1]] = 1
    
    for i in _board:
        print(i)
    
    for x in queens:
        if not attack(x[0], x[1]):
            return True
        
    return False
                    
        
def attack(x: int, y: int) -> bool:
    #Check vertically
    for i in range(8):
        if _board[x][i] == 1 or _board[i][y] == 1:
            return True
    
    # Check diagonally
    for i in range(8):
        for j in range(8):
            if (i + j == x + y) or (i - j == x - y):
                if _board[i][j] == 1:
                    return True
    
    return False
        

if __name__ == "__main__":
    print(solution([[0, 0], [1, 1], [2, 2], [3, 3], 
              [4, 4], [5, 5], [6, 6], [7, 7]]))
