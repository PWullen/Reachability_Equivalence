#dump file for ideas that no longer fit into the scheme

def IMG(f):
    """To compute the Image restricted to a subset C,
       we can compute the Range of another function, namely Constrain(f, C)"""
    #output splitting
    #IM = y.i & IMG(f.i, ONset(f)) | ~y.i & IMG(f.i, ONset(~f))
    #2 found in page 318 + 324 of book LOGIC SYNTHESIS
    #in IMG(f), treat f as a relation, and perform quantification
    print("generating image")
    F = smoothing(f)
    print(F)
    return F

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



"""
def State_Equivalence(X, S, delta, lmda):
    #transfered from the lecture notes
    #X =
    #S =
    #delta =
    #lmda =
    P0 = set(B0,B1)
    S = set(B0,B1)
    P1 = P0
    for x in X:
        for s.j in S and o.xj in lmda(sj, x):
            P1x = Partition(ox, B01)
            P1 = Refine(P1, P1x)
            if Independent(lmda, x) == True:
                break
    if P1 == P0:
        return P0, 0
    for k in range(0, len(S)):
        Pk = {}
        for Bi in P.k-1:
            P.ik = B.i
            for x in X:
                for s.j in B.i
                    t.xj = delta(s.j, x)
                    b.x = block_index(t.x, P.k-1)
                    Pb.xi = Partition(b.x, B.i)
                    P.ik = Refine(P.ik, Pb.xi)
                P.k = union(P.k, P.ik)
        if P.k = P.k-1:
            return P.k, k-1


#dependent equations for State_Equivalence
def Independent(a, b): #clearly incorrect, just dummy eq for now
    if a != b:
        yield True
    else:
        yield False


def Partition(a, b):  #clearly incorrect, also dummy eq for now
    a = function.component
    b = function
    yield(a, b)


def Refine(a, b):  #clearly incorrect, also dummy eq for now
    a = function
    b = function
    yield(a, b)


def union(a, b):  #simplified, dummy eq will be refined later
    ans = a|b
    yield ans


def block_index(a, b):  #clearly incorrect but dummy func to stand in
    a = function
    b = index(a)
    yield a.b
"""