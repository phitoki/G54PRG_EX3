#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 14:33:22 2018

@author: Philipp Kirschthaler

student ID: 2001532821

Nicolai

"""



#create a global variable that determines the size of a board
global h
h = 8


#we create a board in the size of h
board = [[0 for i in range(h)] for j in range(h)]

def print_board() :
    #print a board where 0 becomes "." and 1 becomes "Q"
    for line in board :
        for square in line :
            if square == 0 :
                print(".",end=" ")
            else :
                print("Q",end=" ")
        print()
        



def is_safe(i, j) :
    
    for s in range(0, h) :
        # does the queen n appear in the same column or row?
        if board[i][s] == 1 or board[s][j] == 1:
                return False
    for s in range(0, h) :
        for r in range(0, h) :
            #check for the diagnoals left top, right top, lower left and lower right 
            if (s+r==i+j) or (s-r==i-j):
                #if there is a 1 it is not safe 
                if board[s][r]==1:
                    return False
    return True
             




def solve(n) :  # n is the amount of Queens on the board
    #if n equals 0 no Queen can be placed anmyore
   
    if n == 0 :
        #and we print the board
        print_board()
        input("More?")
        
    
        
    
    else :
        for i in range(n-1, n):
            for j in range(0, h):
                    # i and j get put into the is_safe iteratively  
                 
                
                if (is_safe(i, j) and (board[i][j]!=1)) :
                    board[i][j] = 1
                      
                    # when a queen is placed only n-1 queen can be put on the board
                    
                            
                    if solve(n-1) == True:
                        return True
                            
                     
                    #we use backtracking to replace the Qs with 0 and try another solution
                    board[i][j] = 0
                    
                    
                    
        return False              
    

# for n we put h into because the size of the board is the same than the amount of queens
solve(h)








        
    
