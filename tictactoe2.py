```Approach-2```


poss={
    '1':[('2','3'),('4','7'),('5','9')],
    '2':[('1','3'),('5','8')],
    '3':[('1','2'),('6','9'),('5','7')],
    '4':[('1','7'),('5','6')],
    '5':[('4','6'),('2','8'),('1','9'),('3','7')],
    '6':[('3','9'),('4','5')],
    '7':[('1','4'),('8','9'),('5','3')],
    '8':[('7','9'),('5','2')],
    '9':[('6','3'),('7','8'),('1','5')]
}
 
theBoard = {'7':'-','8':'-','9':'-',
            '4':'-','5':'-','6':'-',
            '1':'-','2':'-','3':'-'}
board_Keys = []
for key in theBoard:
    board_Keys.append(key)
    
def printBoard(board):
    print('-------------')
    print('| '+board['7']+' | '+board['8']+' | '+board['9']+' |')
    print('-------------')
    print('| '+board['4']+' | '+board['5']+' | '+board['6']+' |')
    print('-------------')
    print('| '+board['1']+' | '+board['2']+' | '+board['3']+' |')
    print('-------------')
printBoard(theBoard)
 
def win(board):
    if board['7'] == board['8']==board['9']!='-':return True
    elif board['4']==board['5']==board['6']!='-':return True
    elif board['1']==board['2']==board['3']!='-':return True
    elif board['1']==board['4']==board['7']!='-':return True
    elif board['2']==board['5']==board['8']!='-':return True
    elif board['3']==board['6']==board['9']!='-':return True
    elif board['1']==board['5']==board['9']!='-':return True
    elif board['3']==board['5']==board['7']!='-':return True
    else:return False

    
def poswin(board, turn):
    if board['4']==board['5']==turn or board['6']==board['5']==turn or board['4']==board['6']==turn:
        if board['4']=='-':return '4'
        elif board['5']=='-':return '5'
        elif board['6']=='-':return '6'
    if board['1']==board['2']==turn or board['2']==board['3']==turn or board['3']==board['1']==turn:
        if board['1']=='-':return '1'
        elif board['2']=='-':return '2'
        elif board['3']=='-':return '3'
    if board['7']==board['8']==turn or board['8']==board['9']==turn or board['9']==board['7']==turn:
        if board['7']=='-':return '7'
        elif board['8']=='-':return '8'
        elif board['9']=='-':return '9'
    if board['4']==board['5']==turn or board['6']==board['5']==turn or board['4']==board['6']==turn:
        if board['4']=='-':return '4'
        elif board['5']=='-':return '5'
        elif board['6']=='-':return '6'
    if board['1']==board['4']==turn or board['4']==board['7']==turn or board['1']==board['7']==turn:
        if board['1']=='-':return '1'
        elif board['4']=='-':return '4'
        elif board['7']=='-':return '7'
    if board['2']==board['5']==turn or board['5']==board['8']==turn or board['8']==board['2']==turn:
        if board['2']=='-':return '2'
        elif board['5']=='-':return '5'
        elif board['8']=='-':return '8'
    if board['3']==board['6']==turn or board['6']==board['9']==turn or board['9']==board['3']==turn:
        if board['3']=='-':return '3'
        elif board['6']=='-':return '6'
        elif board['9']=='-':return '9'
    if board['1']==board['5']==turn or board['5']==board['9']==turn or board['9']==board['1']==turn:
        if board['1']=='-':return '1'
        elif board['5']=='-':return '5'
        elif board['9']=='-':return '9'
    if board['3']==board['5']==turn or board['5']==board['7']==turn or board['3']==board['7']==turn:
        if board['3']=='-':return '3'
        elif board['5']=='-':return '5'
        elif board['7']=='-':return '7'
    return '0'
    
def game():
    count=0
    while True:
        if count==9:
            print("!! Game Over !!")
            print("It's a tie.")
            break
        move=input("It's your turn. place at ? ")
        if theBoard[move]=='-':
            theBoard[move]='X'
            count+=1
        else:
            print("The place is already filled.\nplace at ?")
            continue
        printBoard(theBoard)
        if count>4 and win(theBoard):
            print("!! Game Over !!")
            print("You have Won.")
            break
        print("A.I's turn.")
        if move!='5' and theBoard['5']=='-':theBoard['5']='O'
        else:
            pos = poswin(theBoard, 'O')
            if pos!='0':
                theBoard[pos]='O'
            else:
                pos=poswin(theBoard, 'X')
                if pos=='0':
                    for p in poss[move]:
                        if theBoard[p[0]] == '-':
                            theBoard[p[0]] = 'O'
                            break
                        elif theBoard[p[1]] == '-':
                            theBoard[p[1]] = 'O'
                            break
                else:theBoard[pos]='O'
            count+=1
        printBoard(theBoard)
        if count>4 and win(theBoard):
            print("!! Game Over !!")
            print("A.I won.")
            break
game()
