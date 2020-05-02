# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()

"""def GraphSearch(problem,frontier):
    start_state = problem.getStartState()
    explored = set()
    frontier.push((start_state,[]))
    while True:
        popped_element = frontier.pop()
        node = popped_element[0]
        path_till_node = popped_element[1]
        if problem.isGoalState(node):
            break;
        else:
            if node not in explored:   # Skipping already visited nodes
                explored.add(node)     # Adding newly encountered nodes to the set of visited nodes
                for successor in problem.getSuccessors(node):
                    child_node = successor[0]
                    child_path = successor[1]
                    full_path = path_till_node + [child_path]  # Computing path of child node from start node
                    frontier.push((child_node, full_path)) # Pushing ('Child Node',[Full Path]) to the fringe
    
    return path_till_node
"""        


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    fringe = util.Stack()  # Fringe (Stack) to store the nodes along with their paths
    init_state = problem.getStartState()
    visited = set()  # A set to maintain all the visited nodes
    fringe.push((init_state,[]))  # Pushing (Node, [Path from start-node till 'Node']) to the fringe
    while True:
        node, path_till_node = fringe.pop()
        if problem.isGoalState(node):  # Exit on encountering goal node
            break
        else:
            if node not in visited:   # Skipping already visited nodes
                visited.add(node)     # Adding newly encountered nodes to the set of visited nodes
                for success in problem.getSuccessors(node):
                    n_state = success[0]
                    n_direction = success[1]
                    fringe.push((n_state, path_till_node+ [n_direction])) # Pushing ('Child Node',[Full Path]) to the fringe
    return path_till_node

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    fringe = util.Queue()
    init_state = problem.getStartState()
    visited = set()  # A set to maintain all the visited nodes
    fringe.push((init_state,[]))  # Pushing (Node, [Path from start-node till 'Node']) to the fringe
    while True:
        node, path_till_node = fringe.pop()
        if problem.isGoalState(node):  # Exit on encountering goal node
            break
        else:
            if node not in visited:   # Skipping already visited nodes
                visited.add(node)     # Adding newly encountered nodes to the set of visited nodes
                for success in problem.getSuccessors(node):
                    n_state = success[0]
                    n_direction = success[1]
                    fringe.push((n_state, path_till_node+ [n_direction])) # Pushing ('Child Node',[Full Path]) to the fringe
    return path_till_node


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    fringe = util.PriorityQueue()
    init_state = problem.getStartState()
    visited = set()  # A set to maintain all the visited nodes
    fringe.push((init_state,[],0),0)  # Pushing (Node, [Path from start-node till 'Node']) to the fringe
    while True:
        node, path_till_node, cost_till_node = fringe.pop()
        if problem.isGoalState(node):  # Exit on encountering goal node
            break
        else:
            if node not in visited:   # Skipping already visited nodes
                visited.add(node)     # Adding newly encountered nodes to the set of visited nodes
                for success in problem.getSuccessors(node):
                    n_state = success[0]
                    n_direction = success[1]
                    n_cost = success[2]
                    fringe.push((n_state, path_till_node+ [n_direction],n_cost+cost_till_node),cost_till_node+n_cost) # Pushing ('Child Node',[Full Path]) to the fringe
    return path_till_node

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    fringe = util.PriorityQueue()
    init_state = problem.getStartState()
    visited = set()  # A set to maintain all the visited nodes
    fringe.push((init_state,[],0),heuristic(init_state,problem)+0)  # Pushing (Node, [Path from start-node till 'Node']) to the fringe
    while True:
        node, path_till_node, cost_till_node = fringe.pop()
        if problem.isGoalState(node):  # Exit on encountering goal node
            break
        else:
            if node not in visited:   # Skipping already visited nodes
                visited.add(node)     # Adding newly encountered nodes to the set of visited nodes
                for success in problem.getSuccessors(node):
                    n_state = success[0]
                    n_direction = success[1]
                    n_cost = success[2]
                    fringe.push((n_state, path_till_node+ [n_direction],n_cost+cost_till_node),cost_till_node+n_cost+heuristic(n_state,problem)) # Pushing ('Child Node',[Full Path]) to the fringe
    return path_till_node


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
