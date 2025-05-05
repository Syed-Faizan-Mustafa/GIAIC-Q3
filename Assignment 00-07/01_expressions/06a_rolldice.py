import random 

"""
Simulate rolling two dice, and prints results of each
roll as well as the total.
"""

# Number of sides on each die to roll
NUM_SIDES: int = 6 
def main():
    die1 :int = random.randint(1, NUM_SIDES)
    die2 :int = random.randint(1, NUM_SIDES)
    #get their total of num die1 + die2
    total : int = die1 + die2

    # print the result
    print("1 dice have", NUM_SIDES, "sides each")
    print("First Die", die1)
    print("Second Die", die2)
    print("Total after addition of both dice is: ", total)

    """for call the module which is calling in the project not as module,
    but it is module to use in other program but its class and its function"""

if __name__ == "__main__":
    main()
