#Ethan Clark & Emory Miller
#lab section 21

from cisc106 import *

class Quadratic:
    """model of a quadratic expression (a*x**2+b*x+c)"""
    a=0
    b=0
    c=0
    
    def evaluate(self,num):
        """returns a float or list that's value of quad. expression at num
    parameters: num: a number or list of numbers
    returns: float"""
        if type(num)!=int:
            if type(num)!=float:
                if type(num) !=list:
                    print('error: ', num, ' is not a number or list')
                    return None
                for idx in num:
                    if type(idx)!=int:
                        if type(idx)!=float:
                            print('error: ', idx, ' in list ', num,\
                                   ' is not a number')
                            return None
                val_list=[]
                for idx in num:
                    val_list+=[self.a * idx**2 + self.b * idx + self.c]
                return val_list
        return self.a * num**2 + self.b * num + self.c
    
    def roots(self): #needs fixing for special cases mentioned in assn.
        """returns a list of the quadratic's imaginary roots
    parameters: n/a
    returns: list"""
        ret=[]
        pos=((-1 * self.b + (self.b **2 - 4 * self.a * self.c)**.5) / 2 * self.a)
        neg=((-1 * self.b - (self.b **2 - 4 * self.a * self.c)**.5) / 2 * self.a)
        if type(pos) == float:
            ret += [pos]
        if type(neg) == float:
            if neg != pos: #prevents duplications if only 1 root exists
                ret += [neg]
        ret.sort()
        return ret

    def save(self, fname):
        """writes attributes to file fname
    parmeters: fname: a string
    returns: bool"""
        if type(fname) != str:
            return False
        save=open(fname,"w")
        save.write(str(self.a)+"\n")
        save.write(str(self.b)+"\n")
        save.write(str(self.c)+"\n")
        save.close()
        return True

    def load(self, fname):
        """reads file fname and assigns them to self.a, self.b, self.c successively
    parameters: fname: a string
    returns: bool"""
        if type(fname) != str:
            return False
        load=open(fname,"r")
        self.a = float(load.readline())
        self.b = float(load.readline())
        self.c = float(load.readline())
        load.close()
        return True

def make_quadratic(a,b,c):
    """returns instance of class Quadratic with attriutes a,b,c = a,b,c
    parameters: a,b,c: numbers
    returns: instnace of class Quadratic"""
    for x in [a,b,c]:
        if type(x)!=int:
            if type(x)!=float:
                print("error: ",x," not int or float")
                return None
    ret=Quadratic()
    ret.a=float(a)
    ret.b=float(b)
    ret.c=float(c)
    return ret

assertEqual(make_quadratic("a","b","c"),None)
assertEqual(make_quadratic([],{},7),None)
assertEqual(make_quadratic(4, 5, "a"),None)

test3 = make_quadratic(2,3,-40) #for testing evaluate and roots methods
test4 = make_quadratic(0,3,50)
test5 = make_quadratic(4, 5, 6)
test6 = make_quadratic(1,-8,16)

assertEqual(test3.roots(),[-21.138357147217054, 15.138357147217054])
assertEqual(test4.roots(),[0.0])
assertEqual(test5.roots(),[])
assertEqual(test6.roots(),[4.0])

assertEqual(test3.evaluate(1),-35.0)
assertEqual(test4.evaluate(-1),47.0)
assertEqual(test5.evaluate(0),6.0)
assertEqual(test6.evaluate("dogs"),None)

triangle = Quadratic()
triangle.a=3
triangle.b=4
triangle.c=5
triangle.save("texttest.txt")

print(triangle.load("texttest.txt"))
print(triangle.a, triangle.b, triangle.c)
