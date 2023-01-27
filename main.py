import time

row1 = "   :   :   "
row2 = "   :   :   "
row3 = "   :   :   "
break1 = "--- --- ---"
started = False
symbol = 'X'
key = {1 : 1, 2 : 5, 3 : 9}
turns = 0

def returnBoard(row1, row2, row3, break1):
    board = f"{row1}\n{break1}\n{row2}\n{break1}\n{row3}"
    return board

def findColumn(instruction):
    if instruction == 1 or instruction == 4 or instruction == 7:
        return 1
    elif instruction == 2 or instruction == 5 or instruction == 8:
        return 2
    else:
        return 3

def findRow(instruction):
    if instruction > 0 and instruction <= 3:
        return 1
    elif instruction >= 4 and instruction <= 6:
        return 2
    else:
        return 3

def checkIfEmpty(row, column, row1, row2, row3, key):
    index = key[column]
    if row == 1:
        row1 = list(row1)
        if row1[index] == " ":
            return True
        else:
            return False

    elif row == 2:
        row2 = list(row2)
        if row2[index] == " ":
            return True
        else:
            return False

    else:
        row3 = list(row3)
        if row3[index] == " ":
            return True
        else:
            return False

def updateRow(column, row, symbol, row1, row2, row3):
    if row == 1:
        row1 = list(row1)
        row1[key[column]] = symbol
        row1 = ''.join(row1)
        return row1
    elif row == 2:
        row2 = list(row2)
        row2[key[column]] = symbol
        row2 = ''.join(row2)
        return row2
    else:
        row3 = list(row3)
        row3[key[column]] = symbol
        row3 = ''.join(row3)
        return row3

def checkForWin(symbol, row1, row2, row3):
    return False

print("Are you ready to play a game of noughts and crosses?\nReset the board at any time by typing 'reset'!\nType 'yes' to start!")
while started == False:
    start = input('')
    if start == 'yes':
        started = True

while started == True:
    print(f"It's {symbol}'s turn!")
    print(returnBoard(row1, row2, row3, break1))
    instruction = input(f"Where would you like to place your {symbol}? [Position 1-9]\n")
    if instruction != 'reset':
        instruction = int(instruction)
        if instruction <= 9 and instruction >= 1:
            column = findColumn(instruction)
            row = findRow(instruction)
            if checkIfEmpty(row, column, row1, row2, row3, key) == True:
                if row == 1:
                    row1 = updateRow(column, row, symbol, row1, row2, row3)
                elif row == 2:
                    row2 = updateRow(column, row, symbol, row1, row2, row3)
                else:
                    row3 = updateRow(column, row, symbol, row1, row2, row3)
                if symbol == 'X':
                    symbol = 'O'
                else:
                    symbol = 'X'
                turns = turns + 1
                if turns >= 5:
                    if checkForWin() == True:
                        print(f"{symbol} Wins!")
                        time.sleep(1)
                        print('Resetting...')
                        time.sleep(5)
            else:
                print("There is already an X or an O in that position!")
        else:
            print("Sorry I didn't understand that instruction. I was expecting a number(1-9), the positions on the board are numbered as follows; 1 is top left, 2 is top middle etc.")
    else:
        print("Resetting...")
        time.sleep(3)
        started = False
        row1 = "   :   :   "
        row2 = "   :   :   "
        row3 = "   :   :   "
        symbol = 'X'
        turns = 0