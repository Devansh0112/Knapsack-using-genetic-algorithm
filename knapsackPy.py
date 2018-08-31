'''
    Made by Devansh Srivastava
    knapsack Problem using Particle Swarm Optimzation (PSO)
    30 - 08 - 2018, 12:51 AM
    The sun is hot, that's what we are taught '''

# knapsack simple 0/1 problem representation using PSO algorithm in python
# see readme for help PSO

import random

def evaluateCandidate(money, weight, wl, opsol):

    weightTotal = sum(weight)
    moneyTotal = sum(money)

    if weightTotal <= wl:
        return moneyTotal
    else:
        return opsol


def initializePop(options1, Wlimit, size):
    ''' Function to calculate the total benefits
        in the knapsack after putting some quantities of
        the weights '''

    j=0
    rand1  = random.randrange
    weightTotal = []
    moneyTotal = []
    opsol = 0
    x = []
    while j < 10000:
        for k in range(0,size):
            x.insert(k, rand1(0,2))
        for i in range(0,size):
            weightTotal.insert(i, x[i] * options1[0][i])
            moneyTotal.insert(i, x[i] * options1[1][i])

        optimalSolution = evaluateCandidate(moneyTotal, weightTotal, Wlimit, opsol)
        if optimalSolution > opsol:
            opsol = optimalSolution
            print("We found an optimal solution with money", optimalSolution)
            print("The weights are",weightTotal)
            print("The quantities are", x, "\n")

        # incrementing the generation
        j = j + 1
        x.clear()
        weightTotal.clear()
        moneyTotal.clear()

def main():
    ''' Main function of the program. I know it is redundant
    in python to make a main function '''
    weights = int(input("How many weights do you want? "))
    w = []
    m = []
    for i in range(0,weights):
        print("Enter for weight",(i+1))
        w.insert(i,int(input()))
        print("Enter money for weight",(i+1))
        m.insert(i,int(input()))
    # 2d array of lists holding weights and money
    options = [w,m]
    print(options)
    # max weight limit of the knapsack
    W = int(input("Enter the weight limit : "))

    # initializing population
    initializePop(options,W,weights)


if __name__ == '__main__':
    main()
