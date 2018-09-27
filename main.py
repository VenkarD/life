def print_field():
    pass
def alive(point,board):
    x,y = point
    counts=count_live_neighbors(point,board)
    if counts == 3 or (counts == 2 and point in board):
        return True
    return False
def count_live_neighbors(point, board):
    j=0
    for i in get_neighbors(point):
        if i in board:
            j=j+1
    return j
def get_neighbors(point):
    x,y = point
    return [((x+j),(y+i)) for i in range(-1,2) for j in range(-1,2) if not i==j==0]

def new_step(board):
    new_board=set()
    board_with_neighbors =list(board)
    for i in board:
        board_with_neighbors +=get_neighbors(i)
    board_with_neighbors = set(board_with_neighbors)
    for i in board_with_neighbors:
        if alive(i,board):
            new_board.add(i)
    return new_board
    
    
    


image = set([(0, 0), (1, 0), (2, 0), (0, 1), (1, 2)])

for i in range(1):
    image = new_step(image)
    print(image)
