from logic import *
 
AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")
BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

statement = And(AKnight, AKnave)
knowledge0 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Implication(AKnight, statement),
    Implication(AKnave, Not(statement)),
)

print("Puzzle 0")
print(AKnight, model_check(knowledge0, AKnight))
print(AKnave, model_check(knowledge0, AKnave))

statement = And(AKnave, BKnave)
knowledge1 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Implication(AKnight, statement),
    Implication(AKnave, Not(statement)),
)

print("Puzzle 1")
print(AKnight, model_check(knowledge1, AKnight))
print(AKnave, model_check(knowledge1, AKnave))
print(BKnight, model_check(knowledge1, BKnight))
print(BKnave, model_check(knowledge1, BKnave))

same = Or(And(AKnight, BKnight), And(AKnave, BKnave))
different = Or(And(AKnight, BKnave), And(AKnave, BKnight))
knowledge2 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Implication(AKnight, same),
    Implication(AKnave, Not(same)),
    Implication(BKnight, different),
    Implication(BKnave, Not(different)),
)

print("Puzzle 2")
print(AKnight, model_check(knowledge2, AKnight))
print(AKnave, model_check(knowledge2, AKnave))
print(BKnight, model_check(knowledge2, BKnight))
print(BKnave, model_check(knowledge2, BKnave))