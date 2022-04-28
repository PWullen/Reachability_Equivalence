# equivalence
"""Using PyEDA, write a program in Python that takes as input the specification of two sequential circuits
and determines whether they are equivalent, when is each is started in its own initial state (all FFs have 0)"""
from pyeda.inter import *
import os
import blifparser.blifparser as blifparser

from ReachableStates import cofactors


def Wullen_Equivalence():
    # get the file path and pass it to the parser
    filepath = os.path.abspath("Equivalence.py")
    parser = blifparser.BlifParser(filepath)
    # get the object that contains the parsed data
    # from the parser
    blif = parser.blif
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
    print("FSM from circuit a")
    print(TTa)
    print("FSM from circuit b")
    print(TTb)
    ProductMachine = Xor(FSMa, FSMb)
    TTP = expr2truthtable(ProductMachine)
    Fs = cofactors(ProductMachine, (x, v, Y1, Y2, Y3, Z1, Z2))
    print(TTP)
    print(ProductMachine)
    print(Fs)
    # get the list of boolean functions (.names)
    #print(blif.fsm.i)
