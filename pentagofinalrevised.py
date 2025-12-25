import numpy as np
import random


def display_board(board):
    print(board,"\n")
    
def check_victory(board,turn,rot):
    
    #Check Victory -> 0 = before rotation, 1 = after rotation
    for i in range (2):
        if i == 0 :
            if rot == 1: board[0:3,3:6] = np.rot90(board[0:3,3:6], 1)
            elif rot == 2: board[0:3,3:6] = np.rot90(board[0:3,3:6], -1)
            elif rot == 3: board[3:6,3:6] = np.rot90(board[3:6,3:6], 1)
            elif rot == 4: board[3:6,3:6] = np.rot90(board[3:6,3:6], -1)
            elif rot == 5: board[3:6,0:3] = np.rot90(board[3:6,0:3], 1)
            elif rot == 6: board[3:6,0:3] = np.rot90(board[3:6,0:3], -1)
            elif rot == 7: board[0:3,0:3] = np.rot90(board[0:3,0:3], 1)
            elif rot == 8: board[0:3,0:3] = np.rot90(board[0:3,0:3], -1)
        else :
            if rot == 1: board[0:3,3:6] = np.rot90(board[0:3,3:6], -1)
            elif rot == 2: board[0:3,3:6] = np.rot90(board[0:3,3:6], 1)
            elif rot == 3: board[3:6,3:6] = np.rot90(board[3:6,3:6], -1)
            elif rot == 4: board[3:6,3:6] = np.rot90(board[3:6,3:6], 1)
            elif rot == 5: board[3:6,0:3] = np.rot90(board[3:6,0:3], -1)
            elif rot == 6: board[3:6,0:3] = np.rot90(board[3:6,0:3], 1)
            elif rot == 7: board[0:3,0:3] = np.rot90(board[0:3,0:3], -1)
            elif rot == 8: board[0:3,0:3] = np.rot90(board[0:3,0:3], 1)
            
        '''
        Victory Status
        - 0 if no winning/draw situation is present for this game
        – 1 if player 1 wins
        – 2 if player 2 wins
        – 3 if it is a draw
        '''
        Victory = 0 #initialize Winner indicator
        # Check Horizontal
        for row in range(6):
            strboard = ""
            for col in range (6):
                strboard += str(board[row,col])
            if '11111' in strboard : 
                Victory = 1 if Victory == 0 else 3
            elif '22222' in strboard : 
                Victory = 2 if Victory == 0 else 3
            if Victory == 3: break 
                     
        # Check Vertical if Victory = 0
        if Victory != 3:
            for row in range(6):
                strboard = ""
                for col in range (6):
                    strboard += str(board[col,row])
                if '11111' in strboard : 
                    Victory = 1 if Victory == 0 else 3
                elif '22222' in strboard : 
                    Victory = 2 if Victory == 0 else 3
                if Victory == 3: break
        
        # Check Diagonal if Victory = 0
        if Victory != 3:
            strboard1 = strboard2 = strboard3 = strboard4 = strboard5 = strboard6 = ""
            for x in range(6): 
                strboard1 += str(board[x,x])
                strboard2 += str(board[x,5-x])
            for x in range(5):
                strboard3 += str(board[x+1,x])
                strboard4 += str(board[x,x+1])
                strboard5 += str(board[x,4-x])
                strboard6 += str(board[x+1,5-x])
        
            strboards = [strboard1, strboard2, strboard3, strboard4, strboard5, strboard6]
            if any('11111' in strboard for strboard in strboards):
                Victory = 1 if Victory == 0 else 3
            elif any('22222' in strboard for strboard in strboards):
                Victory = 2 if Victory == 0 else 3
            
        #Check if Board Full When Victory = 0
        if Victory == 0:
            strboard = ""
            for row in range(6):
                for col in range(6):
                    strboard += str(board[row,col])
            if i == 1 and "0" not in strboard: Victory = 3
        
        if Victory != 0:
            return Victory
               
    #return to Victory Status
    return Victory
        
def apply_move(board,turn,row,col,rot):
    board_out = board.copy()
    board_out[row,col]=turn
    if rot == 1: board_out[0:3,3:6] = np.rot90(board_out[0:3,3:6], -1)
    elif rot == 2: board_out[0:3,3:6] = np.rot90(board_out[0:3,3:6], 1)
    elif rot == 3: board_out[3:6,3:6] = np.rot90(board_out[3:6,3:6], -1)
    elif rot == 4: board_out[3:6,3:6] = np.rot90(board_out[3:6,3:6], 1)
    elif rot == 5: board_out[3:6,0:3] = np.rot90(board_out[3:6,0:3], -1)
    elif rot == 6: board_out[3:6,0:3] = np.rot90(board_out[3:6,0:3], 1)
    elif rot == 7: board_out[0:3,0:3] = np.rot90(board_out[0:3,0:3], -1)
    elif rot == 8: board_out[0:3,0:3] = np.rot90(board_out[0:3,0:3], 1)
    return board_out
    
def check_move(board,row,col):    
    return board[row, col] == 0
    
def computer_move(board,turn,level):
    if turn == 1:
        turn_opp = 2 
    else:
        turn_opp = 1 
        
    if level == 1:
        while True:
            row = random.randint(0,5)
            col = random.randint(0,5)
            rot = random.randint(1,8)
            if check_move(board,row,col) == True: break
           
    elif level == 2:
        computer_win = False
        player_win = False

        # Check the possibilty for the computer to win.
        for row in range(6):
            for col in range(6):
                for rot in range(1, 9):
                    board_temp = np.copy(board)
                    if check_move(board_temp,row,col):
                        board_temp = apply_move(board_temp,turn,row,col,rot)
                        if check_victory(board_temp,turn, rot) == turn:
                            computer_win = True
                            row_comp, col_comp, rot_comp = row, col, rot
                            break

        # If computer move not possible to win then check the possibilty of movement that the player can win.
        if computer_win == False:
            for row in range(6):
                for col in range(6):
                    for rot in range(1, 9):
                        board_temp = np.copy(board)
                        if check_move(board_temp,row,col):
                            board_temp = apply_move(board_temp,turn_opp,row,col,rot)
                            if check_victory(board_temp, turn_opp, rot) == turn_opp:
                                player_win = True
                                row_player, col_player, rot_player = row, col, rot
                                break
                  
        # If the computer can win, make the winning move else if player can win then block the winning move. Otherwise, make a valid random move.
        if computer_win: row, col, rot = row_comp, col_comp,  rot_comp
        elif player_win : row, col, rot = row_player, col_player, rot_player
        else:
            while True:
                row = random.randint(0,5)
                col = random.randint(0,5)
                rot = random.randint(1,8)
                if check_move(board,row,col) == True: break
            
    return (row,col,rot)

def menu():  
    game_board = np.zeros((6, 6),dtype=int)
    player = turn =  rot = 0
    
    print("<PS0001 Computational Thinking - AY 2023/2024>")
    print("--- Welcome to PENTAGO ---\n")    
    #Validate Players Type
    while True:
        player_type = input("Choose type of the two players (human or computer) ? : ").upper()
        if player_type == "HUMAN" : break
        if player_type == "COMPUTER" :
            while True:
                level = input("Input Level (1-2) : ")
                if level.isdigit():
                    level = int(level)
                    if level not in range(1,3): print("Level Should Between 1 - 2!")
                    else : break
                else: print("Level Should Be Number!")
            break

    #Player 1 : human, Player 2: human/computer
    while check_victory(game_board,turn,rot) == 0:
            
        #Switch turn Player 1 or 2 
        turn=player%2+1
            
        if turn == 2 and player_type == "COMPUTER" : 
            print("-> Player : Computer")
        else :
            print("-> Player : ", turn)
                
        #check if the human move is valid and apply it only if it is indeed a valid move.
        if turn == 2 and player_type == "COMPUTER":
            row, col, rot = computer_move(game_board, turn, level)
            print("Input Row Index (0-5)      : ",row)
            print("Input Column Index (0-5)   : ",col)
            print("Input Rotation Index (1-8) : ",rot)
        else:
            while True:               
                #move from a player can be described by a row index (integer between 0 and 5), a column index (integer between 0 and 5) and a rotation index (integer between 1 and 8) 
                while True:
                    row = input("Input Row Index (0-5)      : ")
                    if row.isdigit():
                        row = int(row)
                        if row not in range(6): print("Row Index Should Between 0 - 5!")
                        else : break
                    else : print("Row Index Should Be Number!")
                            
                while True:
                    col = input("Input Column Index (0-5)   : ")
                    if col.isdigit() :
                        col = int(col)
                        if col not in range(6): print("Column Index Should Between 0 - 5!")
                        else : break
                    else : print("Column Index Should Be Number!")
                       
                while True:
                    rot = input("Input Rotation Index (1-8) : ")
                    if rot.isdigit() : 
                        rot = int(rot)
                        if rot not in range(1,9): print("Ratation Index Should Between 1 - 8!")
                        else : break
                    else : print("Ratation Index Should Be Number!")
                
                if check_move(game_board,row,col) == True: break
            
        player +=1
        game_board= apply_move(game_board,turn,row,col,rot)
        check_victory(game_board,turn,rot)           
        display_board(game_board)
                                
        if check_victory(game_board,turn,rot) == 1:
            print("Player 1 Wins!")
            break
                    
        if check_victory(game_board,turn,rot) == 2:
            if player_type == "COMPUTER" : 
                print("Computer Wins!")
            else :
                print("Player 2 Wins!")
            break
                
        if check_victory(game_board,turn,rot) == 3:
            print("It's a draw!")
            break
        
if __name__ == "__main__":
   menu()
   # # dummy_board = [[1 2 0 0 1 1]
   # #                [1 1 0 2 2 2]
   # #                [1 0 0 2 1 1]
   # #                [0 2 1 2 0 0]
   # #                [2 0 1 2 2 1]
   # #                [1 1 2 2 0 0]]
   # dummy_board = ([[1,2,0,0,1,1],
   #                [1,1,0,2,2,2],
   #                [1,0,0,2,1,1],
   #                [0,2,1,2,0,0],
   #                [2,0,1,2,2,1],
   #                [1,1,2,2,0,0]])
   # print(check_victory(dummy_board,1,3))



    




    