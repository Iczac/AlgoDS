import sys
import threading

# configure
sys.setrecursionlimit(100000)
threading.stack_size(67108864)  # call-stack memory allocation

# GLOBAL vars
maxvertex = None
vertex = None
edges = None
edges_reversed = None
isexplored1, isexplored2  = None, None
visitordered = None
maxscc = None


def dfs_reverse(vertexindex):
    global maxvertex, edges_reversed, isexplored1, visitordered

    if len(edges_reversed[vertexindex]) > 0:
        for index in edges_reversed[vertexindex]:
            if not isexplored1[index-1]:
                isexplored1[index-1] = True
                dfs_reverse(index)

    visitordered[maxvertex-1] = vertexindex
    maxvertex -= 1


def dfs_normal(vertexindex):
    global vertex, edges, isexplored2, maxscc

    if len(edges[vertexindex]) == 0:
        return

    for index in edges[vertexindex]:
        if not isexplored2[index-1]:
            isexplored2[index-1] = True
            dfs_normal(index)

    maxscc[vertex-1] += 1


def kosaraju():
    global vertex, isexplored1, isexplored2

    # first DFS (normal)
    for index in range(1, maxvertex+1):
        if not isexplored1[index-1]:
            isexplored1[index-1] = True
            dfs_reverse(index)

    for index in visitordered:
        if not isexplored2[index-1]:
            vertex = index
            isexplored2[index-1] = True
            dfs_normal(index)

    maxscc.sort(reverse=True)
    print "Top 5 max SCCs: " + str(maxscc[0:5])


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "python kosaraju.py file.txt maxvertex"
        exit(1)

    maxvertex = int(sys.argv[2])
    edges = {x:[] for x in range(1, maxvertex+1)}
    edges_reversed = {x:[] for x in range(1, maxvertex+1)}

    # add edges into edge list
    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            tmp = [int(x) for x in line.split()]
            edges[tmp[0]].append(tmp[1])
            edges_reversed[tmp[1]].append(tmp[0])

    isexplored1 = [False for x in range(1, maxvertex+1)]
    isexplored2 = [False for x in range(1, maxvertex+1)]
    visitordered = [0 for x in range(1, maxvertex+1)]
    maxscc = [0 for x in range(1, maxvertex+1)]

    thread=threading.Thread(target=kosaraju)
    thread.start()
