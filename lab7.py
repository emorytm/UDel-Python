#Ethan Clark & Emory Miller
#Lab section 21

from cisc106 import *

#PROBLEM 1

def convert_roster(fread, fcreate):
    """converts file format to replace comma with space
    parameters:
        fread: file to be read
        fcreate: file to be written
    returns: n/a
    """
    #reads files in format firstName,lastName\n and creates new file
    #...with format firstName lastName\n (doesn't need to handle improper files)
    newText=""
    fin=open(fread, "r")
    fout=open(fcreate, "w")
    for line in fin:
        line=line.replace(","," ")
        newText += line
    fout.write(newText)
    fin.close()
    fout.close()

#PROBLEM 2

def save_battle_board(lst, fname):
    """writes a file with data for load_battle_board()
    parameters:
        lst: list of lists
        fname: name of file to be written to
    returns: bool"""
    if type(lst) != list:
        return False
    if type(fname) != str:
        return False
    to_write = draw_board(lst)
    fout = open(fname, "w")
    fout.write(to_write)
    fout.close()
    return True

def load_battle_board(fname):
    """loads file and returns corresponding list of lists
    parameters:
        fname: name of file to load
    returns: a list"""
    do_close = False
    if type(fname) == str:
        fname = open(fname, "r")
        do_close = True
    loaded = []
    grid = []
    for i in fname:
        loaded.append(i.strip().split(' '))
    if do_close:
        fname.close()
    for idxA in range(len(loaded)):
        for idxB in range(len(loaded[idxA])):
            if loaded[idxA][idxB] == 'X':
                grid.append(True)
            elif loaded[idxA][idxB] == '.':
                grid.append(False)
            else:
                grid += loaded[idxA][idxB]
    return grid



class Ship:
    """model of class ship with a symbol and length
    attributes:
        symbol: a one-character string
        length: an int"""
    symbol=""
    length=0

def draw_board(grid): #each item in sub lists will be Bool or Ship
    """takes a rectangular list of lists (board) and returns representative str
    parameters:
        grid: a list of lists
    returns: a string"""
    string=""
    for idxA in range(0,len(grid)):
        for idxB in range(0,len(grid[idxA])):
            if grid[idxA][idxB] == True:
                string+="X "
            elif grid[idxA][idxB] == False:
                string+=". "
            elif type(grid[idxA][idxB]) == type(s):
                string+= grid[idxA][idxB].symbol
        string+="\n"
    return string

s=Ship()
s.symbol="B"
s.size=3

board=[[True,True,False,False],
       [s,False,False,True],
       [s,True,False,True],
       [s,False,False,False]]
board_rendering="""XX..
B..X
BX.X
B...
"""
#assertEqual(draw_board(board),board_rendering)
