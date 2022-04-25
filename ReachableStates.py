# reachable states
"""write a python program using the functions in PyEDA to implement the BFS algorithm with
the constrain operator that computes the reachable states of a state machine using image
computation. The input to your algorithm should be a state machine described in the KISS
format (Keep It Simple and Stupid). This is part of the BLIF (Berkeley Logic Interchange
Format) and is described in the file blif.pdf on the course website under Files. Demonstrate
your procedure on the state machine shown in Figure 1. Generate a table that shows the From
states, the New states and the Reached states, from the initial state 0."""
import numpy as np
from pyeda.inter import *
from pyeda.boolalg.bdd import _expr2bddnode
#Importing expr2bddnode for DFS operations

def BFS():
    """utilize constrain operator that computes the reachables states of a state machine using image computation"""
    print("running BFS")


def Wullen_ReachableStates():
    print("running reachable states")
