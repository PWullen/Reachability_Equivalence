# equivalence
"""Using PyEDA, write a program in Python that takes as input the specification of two sequential circuits
and determines whether they are equivalent, when is each is started in its own initial state (all FFs have 0)"""
import numpy as np
from pyeda.inter import *

def Wullen_Equivalence(a, b, c, d):
    print("Running equivalence")
    X = a
    S = b
    delta = c
    lmda = d
    State_Equivalence(X, S, delta, lmda)


def State_Equivalence(X, S, delta, lmda):
    """transfered from the lecture notes
       X =
       S =
       delta =
       lmda = """
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
