#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name:  Alan Grissette
# email: hsalley@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        self.tiles[0][0]=digitstr[0]
        self.tiles[0][1]=digitstr[1]
        self.tiles[0][2]=digitstr[2]
        self.tiles[1][0]=digitstr[3]
        self.tiles[1][1]=digitstr[4]
        self.tiles[1][2]=digitstr[5]
        self.tiles[2][0]=digitstr[6]
        self.tiles[2][1]=digitstr[7]
        self.tiles[2][2]=digitstr[8]
        
           

        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[r])):
                if self.tiles[r][c]=="0":
                    self.blank_r=r
                    self.blank_c=c
    
    def __repr__(self):
        """represnts board """
        s=""
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[r])):
               if self.tiles[r][c]=="0":
                   s+="_"
               else:
                   s+=self.tiles[r][c]
        return s[0]+" "+s[1]+" "+s[2]+" "+"\n"+s[3]+" "+s[4]+" "+s[5]+" "+"\n"+s[6]+" "+s[7]+" "+s[8]+" "+"\n"

     
    def move_blank(self, direction):
        """moves the spaces in the bnoard"""
        oldnum=""
        if direction=="up":
            if self.blank_r==0:
                return False 
            else: 
                oldnum=self.tiles[(self.blank_r)-1][self.blank_c]
                self.tiles[self.blank_r][self.blank_c]=oldnum
                self.tiles[(self.blank_r)-1][self.blank_c]="0"
                self.blank_r-=1
                return True
        elif direction=="down":
            if self.blank_r==2:
                return False 
            else: 
                oldnum=self.tiles[(self.blank_r)+1][self.blank_c]
                self.tiles[self.blank_r][self.blank_c]=oldnum
                self.tiles[(self.blank_r)+1][self.blank_c]="0"
                self.blank_r+=1
                return True
        elif direction=="right":
            if self.blank_c==2:
                return False 
            else: 
                oldnum=self.tiles[(self.blank_r)][(self.blank_c)+1]
                self.tiles[self.blank_r][self.blank_c]=oldnum
                self.tiles[(self.blank_r)][(self.blank_c)+1]="0"
                self.blank_c+=1
                return True
        elif direction=="left":
            if self.blank_c==0:
                return False 
            else: 
                oldnum=self.tiles[(self.blank_r)][(self.blank_c)-1]
                self.tiles[self.blank_r][self.blank_c]=oldnum
                self.tiles[(self.blank_r)][(self.blank_c)-1]="0"
                self.blank_c-=1
                return True
                
    def digit_string(self):
        """ represewnts the niumbers as a string"""
        s=""
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[r])):
                if self.tiles[r][c]=="_":
                    s+="0"
                else:
                    s+=self.tiles[r][c]
        return s
    
    def num_misplaced(self):
        "shows misplaced numbers"
        count=-1
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[r])):
                if self.tiles[r][c]!=GOAL_TILES[r][c]:
                    count+=1
        return count
                    
    def copy(self):
        """copies board """
        return Board(str(self.digit_string()))
        
    def __eq__(self, other):
        """ compares tiles to list """
        
        if self.tiles==other:
            return True
        else:
            return False
        
 
        
        
        
        


    ### Add your other method definitions below. ###
