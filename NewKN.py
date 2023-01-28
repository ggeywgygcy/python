def mytictactoe(val): 
    print("\n") 
    print("\t     |     |") 
    print("\t  {}  |  {}  |  {}".format(val[0], val[1], val[2])) 
    print('\t_____|_____|_____') 
  
    print("\t     |     |") 
    print("\t  {}  |  {}  |  {}".format(val[3], val[4], val[5])) 
    print('\t_____|_____|_____') 
  
    print("\t     |     |") 
  
    print("\t  {}  |  {}  |  {}".format(val[6], val[7], val[8])) 
    print("\t     |     |") 
    print("\n") 

def singlegame(curplayer): 
    val = [' ' for i in range(9)] 
       
    playerpos = {'X' : [], 'O' : []} 

while True: 
    mytictactoe(val) 
    try: 
    print("Player ", curplayer, " turn. Choose your Block : ", end="") 
    chance = int(input()) 
except ValueError: 
    print("Invalid Input!!! Try Again") 
    continue 
 
if chance < 1 or chance > 9: 
    print("Invalid Input!!! Try Again") 
    continue 
  
if val[chance - 1] != ' ': 
    print("Oops! The Place is already occupied")
    val[chance - 1] = curplayer 
  
playerpos[curplayer].append(chance)

if check_Victory(playerpos, curplayer): 
    mytictactoe(val) 
    print("Congratulations! Player ", curplayer, " has won the game!")      
    print("\n") 
    return curplayer 
      
if check_Tie(playerpos): 
    mytictactoe(val) 
    print("Oh! Game Tied") 
    print("\n") 
    return 'D' 

def check_Victory(playerpos, curplayer): 
  
    # All probable winning combinations 
    solution = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]] 
  
    # Loop to check whether any winning combination is satisfied or not 
    for i in solution: 
        if all(j in playerpos[curplayer] for j in i): 
  
            # Return True if any winning combination is satisfied 
            return True 
    # Return False if no combination is satisfied  
    return False        
  
# Defining Function to check if the game is Tied 
def check_Tie(playerpos): 
    if len(playerpos['X']) + len(playerpos['O']) == 9: 
        return True 
    return False    

    if curplayer == 'X': 
    curplayer = 'O' 
else: 
    curplayer = 'X' 

