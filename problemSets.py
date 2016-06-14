def Composition(Text, k):
    retVal = []
    l = len(Text)
    for i in range(0,l-k+1):
        retVal.append(Text[i:i+k])
    return retVal

def GenomePathProblem(Pattern):
    retVal = ""
    l = len(Pattern)
    for i in range(0, l-1):
        retVal += Pattern[i][0]
    retVal += Pattern[l-1]
    return retVal

def Overlap(Pattern):
    adjList = []
    l = len(Pattern)
    for i in range(l):
        adjList.append(Pattern[i] + " -> ")
    return adjList

Pattern = ["ATGCG", "GCATG", "CATGC", "AGGCA", "GGCAT"]

print(Overlap(Pattern))

'''
inputFile ="dataset_198_3-2.txt"
outputFile = "answer.txt"

fOut = open(outputFile, 'w')

Pattern = [line.rstrip('\n') for line in open(inputFile)]

fOut.write(GenomePathProblem(Pattern))
fOut.close()
'''
