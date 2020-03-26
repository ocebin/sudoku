import time
start_time = time.time()

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
                print(bo[i][j],end=' ')
                print(' | ', end='\n')
            else:
                print(bo[i][j],end=' ')
    print('- ' * 17)
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[i])):
            if(bo[i][j]==0):
                return (i,j)
    return None
def cek_row(num,posx,bo):
    for i in range(9):
        if (bo[posx][i]==num):
            return False
    return True
def cek_col(num,posy,bo):
    for i in range(9):
        if (bo[i][posy]==num):
            return False
    return True
def cek_sub(num,posx,posy,bo):
    for i in range((posx//3)*3,((posx//3)*3)+3):
        for y in range((posy//3)*3,((posy//3)*3)+3):
            if(bo[i][y]==num):
                return False
    return True
def valid(bo):
    zero = find_empty(bo)
    if(zero == None):
        return True

    posx,posy = zero
    for num in range(1, 10):
        hasil_row = cek_row(num,posx, bo)
        hasil_col = cek_col(num,posy, bo)
        hasil_sub = cek_sub(num,posx,posy,bo)
        if(hasil_row == True and hasil_col == True and hasil_sub == True):
            bo[posx][posy] = num
            #print("OSBIN",'(',posx,posy,')',bo[posx][posy])
            #print_board(bo)
            if(valid(bo)):
                return True
            bo[posx][posy]=0
            #print("O",'(',posx,posy,')',bo[posx][posy])
            #print_board(bo)

    return False
print('AWAL SUDOKU')
print_board(board)

valid(board)
print("SOLVED SUDOKU")
print_board(board)
print("Solve dalam ",time.time()-start_time, "detik")