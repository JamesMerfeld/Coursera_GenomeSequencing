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

def GetPrefix(kMer):
    k = len(kMer)
    return kMer[0:k-1]

def GetSuffix(kMer):
    k = len(kMer)
    return kMer[1:]

def Overlap(Pattern):
    adjList = []
    l = len(Pattern)
    for i in range(l):
        for j in range(l):
            if GetSuffix(Pattern[i]) == GetPrefix(Pattern[j]):
                adjList.append(Pattern[i] + " -> " + Pattern[j])
    return adjList

def Overlap2(Pattern):
    adjList = dict()
    l = len(Pattern)
    for i in range(l):
        tmp = []
        for j in range(l):
            if GetSuffix(Pattern[i]) == GetPrefix(Pattern[j]):
                tmp.append(Pattern[j])
        if tmp:
            adjList[Pattern[i]] = tmp
    return adjList

def GenerateAndPrintAdjacencyList(Pattern):
    adjList = Overlap2(Pattern)
    for p in Pattern:
        print p + " : " + str(adjList[p])

Pattern = ["000","001","010","011","100","101","110","111"]
#Pattern = ["00","01","10","11"]
#Pattern = ["ATGCG", "GCATG", "CATGC", "AGGCA", "GGCAT"]

Pattern = ["0000","0001","0010","0011","0100","0101","0110","0111","1000","1001","1010","1011","1100","1101","1110","1111"]

#GenerateAndPrintAdjacencyList(Pattern)

print(len("0000100110101111000"))

'''
Pattern = ["ATGCG", "GCATG", "CATGC", "AGGCA", "GGCAT"]

output = Overlap(Pattern)
for kmer in output:
    print kmer
'''

'''
inputFile ="dataset_198_9.txt"
outputFile = "answer.txt"

fOut = open(outputFile, 'w')

Pattern = [line.rstrip('\n') for line in open(inputFile)]

#fOut.write(GenomePathProblem(Pattern))
output = Overlap(Pattern)
for kMer in output:
    fOut.write(kMer + '\n')
fOut.close()
'''
