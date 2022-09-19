# Tictac game

playerX = "X" 
playerO = "O"  
drawi = ""  
    
t = ["","","","","","","","",""] #array to control grid output and input

def display_board(): #function to diplay board
    print("Welcome to the TIC TAC TOE!\n")
    
    print("TIC TAC TOE")
    print("*********************")
    print(f"* {t[0]}     |   {t[1]}  |   {t[2]}  ")
    print(f"* ----------------- *")
    print(f"* {t[3]}     |   {t[4]}  |   {t[5]}  ")
    print(f"* ----------------- *")
    print(f"* {t[6]}     |   {t[7]}  |   {t[8]}  ")
    print(f"* ----------------- *")
    print("*********************")
    
    

def player_input(player): #Function to take user input and assign mark to grid 
        play = int(input("Enter any value btw 0-9\n")) #index to add mark
        if play >=0 and play<=8 and t[play] == "": # is index of user in range and is index on grid empty?
            t[play] = player #mark assign to the index (X or O )
        else:
            print("Position occupied")
        
def check_horizontal(): #determine if rows are filled with same marks (O or X)
    if t[0] == t[1] == t[2] == "X" or t[3] == t[4] == t[5] == "X" or t[6] == t[7] == t[8] == "X":
        print("PlayerX won the game")
        return True
    elif t[0] == t[1] == t[2] == "O" or t[3] == t[4] == t[5] == "O" or t[6] == t[7] == t[8] == "O":
        print("PlayerO won the game")
        return True

def check_vertical(): #determine if columns are filled with same marks (O or X)
    if t[0] == t[3] == t[6] == "X" or t[1] == t[4] == t[7] =="X" or t[2] == t[5] == t[8] == "X" :
        print("PlayerX wins")
        return True
    elif t[0] == t[3] == t[6] == "O" or t[1] == t[4] == t[7] =="O" or t[2] == t[5] == t[8] == "O" :
        print("PlayerO wins")
        return True 
    
def diagonal(): #determine if diagonals are filled with same marks (O or X)
    if t[0] == t[4] == t[8] == "X" or t[2] == t[4] == t[6] == "X":
        print("PlayerX wins")
        return True
    elif t[0] == t[4] == t[8] == "O" or t[2] == t[4] == t[6] == "O":
        print("PlayerO wins")
        return True


def check_Win(): # Function to determine winner
    check_horizontal()
    check_vertical()
    diagonal()
    
def start(): # Function to start the game
    display_board()
    
    for r in range(0,10):
        if r >= 5:
            if check_Win():
                break
        if r == 9:
            print("draw")
            break
        if r%2 == 0:
            player_input(playerX)
            display_board()
        else:
            player_input(playerO)
            display_board()  
start()



  
    
    
    




    
    
    

        
    
    
        
        
    


    
    
