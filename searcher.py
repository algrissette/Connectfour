#
# searcher.py (Final project)
#
# classes for objects that perform state-space search on Eight Puzzles  
#
# name: Alan Grissette
# email: hsalley@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

import random
from state import *


class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    ### Add your Searcher method definitions here. ###
    
    def __init__(self, depth_limit):
        """initializes the searcher """ 
        self.states=[]
        self.num_tested=0
        self.depth_limit=depth_limit
        
            
            

    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s


    def add_state(self, new_state):
        """adds one state to the self.state """
        self.states+=[new_state]
    
    def should_add(self, state):
        """checks if we should add a state based on if the tile can move in specific directions """
        if self.depth_limit!=-1: 
            if state.num_moves>self.depth_limit:
              
                return False
        if state.creates_cycle()==True:
            return False
    
        return True
    
    def add_states(self, new_states):
        """addss multiple states based off should add """
        
        for state in new_states:
            if self.should_add(state)==True:
                self.add_state(state)
                
                
    def next_state(self):
        """ chooses the next state to be tested from the list of 
        untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s     


        
    def find_solution(self, init_state):

        self.add_state(init_state)
        while len(self.states)>0:
           s=self.next_state()
           if s.is_goal()==True:
               
               self.num_tested+=1
               return s
           else:
               self.num_tested+=1
               self.add_states(s.generate_successors())
        
        return None 
   
    

        
### Add your BFSeacher and DFSearcher class definitions below. ###

class BFSearcher(Searcher):
    """ BFS involves always choosing one the untested states that has the smallest depth (i.e., the smallest number of moves from the initial state)."""
    
    def next_state(self):
        s = self.states[0]
        self.states.remove(s)
        return s 

class DFSearcher(Searcher):
    """DFS involves always choosing one the untested states that has the largest depth (i.e., the largest number of moves from the initial state).

 """
    
    def next_state(self):
        s = self.states[-1]
        self.states.remove(s)
        return s 

def h0(state):
    """ a heuristic function that always returns 0 """
    return 0

### Add your other heuristic functions here. ###


class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    ### Add your GreedySearcher method definitions here. ###'


    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s
    
    def __init__(self, heuristic):
        super().__init__(-1)
        self.heuristic=heuristic
    
    def priority(self, state):
        """ computes and returns the priority of the specified state,
        based on the heuristic function used by the searcher
        """
        return -1 * (self.heuristic(state))
    
    def add_state(self,state):
        """ """
        self.states+=[[self.priority(state),state]]
        
        
        
        
    def next_state(self):
        """ """
        maxstate=max(self.states)
        self.states.remove(maxstate)
        return maxstate[1]

    



### Add your AStarSeacher class definition below. ###

class AStarSearcher(GreedySearcher):
    """ Like greedy search, A* is an informed search algorithm that assigns a priority to each state based on a heuristic function, and that selects the next state based on those priorities.  """
   
    def priority(self,state):
        return -1*( self.heuristic(state)+state.num_moves)
        
    


                  
def h1(state):
    """huerstic function that returns a number based on the misplaced tiles """
    s=state.board.num_misplaced()
    return s

def h2(state):
    """returns a number based on the amount of tiles misplaced column and row wise """
    points=16
    board=state.board
    for r in range(len(board.tiles)):
        for c in range(len(board.tiles[r])):
            if board.tiles[r][c] in GOAL_TILES[r]:
                points-=1
            if board.tiles[r][c] in GOAL_TILES[0][c]:
                points-=1
            if board.tiles[r][c] in GOAL_TILES[1][c]:
                points-=1
            if board.tiles[r][c] in GOAL_TILES[2][c]:
                points-=1
    return points 
            
