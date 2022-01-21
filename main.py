from enum import Enum
from copy import copy,deepcopy
from termcolor import colored

class Color(Enum):
    G = str(colored('█',"green"))
    R = str(colored('█',"red"))
    B = str(colored('█',"blue"))
    O = str(colored('█',"magenta"))
    W = str(colored('█',"white"))
    Y = str(colored('█',"yellow"))
    N = 'N'


class Cube():
    def __init__(self): 
        self.cube = [[Color.N,Color.N,Color.N,Color.W,Color.W,Color.W,Color.N,Color.N,Color.N,Color.N,Color.N,Color.N],[Color.N,Color.N,Color.N,Color.W,Color.W,Color.W,Color.N,Color.N,Color.N,Color.N,Color.N,Color.N],[Color.N,Color.N,Color.N,Color.W,Color.W,Color.W,Color.N,Color.N,Color.N,Color.N,Color.N,Color.N],

        [Color.O,Color.O,Color.O,Color.G,Color.G,Color.G,Color.R,Color.R,Color.R,Color.B,Color.B,Color.B],[Color.O,Color.O,Color.O,Color.G,Color.G,Color.G,Color.R,Color.R,Color.R,Color.B,Color.B,Color.B],[Color.O,Color.O,Color.O,Color.G,Color.G,Color.G,Color.R,Color.R,Color.R,Color.B,Color.B,Color.B],

        [Color.N,Color.N,Color.N,Color.Y,Color.Y,Color.Y,Color.N,Color.N,Color.N,Color.N,Color.N,Color.N],[Color.N,Color.N,Color.N,Color.Y,Color.Y,Color.Y,Color.N,Color.N,Color.N,Color.N,Color.N,Color.N],[Color.N,Color.N,Color.N,Color.Y,Color.Y,Color.Y,Color.N,Color.N,Color.N,Color.N,Color.N,Color.N]
        ]

    def operation(self,op):
        if op == "f":
            self.flip()
        if op == "F":
            self.flip()
            self.flip()
            self.flip()
        if op == "k":
            self.top()
        if op == "l":
            self.side()
        if op == "j":
            self.top()
            self.top()
            self.top()
        if op == "h":
            self.side()
            self.side()
            self.side()


    def flip(self):
        old = deepcopy(self.cube)
        #corners
        self.cube[3][3] = old[3][5]
        self.cube[3][5] = old[5][5]
        self.cube[5][5] = old[5][3]
        self.cube[5][3] = old[3][3]
        #edges
        self.cube[3][4] = old[4][5]
        self.cube[4][5] = old[5][4]
        self.cube[5][4] = old[4][3]
        self.cube[4][3] = old[3][4]
        #sides
        self.cube[2][3] = old[3][6]
        self.cube[2][4] = old[4][6]
        self.cube[2][5] = old[5][6]

        self.cube[3][6] = old[6][5]
        self.cube[4][6] = old[6][4]
        self.cube[5][6] = old[6][3]

        self.cube[6][5] = old[5][2]
        self.cube[6][4] = old[4][2]
        self.cube[6][3] = old[3][2]

        self.cube[5][2] = old[2][3]
        self.cube[4][2] = old[2][4]
        self.cube[3][2] = old[2][5]

    def side(self):
        old = deepcopy(self.cube)

        for i in range(3,12):
            self.cube[3][i] = old[3][i-3]
            self.cube[4][i] = old[4][i-3]
            self.cube[5][i] = old[5][i-3]
        for i in range(3):
            self.cube[3][i] = old[3][9+i]
            self.cube[4][i] = old[4][9+i]
            self.cube[5][i] = old[5][9+i]

        #counterclockwise
        #corners
        self.cube[0][3] = old[0][5]
        self.cube[0][5] = old[2][5]
        self.cube[2][5] = old[2][3]
        self.cube[2][3] = old[0][3]
        #edges
        self.cube[0][4] = old[1][5]
        self.cube[1][5] = old[2][4]
        self.cube[2][4] = old[1][3]
        self.cube[1][3] = old[0][4]

        #clockwise
        #corners
        self.cube[6+0][3] = old[6+2][3]
        self.cube[6+0][5] = old[6+0][3]
        self.cube[6+2][5] = old[6+0][5]
        self.cube[6+2][3] = old[6+2][5]
        #edges
        self.cube[6+0][4] = old[6+1][3]
        self.cube[6+1][5] = old[6+0][4]
        self.cube[6+2][4] = old[6+1][5]
        self.cube[6+1][3] = old[6+2][4]



    def top(self):
        old = deepcopy(self.cube)

        for i in range(6):
            self.cube[i][3] = old[i+3][3]
            self.cube[i][4] = old[i+3][4]
            self.cube[i][5] = old[i+3][5]

        self.cube[5][11] = old[0][3]
        self.cube[5][10] = old[0][4]
        self.cube[5][9] = old[0][5]
        self.cube[4][11] = old[1][3]
        self.cube[4][10] = old[1][4]
        self.cube[4][9] = old[1][5]
        self.cube[3][11] = old[2][3]
        self.cube[3][10] = old[2][4]
        self.cube[3][9] = old[2][5]

        self.cube[6][3] = old[5][11]
        self.cube[6][4] = old[5][10]
        self.cube[6][5] = old[5][9]
        self.cube[7][3] = old[4][11]
        self.cube[7][4] = old[4][10]
        self.cube[7][5] = old[4][9]
        self.cube[8][3] = old[3][11]
        self.cube[8][4] = old[3][10]
        self.cube[8][5] = old[3][9]

        #counterclockwise
        #corners
        self.cube[0+3][3-3] = old[0+3][5-3]
        self.cube[0+3][5-3] = old[2+3][5-3]
        self.cube[2+3][5-3] = old[2+3][3-3]
        self.cube[2+3][3-3] = old[0+3][3-3]
        #edges
        self.cube[0+3][4-3] = old[1+3][5-3]
        self.cube[1+3][5-3] = old[2+3][4-3]
        self.cube[2+3][4-3] = old[1+3][3-3]
        self.cube[1+3][3-3] = old[0+3][4-3]

        #clockwise
        #corners
        self.cube[0+3][3+3] = old[2+3][3+3]
        self.cube[0+3][5+3] = old[0+3][3+3]
        self.cube[2+3][5+3] = old[0+3][5+3]
        self.cube[2+3][3+3] = old[2+3][5+3]
        #edges  
        self.cube[0+3][4+3] = old[1+3][3+3]
        self.cube[1+3][5+3] = old[0+3][4+3]
        self.cube[2+3][4+3] = old[1+3][5+3]
        self.cube[1+3][3+3] = old[2+3][4+3]




    def __repr__(self):
        r = """       ╔═══════╗              
       ║┌─┬─┬─┐║              
       ║│%s│%s│%s│║              
       ║├─┼─┼─┤║              
       ║│%s│%s│%s│║              
       ║├─┼─┼─┤║              
       ║│%s│%s│%s│║              
╔══════╝└─┴─┴─┘╚═════════════╗
║┌─┬─┬─┐┌─┬─┬─┐┌─┬─┬─┐┌─┬─┬─┐║
║│%s│%s│%s││%s│%s│%s││%s│%s│%s││%s│%s│%s│║
║├─┼─┼─┤├─┼─┼─┤├─┼─┼─┤├─┼─┼─┤║
║│%s│%s│%s││%s│%s│%s││%s│%s│%s││%s│%s│%s│║
║├─┼─┼─┤├─┼─┼─┤├─┼─┼─┤├─┼─┼─┤║
║│%s│%s│%s││%s│%s│%s││%s│%s│%s││%s│%s│%s│║
║└─┴─┴─┘└─┴─┴─┘└─┴─┴─┘└─┴─┴─┘║
╚══════╗┌─┬─┬─┐╔═════════════╝
       ║│%s│%s│%s│║              
       ║├─┼─┼─┤║              
       ║│%s│%s│%s│║              
       ║├─┼─┼─┤║              
       ║│%s│%s│%s│║              
       ║└─┴─┴─┘║              
       ╚═══════╝              """ % (
               self.cube[0][3].value,self.cube[0][4].value,self.cube[0][5].value,
               self.cube[1][3].value,self.cube[1][4].value,self.cube[1][5].value,
               self.cube[2][3].value,self.cube[2][4].value,self.cube[2][5].value,

               self.cube[3][0].value,self.cube[3][1].value,self.cube[3][2].value,self.cube[3][3].value,self.cube[3][4].value,self.cube[3][5].value,self.cube[3][6].value,self.cube[3][7].value,self.cube[3][8].value,self.cube[3][9].value,self.cube[3][10].value,self.cube[3][11].value,
               self.cube[4][0].value,self.cube[4][1].value,self.cube[4][2].value,self.cube[4][3].value,self.cube[4][4].value,self.cube[4][5].value,self.cube[4][6].value,self.cube[4][7].value,self.cube[4][8].value,self.cube[4][9].value,self.cube[4][10].value,self.cube[4][11].value,
               self.cube[5][0].value,self.cube[5][1].value,self.cube[5][2].value,self.cube[5][3].value,self.cube[5][4].value,self.cube[5][5].value,self.cube[5][6].value,self.cube[5][7].value,self.cube[5][8].value,self.cube[5][9].value,self.cube[5][10].value,self.cube[5][11].value,

               self.cube[6][3].value,self.cube[6][4].value,self.cube[6][5].value,
               self.cube[7][3].value,self.cube[7][4].value,self.cube[7][5].value,
               self.cube[8][3].value,self.cube[8][4].value,self.cube[8][5].value,
               )
        return r
        

def main():
    c1 = Cube()
    print(c1)
    while True:
        s = input()
        if "reset" in s:
            c1 = Cube()
        elif "quit" in s:
            return
        else:
            for i in s:
                c1.operation(i)
        print(c1)



if __name__ == "__main__":
    main()
