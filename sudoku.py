board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(bo):
    for i in range(len(bo)):
        if (i%3==0):
            print('- '*17)
        for j in range(len(bo[i])):
            if (j%3==0):
                print(' | ', end=' ')
            if (j==8):
                print(bo[i][j], end=' ')
                print(' | ', end=' ')
            else:
                print(bo[i][j], end=' ')
        print('\n')
    print('- ' * 17)

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[i])):
            if(bo[i][j]==0):
                return (i,j)


def valid(bo,num,pos):
    #check row
    for i in range(len(bo)):
        if (bo[pos[0][i)




print_board(board)

print(find_empty(board))