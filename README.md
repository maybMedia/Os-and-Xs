# Noughts and Crosses

## Process
1. I began by creating a simple board and storing it in four variables; row1, row2, row3 and break1.
2. I then created a simple loop to check if the game is in progress or ready to start which also included some instructions.
3. I then created a loop which printed the board and who's turn it is to the console each turn and requested an input from the user. This input is then interpreted and a row and column is given to the value.
4. I then created a function which checks if there is already a symbol in that row and column. I feel like I have not elegantly implemented this function as it uses 3 if statements to determine the row to check.
5. Then I created a function which if the row and column are empty, replaces the blank space with the symbol of the current player.

## Screenshots


## Tools Used


## Skills learnt or improved
- I became more comfortable with using functions.
- I improved my understanding of converting strings to lists and joining them back together.

## Challenges
- I really struggled with coming up with a method to check whether the position was filled or not. I solved this by using a dictionary with a value for the position and then the index which matched that in the split up string.