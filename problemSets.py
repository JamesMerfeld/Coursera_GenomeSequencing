import myLibs
import random

def FindEulerianCycle2(adjList):
    eCycle = ""
    numEdges = 0
    startNodes = []
    for node in adjList:
        startNodes.append(node)
        numEdges += len(adjList[node])
    print startNodes
    while(True):
        workingNodes = []
        for node in startNodes:
            workingNodes.append(node)
        while len(workingNodes) > 0:
            cycle = []
            visited = []
            currentNode = workingNodes[random.randint(0, len(workingNodes)-1)]
            workingNodes.remove(currentNode)
            while len(visited) < numEdges:
                #print "Current node: " + str(currentNode)
                #print "Visited edges: " + str(visited)
                nextNodes = adjList[currentNode]
                for node in nextNodes:
                    key = str(currentNode)+str(node)
                    if key in visited:
                        nextNodes.remove(node)
                if not nextNodes:
                    print "Dead-end found"
                    break
                #print "Possible next nodes: " + str(nextNodes)
                nextNode = nextNodes[random.randint(0, len(nextNodes)-1)]
                #print "Next node: " + str(nextNode)
                visited.append(str(currentNode)+str(nextNode))
                currentNode = nextNode
            if len(visited) == numEdges:
                eCycle = str(visited)
                break
        if eCycle:
            break
    return eCycle

def FindEulerianCycle(adjList):
    eCycle = []
    startNodes = []
    edges = []
    for node in adjList:
        startNodes.append(node)
        for n in adjList[node]:
            edges.append(str(node)+str(n))
    currentNode = startNodes[random.randint(0, len(startNodes) - 1)]
    while len(startNodes) > 0:
        startNodes.remove(currentNode)
        toVisit = list(edges)
        while len(toVisit) > 0:
            nextNodes = []
            for node in adjList[currentNode]:
                key = str(currentNode)+str(node)
                if key in toVisit:
                    nextNodes.append(key[1])
            if not nextNodes:
                print "Dead-end found"
                currentNode = toVisit[random.randint(0, len(toVisit) - 1)][0]
                break
            nextNode = nextNodes[random.randint(0, len(nextNodes) - 1)]
            currentNode = nextNode
            toVisit.remove((str(currentNode)+str(nextNode)))
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

print(FindEulerianCycle(adjList))
#myLibs.PrintAdjList(adjList)