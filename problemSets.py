import myLibs
import random

def FindEulerianCycle2(adjList):
    eCycle = []
    nodes = dict(adjList)
    currentNode = random.choice(adjList.keys())
    while currentNode:
        eCycle.append(currentNode)
        print "Current node: " + str(currentNode)
        nextNodes = adjList[currentNode]
        print "Next nodes: " + str(nextNodes)
        if not nextNodes:
            print "Dead-end reached"
            myLibs.PrintAdjList(nodes)
            currentNode = ""
        else:
            index = random.randint(0,len(nextNodes)-1)
            nextNode = nextNodes[index]
            print "Next node: " + str(nextNode)
            nodes[currentNode].remove(nextNode)
            currentNode = nextNode
    return eCycle

def FindEulerianCycle(adjList):
    eCycle = []
    nodes = dict(adjList)
    currentNode = random.choice(adjList.keys())

    #form initial cycle
    while True:
        eCycle.append(currentNode)
        print "Current node: " + str(currentNode)
        nextNodes = adjList[currentNode]
        print "Next nodes: " + str(nextNodes)
        if not nextNodes:
            print "Dead-end reached"
            myLibs.PrintAdjList(nodes)
            nextNodes = []
            for node in eCycle:
                if len(adjList[node]) > 0:
                    nextNodes.append(node)
            if not nextNodes:
                print "Eulerian Cycle found: " + str(eCycle)
                return eCycle;
            else:
                print "Cycle = " + str(eCycle)
                print "Next nodes: " + str(nextNodes)
                index = random.randint(0, len(nextNodes) - 1)
                nextNode = nextNodes[index];
                print "Next node: " + str(nextNode)
                break
        else:
            index = random.randint(0,len(nextNodes)-1)
            nextNode = nextNodes[index]
            print "Next node: " + str(nextNode)
            nodes[currentNode].remove(nextNode)
            currentNode = nextNode
    return eCycle

#Week2, 1-2, Step2 - Code Challenge
inputFile ="myInput.txt"
outputFile = "answer.txt"

fOut = open(outputFile, 'w')

#get contents of file
contents = [line.rstrip('\n') for line in open(inputFile)]

#create empty adjacency list
adjList = dict()

#create adjacency list from file contents
for line in contents:
    keyVal = line.split(" -> ")
    node = keyVal[0]
    routes = keyVal[1].split(",")
    newRoutes = []
    for route in routes:
        newRoutes.append(route)
    adjList[node] = newRoutes

fOut.close()

FindEulerianCycle(adjList)