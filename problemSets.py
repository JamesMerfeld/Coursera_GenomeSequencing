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

def PathGraph(Text, k):
    c = Composition(Text,k)
    p = []
    l = len(Text)
    for kmer in c:
        p.append(kmer[0:k-1])
    p.append(c[len(c)-1][1:])
    return p

def DeBruijn(Text,k):
    adjList = dict()
    pg = PathGraph(Text, k)
    l = len(pg)
    for i in range(l-1):
        key = pg[i]
        if key in adjList:
            adjList[pg[i]].append(pg[i+1])
        else:
            newList = []
            newList.append(pg[i+1])
            adjList[pg[i]] = newList
    return adjList

def DeBruijn(Patterns):
    adjList = dict()
    for pattern in Patterns:
        prefix = GetPrefix(pattern)
        suffix = GetSuffix(pattern)
        if prefix not in adjList:
            newList = []
            newList.append(suffix)
            adjList[prefix] = newList
        else:
            adjList[prefix].append(suffix)
    return adjList

def PrintAdjList(adjList):
    first = 0
    for key in adjList:
        out = key + " -> "
        for k in adjList[key]:
            if not first:
                out += k
                first = 1
            else:
                out += ", " + k
        first = 0
        print out

'''
Patterns = ["GAGG","CAGG","GGGG","GGGA","CAGG","AGGG","GGAG"]
PrintAdjList(DeBruijn(Patterns))
'''

'''
inputFile ="dataset_200_7-2.txt"
outputFile = "answer.txt"

fOut = open(outputFile, 'w')

Patterns = [line.rstrip('\n') for line in open(inputFile)]

adjList = DeBruijn(Patterns)
print adjList

first = 0
for key in adjList:
    out = key + " -> "
    for k in adjList[key]:
        if not first:
            out += k
            first = 1
        else:
            out += "," + k
            #out += ", " + k
    first = 0
    fOut.write(out + '\n')

fOut.close()

inputFile1 ="answer.txt"
inputFile2 ="answerCorrect.txt"

in1 = [line.rstrip('\n') for line in open(inputFile1)]
print len(in1)
in2 = [line.rstrip('\n') for line in open(inputFile2)]
print len(in2)


for line in in1:
    if line not in in2:
        print "in1, not in2: " + line

for line in in2:
    if line not in in1:
        print "in2, not in1: " + line
'''