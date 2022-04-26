#dump file for ideas that no longer fit into the scheme

def BFS_FSM(S, X, delta, Z, S0):
    """:input: state transition graph and initial states
       :return: set of reachable states from S0
       S = set of states
       X = input values
       delta = state transition function
       Z = output function
       S0 = initial states
       """
    print("running bfs from lecture pseudocode")
    Reached = From = New.o = S0
    k = 0  #level of current nodes
    while New.k is not None:
        k = k + 1
        To = IMG(delta, From)
        New.k = To - Reached
        From = New.k
        Reached = union(Reached, New.k)
    return(New.j for j in range(0,k))