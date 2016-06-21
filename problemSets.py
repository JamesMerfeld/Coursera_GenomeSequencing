import myLibs

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
myLibs.PrintAdjList(adjList)

fOut.close()