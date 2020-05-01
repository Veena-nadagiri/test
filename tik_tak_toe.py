#!/usr/bin/env python
# coding: utf-8

# In[40]:


from IPython.display import clear_output

def display_board(board):
    clear_output()
    
    print(board[7]+'_|_'+board[8]+"_|_"+board[9])
    print(board[6]+"_|_"+board[5]+"_|_"+board[4])
    print(board[1]+"_|_"+board[2]+"_|_"+board[3])
    


# In[41]:


test_board = ['o', 'x','o','x','o','x','o','x','x','x']
display_board(test_board)


# In[42]:


def player_name():
    '''
    output = (player1_marker,player2_marker)
    
    '''
    marker =" "
    while not ( marker == 'x' or marker == 'o'):
        marker = input("player1 : choose x or o : ").upper()
        
        if marker == 'x'or 'X':
            return ('x','o')
        else:
            return ('o','x')
            


# In[9]:


player1_marker,player2_marker = player_name()


# In[10]:


player2_marker


# In[11]:



def place_marker(board,marker,position):
    board[position] = marker
    


# In[12]:


test_board


# In[14]:


place_marker(test_board,'x',0)


# In[16]:


display_board(test_board) 


# In[17]:


def win_check(board,mark):
    return(board[7] == mark and board[8] ==mark and board[9]==mark or
    board[5] == mark and board[4] == mark and board[6] == mark or
    board[1] == mark and board[2] == mark and board[3] == mark or
    board[7] == mark and board[4] == mark and board[1] == mark or
    board[8] == mark and board[5] == mark and board[2] == mark or
    board[9] == mark and board[6] == mark and board[3] == mark or
    board[7] == mark and board[5] == mark and board[3] == mark or
    board[9] == mark and board[5] == mark and board[1] == mark )            


# In[19]:


display_board(test_board)
win_check(test_board,'x')


# In[20]:


import random
def random_choose():
    if random.randint(0,1)==0:
        return 'player1'
    else:
        return 'player2'


# In[21]:


def free_space(board,position):
    return board[position] == ' '  #returns false when board is full
    


# In[22]:


def full_board_check(board):
    for i in range(1,10):
        
        if free_space(board,i): # its true when theres a free space
            return False       # thers still space on the board
    
    return True


# In[32]:


print([i for i in range(1,9)])


# In[33]:


def ask_position(board):
    position = 0
    while position not in range(1,10) and not free_space(test_board,position):
        position = int(input("choose the position between (1-9) :"))
    return position    


# In[34]:


def replay():
    choice = input("play again:? enter yes or no ")
    return choice == 'yes'


# In[35]:


print("hello welcome to tik tak toe ...!!!")


# In[38]:



while True:
    the_board=[' ']*10
    player1_marker,player2_marker =  player_name()
    turn =  random_choose()
    print(turn + 'will go first')
    play_game = input('ready to play game? yes or no')
    if play_game == 'yes':
        game_on = True
        
    else:
        game_on = False
        
    while game_on:
        if turn =='player1':
            display_board(the_board)
            position = ask_position(the_board)
            place_marker(the_board,player1_marker,position)
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('player 1 has won ....!')
                game_on = False
                
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('oooops game is tie')
                    game_on = False
                else:
                    turn = 'player2'
                    
                
        
        else:
            display_board(the_board)
            position = ask_position(the_board)
            place_marker(the_board,player2_marker,position)
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('player 2 has won ....!')
                game_on = False
                
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('oooops game is tie')
                    game_on = False
                else:
                    turn = 'player1'
                    
    
    
    
    
    
    
    if not replay():
        break
            


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




