import random
def printboard(board):
    print('\n'*100)
    print(f' {board[0]} | {board[1]} | {board[2]}')
    print('---+---+---')
    print(f' {board[3]} | {board[4]} | {board[5]}')
    print('---+---+---')
    print(f' {board[6]} | {board[7]} | {board[8]}')
def playerinput():
    while True:
        player1=input('Enter Marker for Player 1 (X/O): ').upper()
        if player1=='X':
            return('X','O')
        elif player1=='O':
            return('O','X')
def position(board,marker,dii,user):
    while True:
        if user=='user':
            pos=int(input('Enter position: '))
        elif user=='computer':
            pos=random.randint(1,9)
        if board[pos-1]!='X' and board[pos-1]!='O':
            dii[marker].append(pos-1)
            board.pop(pos-1) 
            board.insert(pos-1,marker)
            break
def wincheck(dii,a):
    for k,v in dii.items():
        for i in a:
            for j in v:
                if j in i and count[k]!=3:
                    count[k]+=1
                    if count[k]==3:
                        return k
            count[k]=0
print('Hello! Welcome to TIC-TAC-TOE Game'.center(40,'='))
user=input('Do you want to play with User or Computer? ')
player1,player2=playerinput()
board=[' ']*9
win={player1:[],player2:[]}
count={player1:0,player2:0}
a=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
printboard(board)
print(f"Player 1 is '{player1} and Player 2 is '{player2}'\nPlayer 1 will go first!")
for i in range(9):
    if i%2==0:
        print('Player 1 : ')
        position(board,player1,win,'user')
        printboard(board)
    elif i%2!=0:
        print('Player 2 : ')
        position(board,player2,win,user)
        printboard(board)
    winch=wincheck(win,a)
    if winch==player1:
        print('Player 1 won!')
        break
    elif winch==player2:
        print('Player 2 won!')
        break
    elif winch==None and i==8:
        print('Nobody Won!')
        break
    i+=1