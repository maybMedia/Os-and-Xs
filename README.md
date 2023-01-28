# Noughts and Crosses

## Process
1. I began by creating a simple board and storing it in four variables; row1, row2, row3 and break1.
2. I then created a simple loop to check if the game is in progress or ready to start which also included some instructions.
3. I then created a loop which printed the board and who's turn it is to the console each turn and requested an input from the user. This input is then interpreted and a row and column is given to the value.
4. I then created a function which checks if there is already a symbol in that row and column. I feel like I have not elegantly implemented this function as it uses 3 if statements to determine the row to check.
5. Then I created a function which if the row and column are empty, replaces the blank space with the symbol of the current player.

## Screenshots
![Inefficient function which detects if there is a win.](./screenshots/InefficientFunction.png)
![Another unelegant solution to update rows, similar method used to check for empty positions](./screenshots/UpdateRowFunction.png)

## Tools Used
- [RealPython - Used for the idea though did not use any of the source code etc.](https://realpython.com/tic-tac-toe-python/#step-2-set-up-the-tic-tac-toe-game-logic-in-python)

## Skills learnt or improved
- I became more comfortable with using functions.
- I improved my understanding of converting strings to lists and joining them back together.

## Challenges
- I really struggled with coming up with a method to check whether the position was filled or not. I solved this by using a dictionary with a value for the position and then the index which matched that in the split up string.
- The method in which it detects a win is extremely unelegant but the way I created the board made it very difficult to have the program interpret the position of pieces in a simple way. 
- Repeat a few lines of code which I couldn't figure out how to convert to a function. I.e. needs to modify a variable etc.