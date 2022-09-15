#Ethan Clark & Emory Miller
#Lab section 21

from cisc106 import *

# Problem 1

def round_list(float_list, decimals):
    """Rounds the floats in a list to a given place
    Parameters:
         float_list: a list
         decimals: integer
    Returns: None"""
    if type(float_list) != list:
        print("Error: First argument must be a list")
        return None
    if type(decimals) !=int or decimals < 0:
        print("Error: Second argument must be a positive integer")
        return None
    for idx in range(0,len(float_list)):
        if type(float_list[idx])==float:
            float_list[idx]=round(float_list[idx],decimals)
        elif type(float_list[idx])==list:
            round_list(float_list[idx],decimals)

lst0=[1.111, 2, [2.222,"a"]]
round_list(lst0,1)
assertEqual(lst0,[1.1, 2, [2.2, "a"]])
lst1=[]
round_list(lst1,1)
assertEqual(lst1,[])
lst2=[1.2345, 1.44, "1.0", 1.0]
round_list(lst2, 2)
assertEqual(lst2, [1.23, 1.44, "1.0", 1.00]) 
assertEqual(round_list(123, 1), None)#Test if first argument is a list
assertEqual(round_list(lst0, 1.1), None)#Test if second argument is an integer

# Problem 2

def word_separator(string):
    """separates string with all words run together and words specified by caps
    parameters:
        string: a string which contains only letters
    returns: a string"""
    temp=""
    if type(string) != str:
        print("Error: Argument must be a string")
        return None
    new_string=string[0]
    if not string.isalpha():
        print("Error: String must contain only letters")
        return None
    for idx in range(1,len(string)):
        if string[idx].islower():
            temp+=string[idx]
        elif string[idx].isupper():
            temp+=" "
            new_string+=temp
            temp=string[idx].lower()
    new_string+=temp
    return new_string

s_a="FourScoreAndSevenYearsAgo"
assertEqual(word_separator(s_a), "Four score and seven years ago")
assertEqual(word_separator("OneTwothreeFour"), "One twothree four")
assertEqual(word_separator("12345"), None)
assertEqual(word_separator(12345), None)
assertEqual(word_separator("OneTwo3Four"), None)

# Problem 3

def addDigits(string):
    """sums digits in string of integers
    parameters:
        string: a string of only integers
    returns:
        integer"""
    total=0
    if type(string) != str:
        print("Error: Argument must be a string")
        return None
    if not string.isnumeric():
        print("Error: String must contain only numbers")
        return None
    for idx in range(0,len(string)):
        total+=int(string[idx])
    return total

assertEqual(addDigits("abcd"), None)
assertEqual(addDigits("123ab"), None)
assertEqual(addDigits("1.1234"), None)
assertEqual(addDigits("0123"), 6)

# Problem 4

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
                string+="X"
            elif grid[idxA][idxB] == False:
                string+="."
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
assertEqual(draw_board(board),board_rendering)

board0=[[False,False,False,False],
       [False,False,False,False],
       [False,False,False,False],
       [False,False,False,False]]
board_rendering0="""....
....
....
....
"""
assertEqual(draw_board(board0),board_rendering0)

board1=[[s,s,s,s],
       [False,False,False,False],
       [False,False,False,False],
       [False,False,False,False]]
board_rendering1="""BBBB
....
....
....
"""
assertEqual(draw_board(board1),board_rendering1)

board3=[[True,True,True,True],
       [True,True,True,True],
       [True,True,True,True],
       [True,True,True,True]]
board_rendering3="""XXXX
XXXX
XXXX
XXXX
"""
assertEqual(draw_board(board3),board_rendering3)

board4=[[s,True,True],
       [True,s,True],
       [True,True,s]]
board_rendering4="""BXX
XBX
XXB
"""
assertEqual(draw_board(board4),board_rendering4)

board5=[]
board_rendering5=""""""
assertEqual(draw_board(board5),board_rendering5)

# Problem 5

def validPassword(string):
    """Takes a password(string) as an argument, and checks that it is at least
    7 characters long, contains at least one uppercase letter, one lowercase
    letter, one numeric digit, and one special character.
    parameters:
        string: a string
    returns:
        bool"""
    if type(string) != str:
        print("Error: Password must be a string")
        return False
    if len(string) < 7 or len(string) > 15:
        print("Error: Password must be between 7 and 15 characters long")
        return False
    check=0
    for idx in range(len(string)):
        if string[idx].isupper():
            check +=1
    if check < 1:
        print("Error: Password must contain at least one uppercase letter")
        return False
    check=0
    for idx in range(len(string)):
        if string[idx].islower():
            check += 1
    if check < 1:
        print("Error: Password must contain at least one lowercase letter")
        return False
    check=0
    for idx in range(len(string)):
        if string[idx].isnumeric():
            check +=1
    if check < 1:
        print("Error: Password must contain at least one number")
        return False
    check=0
    chars = ["!","@","#","$","%","^","&","*"]
    for idx in range(len(string)):
        if string[idx] in chars:
            check +=1
    if check < 1:
        print("Error: Password must contain at least one special character",
              "in set {! @ # $ % ^ & *}")
        return False
    else:
        return True

assertEqual(validPassword("a"),False)
assertEqual(validPassword("aaaaaaa"),False)
assertEqual(validPassword("aaaaAAA"),False)
assertEqual(validPassword("aaaaAAA777"),False)
assertEqual(validPassword("aaaAA777!!"),True)
