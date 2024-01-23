# constants are vars that values cant be altered

# Enums are readable names that are bound to a constant val
from enum import Enum

class State(Enum): #initializing Enum
    INACTIVE = 0
    ACTIVE = 1

print(State.ACTIVE) # returns State.ACTIVE
print(State(1)) # returns State.ACTIVE
print(State['ACTIVE']) # returns State.ACTIVE

print(list(State))
print(len(State)) # 2

