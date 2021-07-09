#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class tick_tack_toe:
    
    def __init__(self):
        
        self.board = {'1':' ', '2':' ', '3':' ', '4':' ', '5':' ', '6':' ','7':' ','8':' ','9':' '}
        self.avail_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]     
        
    def play(self, move, player):       
        
        if move in self.avail_moves:
        
            if player == 1:

                self.board[str(move)] = 'O'                
                self.avail_moves.remove(move)
                
                
            elif player == 2:

                self.board[str(move)] = 'X'
                self.avail_moves.remove(move)
        
            #tick_tack_toe.print_board(self)
            
        else: 
           
            print('Enter a valid move')
            #tick_tack_toe.print_board(self)
            
        return self.board, self.avail_moves
            
    def print_board(self):
        
        #initialize the board        
        
        print('    |    |   ')
        print('',self.board['1'],' |',self.board['2'],' |',self.board['3'])
        print('____|____|___')
        print('    |    |  ')
        print('',self.board['4'],' |',self.board['5'],' |',self.board['6'])
        print('____|____|___')
        print('    |    |  ')
        print('',self.board['7'],' |',self.board['8'],' |',self.board['9'])
        print('    |    |  ')
        
    def check_winner(self):
    
        for i in ['X', 'O']:

            for s in [(1, 2, 3), (1, 4, 7), (7, 8, 9), (3, 6, 9), (1, 5, 9), (3, 5, 7), (2, 5, 8), (4, 5, 6)]:

                if self.board[str(s[0])] == i and self.board[str(s[1])] == i and self.board[str(s[2])] == i:
                    
                    
                    return i

                else:

                    pass
        
if __name__ == "__main__":
    
    tick_tack_toe()
    


# In[ ]:




