

#Ethan Clark & Emory Miller
#lab section 21

from cisc106 import *
import random

class Ship:
    """model of a ship
    attributes:
        length: an int
        name: a string
        symbol: a string"""
    length=0
    name=""
    symbol=""

class Coordinate:
    """model of a coordinate
    attributes:
        x: the x coordinate, an int
        y: the y coordinate, an int
        direction: the orientation of the ship (x or y), a string"""
    x=0
    y=0
    direction=""


class Board:
    """model of the grid or "battle board" used by each player
    attributes:
        layout: a dictionary"""
    layout={}

class CBoard:
    """model of the grid or "battle board" used by the computer
    attributes:
       layout: a dictionary"""
    layout={}

def main():
    """runs the program
    returns: n/a"""

    """Creates game board for the player and computer"""
    board = Board()
    for i in range(100):
        board.layout[i]=False
    cboard= CBoard()
    for i in range(100):
        cboard.layout[i]=False

    print("Welcome to Battleship!\nYou'll first be asked to palce your ships, and then you'll be asked to place shots until you or the computer loses.")

    """Asks the player for coordinates to place ships"""
    display_board(board)
    ship_list=load_ships()
    count = int(ship_list[0])
    ship_list=ship_list[1:]
    while count > 0:
        s=make_ship(ship_list[:3])
        ship_info(ship_list[:3])
        ship_list=ship_list[3:]
        c=get_player_coord()
        a=legal_placement(c, board, s, True) #Set to true to diplay error messages
        while a == False:
            c=get_player_coord()
            a=legal_placement(c, board, s, True)
        place_ship_on_board(s, board, c)
        display_board(board)
        count-=1

    """Generates a board with ships on it for the computer"""
    ship_list=load_ships()
    count = int(ship_list[0])
    ship_list=ship_list[1:]
    while count > 0:
        s=make_ship(ship_list[:3])
        ship_list=ship_list[3:]
        c=make_random_coordinate()
        a=legal_placement(c, cboard, s)
        while a == False:
            c=make_random_coordinate()
            a=legal_placement(c, cboard, s)
        place_ship_on_board(s, cboard, c)
        count-=1

    b=fleet_status(board)
    c=fleet_status(cboard)

    """Meat and Potatoes, this is where functions are called to play the
    actual game"""
    while b and c:
        
        print("Computer Board:")
        display_board(cboard, True)# Change from true to false to enable cheat mode
        player_strike(cboard)
        c=fleet_status(cboard)
        
        computer_strike(board)
        print("Your board:")
        display_board(board)
        b=fleet_status(board)

    if c:
        print("You lose! :(")
        return
    else:
        print("You win! :)")
        return
    

def load_ships(fread = "ships.txt"):
    """loads ships from text file and returns list with ship values
    parameters:
        filename: the name of the file containing ship attributes, a string
    returns:
        a list cointaining ship lenghts, symbols, names"""
    ship_list = []
    fin=open(fread, "r")
    for line in fin:
        ship_list.append(line.rstrip())
    fin.close()
    return ship_list
    
def make_ship(ship_list): 
    """creates an instance of class ship from list of strings
    parameters:
        ship_info: a list of strings
    returns:
        instance of class Ship"""
    new=Ship()
    new.length=int(ship_list[2])
    new.name=ship_list[0]
    new.symbol=ship_list[1]
    return new

def ship_info(ship_list):
    """informs the player of what ship they are playing
    parameters: an instance of class Ship
    returns: none"""
    print("Place", ship_list[0], "(length ", ship_list[2]+") at which coordinate and orientation?")

def make_random_coordinate():
    """creates instance of class Coordinate at given x, y location
    parameters:
        x: the x coordinate, an int
        y: the y coordinate, an int
        direction: the direction that the ship lays onthe board, x or y (str)
    returns:
        instance of class Coordinate"""
    c=Coordinate()
    c.x=random.randint(0,9)
    c.y=random.randint(0,9)
    temp=random.randint(0,1)
    if temp in [0]:
        c.direction="x"
    else:
        c.direction="y"
    return c

def display_board(Board, hide_unhit=False):
    """prints board with all assocaited values and symbols
    parameters:
        Board: an instance of class Board
    returns: none"""
    print(" ABCDEFGHIJ")
    for idxA in range(10):
        temp=""
        for idxB in range(10):
            if Board.layout[10*idxA+idxB]:
                if hide_unhit:
                    if Board.layout[10*idxA+idxB].isupper():
                        if Board.layout[10*idxA+idxB] not in ["X"]:
                            temp+="."
                        else:
                            temp+=Board.layout[10*idxA+idxB]
                    else:
                        temp+=Board.layout[10*idxA+idxB]
                else:
                    temp+=Board.layout[10*idxA+idxB]            
            else:
                temp+="."
        print(str(idxA)+temp)

def get_player_coord(): #x is in int, not a letter
   """Creates an instance of class coord, which is specified by the player
   parameters:
   returns: coord, an instance of class Coord"""
   poss=["a","b","c","d","e","f","g","h","i","j"]
   ok=1
   while ok>0:
       init=input("Please enter a coordinate in the form 'b7x': ")
       if len(init)==3:
           if init[0].isalpha():
               if init[0] in poss:
                   if init[2].isalpha():
                       if init[2] in ["x","y"]:
                           if init[1].isdigit():
                               if 0 <= int(init[1]) < 10:
                                   ok=0
   new=Coordinate()
   new.x=poss.index(init[0])
   new.y=int(init[1])
   new.direction=init[2]
   return new
    
 
def place_ship_on_board(ship, Board, Coordinate):
   """places values of ship on board at Coordinate
   parameters:
       Ship: an instance of class Ship
       Board: an instance of class Board
       Coordinate: an instance of class Coordinate
   returns: None"""
   if Coordinate.direction in ["x"]:
       for idx in range(ship.length):
           Board.layout[Coordinate.y*10+(Coordinate.x+idx)]=ship.symbol
   elif Coordinate.direction in ["y"]:
       for idx in range(ship.length):
           Board.layout[(Coordinate.y+idx)*10+Coordinate.x]=ship.symbol
           
def is_hit(board, place):
    """Determines whether a ship was hit or not, and displays what type of ship
    parameters: board, an instance of class Board
                place, an int
    returns: a string"""
    ship_list=load_ships()
    count = int(ship_list[0])
    ship_list=ship_list[1:]
    ship_symbol = str(board.layout[place])
    while count > 0:
        if str(ship_list[1]) == ship_symbol:
            return ship_list[0]
        ship_list=ship_list[3:]
        count-=1

def is_sunk(board, place): ## Can't get this one to work... 
    """determines whether a ship is sunk or not
    parameters: board, an instance of class Board
                place, an int
    returns: a string"""
    ship_list=load_ships()
    count = int(ship_list[0])
    ship_count = 1
    ship_length = 0
    ship_list=ship_list[1:]
    ship_symbol=str(board.layout[place])
    while count > 0:
        if str(ship_list[1]) == ship_symbol:
            ship_length = int(ship_list[2])
            ship_symbol=ship_symbol.lower()
            count = 0
        ship_list=ship_list[3:]
        count-=1
    if ship_count < ship_length:
        for i in range(ship_length):
            for idx in range(100):
                if board.layout[idx]:
                    if board.layout[idx].isalpha():    
                        if str(board.layout[idx]) == str(ship_symbol):
                            ship_count += 1
    if ship_count == ship_length:
        return ship_list[0]


def player_strike(computer_board):
    """asks player for a coordinate and responds, modifies board accordingly.
    parameters: computer_board: an instance of class Board
    returns: bool"""
    inp=input_coordinate()
    poss=["a","b","c","d","e","f","g","h","i","j"]
    place=(10*int(inp[1])+poss.index(inp[0]))
    if computer_board.layout[place]:
        if computer_board.layout[place].isupper():

            if computer_board.layout[place] not in ["X"]:
                print("\nYou hit their", is_hit(computer_board, place)+"!")
                computer_board.layout[place]=computer_board.layout[place].lower()
                return True
            else:
                print("\nMiss!\n")
                computer_board.layout[place]="X"
                return False
        else:
            print("\nMiss!\n")
            computer_board.layout[place]="X"
            return False
    else:
        print("\nMiss!\n")
        computer_board.layout[place]="X"
        return False

def input_coordinate():
    """asks player for location at which to shoot
    parameters: none
    returns: 2-character string"""
    poss=["a","b","c","d","e","f","g","h","i","j"]
    check=1
    while check>0:
        inp=input("Enter shot in the form of 'a7':  ")
        if len(inp) == 2:
            if inp[0].isalpha():
                if inp[0] in poss:
                    if inp[1].isdigit():
                        if int(inp[1]) in [0,1,2,3,4,5,6,7,8,9]:
                            check=0
    return inp
    

def computer_strike(player_board):
    """generates random strike coordinate for computer
    parameters: player_board: an instance of class Board
    returns: bool"""
    place=random.randint(0,99)
    if player_board.layout[place]:
        if player_board.layout[place].isupper():
            if player_board.layout[place] not in ["X"]:
                print("\nThe other player hit your", is_hit(player_board, place)+"!")
                player_board.layout[place]=player_board.layout[place].lower()
                return True
            else:
                print("\nComputer missed!\n")
                player_board.layout[place]="X"
                return False
        else:
            print("\nComputer missed!\n")
            player_board.layout[place]="X"
            return False
    else:
        print("\nComputer missed!\n")
        player_board.layout[place]="X"
        return False

       
def legal_placement(coord, board, ship, hide=False):
    """Determines whether a given ship can be placed at a coordinate
    parameters: coord, an instance of class Coord; board, an instance of class Board,
    ship, an instance of class ship
    returns:bool"""
    if coord.direction in ["x"]:
        if (coord.x + ship.length -1) > 9:
            if hide:
                print("Error: placement puts ship off board")
                return False
            return False
        for idx in range(ship.length):
            if board.layout[coord.y*10+(coord.x+idx)]:
                if hide:
                    print("Error: place intersects other ship")
                    return False
                return False
    elif coord.direction in ["y"]:
        if (coord.y + ship.length -1) > 9:
           if hide:
               print("Error: placement puts ship off board")
               return False
           return False
        for idx in range(ship.length):
           if board.layout[(coord.y+idx)*10+coord.x]:
               if hide:
                   print("Error: place intersects other ship")
                   return False
               return False   
    else:
       return True

def fleet_status(board):
    """Checks whether a fleet has been sunk or not
    parameters:board, an instance of class Board
    returns: True if there are ships left
            None if there are no ships left"""
    for idx in range(100):
        if board.layout[idx]:
            if board.layout[idx].isalpha():
                if board.layout[idx].isupper():
                    if board.layout[idx] != "X":
                        return True
    return False

main()
