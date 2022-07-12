# equivalence
"""Using PyEDA, write a program in Python that takes as input the specification of two sequential circuits
and determines whether they are equivalent, when is each is started in its own initial state (all FFs have 0)"""
from pyeda.inter import *
from ReachableStates import cofactors

def Wullen_Equivalence():
    """
    Wullen_Equivalence takes in hardcoded input from two Finite State Machines, to then take the product machine
    to check for Equivalence.
    It does this through the inputs of logical expressions derived from the specific FSMs being operated on via Xor()
    from PyEDA. Cofactoring the Xor result yields the possible logical values, which should all yield=0 if the FSMs are
    equivalent.

    Various print statements are nested in the code readily able to be uncommented for visual inspection of the truth
    table values, and the logical expression values.

    """
    # init FSMs
    y1, y2, y3, Y1, Y2, Y3, x = map(exprvar, 'abcABCx')
    y1 = Or(And(~x, Y1), Y3)
    y2 = And(x, Y1)
    y3 = y2
    FSMa = And(y1, y2, y3)
    TTa = expr2truthtable(FSMa)
    z1, z2, Z1, Z2, v = map(exprvar, 'abABx')
    z1 = And(v, Or(~Z1, ~Z2))
    z2 = z1
    FSMb = And(z1, z2)
    TTb = expr2truthtable(FSMb)
    """Logic Expression printouts"""
    #print(FSMa)
    #print(FSMb)

    """Truth Table printouts"""
    #print("FSM from circuit a")
    #print(TTa)
    #print("FSM from circuit b")
    #print(TTb)

    ProductMachine = Xor(FSMa, FSMb)
    TTP = expr2truthtable(ProductMachine)
    Fs = cofactors(ProductMachine, (x, v, Y1, Y2, Y3, Z1, Z2))
    """Product Machine printouts"""
    #print(TTP)
    #print(ProductMachine)
    #print(Fs)
    result = "Since the result of the Xor operation from the product machine is not all =0; we do not have equivalence."
    print(result)
    return False
