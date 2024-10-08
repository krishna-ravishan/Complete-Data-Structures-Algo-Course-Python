# All pairs shortest path problem

# In case of single source shortest path we are required to find a path between a given vertex called source to all other vertices in a graph such that the total distance between them is minimum. Eg: Five office in different cities, travel cost between these cities is known and find the cheapest way to head from head office to branches in diff cities.

# All pairs shortest path problem is about finding a path between every vertex to all other vertices in a graph such that the total distance between thm is minimum.

# We run this algorithm V times where V is the number of vertices.

# Floyd Warshall algorithm

# If D[u][v] > D[u][viaX] + D[viaX][v]:
#     D[u][v] = D[u][viaX] + D[viaX][v]

# Continue this iteration for V*E times. You'll get a table of the shortest path between all pairs.

# Why floyd warshall? The vertex is not reachable, two vertices are directly connected and two vertices are connected via other vertex.


# Floyd Warshall with Negative Cycle: Does not work with negative cycle.

# This is because to go through cycle we need to go via negative cycle participating vertex at least twice, FW never runs loop twice via same vertex and hence fW can never detect a negative cycle.

INF = 9999
# Printing the solution
def printSolution(nV, distance):
    for i in range(nV):
        for j in range(nV):
            if(distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")


def floydWarshall(nV, G):
    distance = G
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])
    
    printSolution(nV, distance)

G = [[0, 8, INF,1],
    [INF, 0, 1,INF],
    [4, INF, 0,INF],
    [INF, 2, 9,1]
    ]

floydWarshall(4, G)

# Rest vs Floyd Warshall

# Can be used for unweighted grpahs and is prefered for weighted graphs as implementation is easy.