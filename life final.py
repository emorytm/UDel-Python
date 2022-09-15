#Ethan Clarke & Emory Miller
#lab section 21

# Conway's life in Python

import random
from cisc106 import *

class Grid():
    """A class to be used to modify a list of lists with object methods
    attribute: a list of lists"""
    lists=[]
    
    def copy(self):
        """Make a copy of a grid.
        Returns: a list of lists"""
        copy = Grid()
        copy.lists=[]
        for row in self.lists:
            copy.lists.append(row[:])
        return copy
    
    def to_string(self):
        """Generate a string representation of a grid
        of bools.
        Returns: a string representation"""
        ret = "+"+"-"*len(self.lists)+"+\n"
        for row in self.lists:
            ret += "|"
            for cell in row:
                if cell:
                    ret += "X"
                else:
                    ret += " "
            ret += "|\n"
        ret += "+"+"-"*len(self.lists)+"+\n"
        return ret
    
    def value(self,i,j):
        """Returns the value of a grid coordinate
        with appropriate boundary conditions.
        Parameters: i,j, ints, the coordinates of interest
        Returns: bool"""
        if i<0:
            i=len(self.lists)-1
        elif i>=len(self.lists):
            i=0
        if j<0:
            j=len(self.lists)-1
        elif j>=len(self.lists):
            j=0
        return self.lists[i][j]
    
    def count_adjacent(self,i,j):
        """Count the number of living cells adjacent
        to a grid coordinate (not including the coord
        itself)
        Parameters: i,j, ints, the coordinates of interest
        Returns: int"""
        count = 0
        for i0 in [i-1,i,i+1]:
            for j0 in [j-1,j,j+1]:
                if self.value(i0,j0):
                    count += 1
        if self.value(i,j):
            count -= 1
        return count
    
    def step(self):
        """Update one iteration of Conway's game of life
        Returns: None"""
        copy=self.copy()
        for i in range(len(self.lists)):
            for j in range(len(self.lists)):
                neighbors = self.count_adjacent(i,j)
                if self.lists[i][j]:
                    if neighbors<2 or neighbors>3:
                        self.lists[i][j]=False
                elif neighbors==3:
                     self.lists[i][j] = True
                     
    def save(self, fname):
        """writes string conversion of grid to fname"""
        if type(fname) != str:
            return False
        fout = open(fname, "w")
        fout.write(self.to_string())
        fout.close()
        return True
        
    def load(self, inf): 
        """loads values from converted string from inf to self.lists
        parameters: inf: a string
        returns: none"""
        if type(inf) != str:
            return False
        temp=open(inf,"r")
        inf=temp.read()
        temp.close()
        temp=[[]]
        i=-1
        for idx in range(len(inf)):
            if inf[idx] in ["\n"]:
                i+=1
                if i>-1:
                    temp.append([])
            elif inf[idx] in [" "]:
                temp[i].append(False)
            elif inf[idx] in ["X"]:
                temp[i].append(True)
        check=3
        while check>0:
            if temp[-1] in [[]]:
                temp.pop()
                check-=1
        self.lists=temp
        return True

def generate_grid(size):
    """Create a 2-d square grid of bools (all False)
    Parameter: size, int, the size of grid
               grid, an instance of class Grid, a list 
    Returns: a list of lists"""
    grid=Grid()
    grid.lists=[]
    for i in [0]*size:
        grid.lists.append([False]*size)
    return grid

def random_grid(size):
    """Create a 2-d square grid of bools filled
    randomly with True or False.
    Parameter: size, int, the size of the grid
               grid, list, an instance of class Grid.
    Returns: a list of lists"""
    grid=generate_grid(size)
    for row in grid.lists:
        for idx in range(size):
            if random.randint(0,1)==1:
                row[idx]=True
    return grid

def main():
    g=random_grid(20)
    while True:
        print(g.to_string())
        g.step()

k=random_grid(3)
