'''
    Made by Devansh Srivastava
    knapsack Problem using genetic algorithm
    30 - 08 - 2018, 12:51 AM
    The sun is hot, that's what we are taught '''

# knapsack simple 0/1 problem representation using genetic algorithm in python

import random

x = [] # list storing random quantities as for the weights
fitX = [] # list for storing the fit candidates
fitestX = [] # for storing the fittest from every generation

# evaluating candidates
def evaluateCandidate(w,wl,size, popsize):
    ''' This function evaluates whether the candidate is
    eligible for participation in crossover and mutation
    i.e. sum of it weights is <= the weight limit provided '''

    fitX.clear()
    for i in range(0, popsize):
        y = []
        condition = 0
        for j in range(0,size):
            condition = condition + w[j]*x[i][j]

        if condition <= wl and condition > 0:
            for k in range(0,size):
                y.append(x[i][k])
            if y not in fitX:
                fitX.append(y)
        del y
        del condition

    print("The fit candidates are : \n {}".format(fitX))

# mutation Process
def mutation(size, populationSize):
    for i in range(0,populationSize):
        rand1 = random.randrange(size)
        if x[i][rand1] == 0:
            x[i][rand1] = 1
        else:
            x[i][rand1] = 0

    r = random.randrange
    del x[r(len(x)-populationSize)]


# crossover process
def crossover(crossarray, popsize):
    if len(x) > popsize:
        return
    else:
        pivotIndex = len(crossarray[0])//2
        x.append(crossarray[0][:pivotIndex] + crossarray[1][pivotIndex:])
        x.append(crossarray[1][:pivotIndex] + crossarray[0][pivotIndex:])


# Selection process for crossover using roulette process
def rouletteProcess(y,popsize, fitestX):
    x.clear()
    x.append(fitestX)
    fitlength = len(fitX)
    rouletteWidth = fitlength * 10

    while len(x) < popsize:
        forCrossover = []
        while len(forCrossover) < 2:
            rand2 = random.randrange(rouletteWidth)
            indexes = rand2//10
            forCrossover.append(fitX[indexes])
        crossover(forCrossover, popsize)


def selection(money, size, pop):
    y = []
    temp = []

    for i in range(0,len(fitX)):
        tempY = []
        for j in range(0,size):
            tempY.append(money[j]*fitX[i][j])

        y.append(tempY)
        temp.append(sum(y[i]))
        del tempY

    fitestX = fitX[temp.index(max(temp))]
    print("{} is the fittest candidate \n\n ".format(fitestX))
    rouletteProcess(y, pop, fitestX)
    del y, temp



# initializing random population
def initializeRandomPop(size, popsize):
    ''' here random population for quantity are
        obtained using randrange '''
    rand1  = random.randrange
    for i in range(0,popsize):
        y = []
        for j in range (0, size):
            y.append(rand1(0,2))
        x.append(y)
        del y

    print("The population initialized is  : \n {}".format(x))

# main function
def main():
    ''' Main function of the program.'''

    size = int(input("How many weights do you want? "))
    populationSize = int(input("Enter the population size : "))

    w = []
    m = []
    for i in range(0,size):
        print("Enter for weight",(i+1))
        w.append(int(input()))
        print("Enter money for weight",(i+1))
        m.append(int(input()))
    # 2d array of lists holding weights and money
    options = [w,m]
    print(options)
    # max weight limit of the knapsack
    W = int(input("Enter the weight limit : "))

    # initializing population
    initializeRandomPop(size, populationSize)
    for i in range(0,3):
        print("\n\n ---- This one is the {} iteration ---- \n\n".format(i+1))
        evaluateCandidate(w,W,size, populationSize)
        selection(m, size, populationSize)
        print("Array after crossover : ",x)
        mutation(size, populationSize)
        fitestX.clear()
        print("The new mutated arrar is {}\n\n\n\n".format(x))


if __name__ == '__main__':
    main()
