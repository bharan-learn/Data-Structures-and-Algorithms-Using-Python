'''
Tower of Hanoi is a mathematical puzzle where we have three rods and n disks. The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:
1) Only one disk can be moved at a time.
2) Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack i.e. a disk can only be moved if it is the uppermost disk on a stack.
3) No disk may be placed on top of a smaller disk.
'''

'''
Algorithm:

A: Source
B: Destination
C: Auxillary

Move n-1 discs from A to C.
Move nth disc from A to B.

n-1 discs from C to B is a subproblem using A as Auxillary.

For n disks, total 2^n – 1 moves are required.

For n disks, total 2^(n+1) – 1 function calls are made.

'''


def towers_of_hanoi(number_of_discs,source,destination,auxillary):

# Base Case:

    if number_of_discs==1:
        print("Move Disc " + str(number_of_discs) + "from" + source + "to" + destination)
        #Terminate the Base case
        return
# Recursive Case:

    #   Move n-1 Discs to Source to Auxillary
    towers_of_hanoi(number_of_discs-1, source, auxillary, destination)
    print("Move Disc " + str(number_of_discs)+ "from" + source + "to" + destination)
    #   Subproblem - Move n-1 Discs from Auxillary to Destination
    towers_of_hanoi(number_of_discs-1, auxillary, destination,source)


towers_of_hanoi(4, "A", "B" , "C")
