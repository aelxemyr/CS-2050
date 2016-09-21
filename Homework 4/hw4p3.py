# Bennett Alex Myers
# CS 2050 - Homework 4
# 3 April 2016

# Lee & Hubbard Section 7.9 Problem 3:
#     Write the code and perform Dijkstra's algorithm on the graph in Fig. 7.9
#     to find the minimum cost of visiting all other vertices from vertex 9 of
#     the graph.

import unittest
import xml.dom.minidom
import heapq

main = "__main__" == __name__

# Represents a vertex in a graph. Maintains an adjacency list (dictionary) which
# maps neighboring vertices to the weights corresponding to the edges to those
# vertices. Also maintains an attribute distance, which will be the key value
# in performing Dijkstra's algorithm, initialized to 9999.
class Vertex:
    def __init__(self,vertexId,label):
        self.vertexId = vertexId
        self.label = label
        self.adjacent = {}
        self.distance = 9999
        self.previous = None
        
# Represents a weighted, undirected graph (as per specification for performing
# Dijkstra).
class Graph:

    # Ininitializes the graph by processing an .xml file containing graph data.
    # Vertices are maintained in a dictionary mapping vertex IDs to vertices.    
    def __init__(self,graphFile):
            self.vertices = {}
            try:
                self.addVertices(graphFile)
                self.addEdges(graphFile)
            except IOError:
                print("Invalid input file. Please use a valid .xml file")
    
    # Creates vertex objects based on vertex data in graph file and stores them
    # in ID to vertex mapping.
    # Exception handling in place to ensure valid data.
    def addVertices(self,graphFile):
        graph = xml.dom.minidom.parse(graphFile)
        try:
            vertices = graph.getElementsByTagName("Vertices")[0]
            vList = vertices.getElementsByTagName("Vertex")
            for vertex in vList:
                vertexId = str(vertex.getAttribute("vertexId"))
                label = str(vertex.getAttribute("label"))
                v = Vertex(vertexId,label)
                self.vertices[vertexId] = v
        except:
            print("The .xml file does not contain proper vertex data." + 
                  " Please use a properly formatted graph .xml file.")

    # Populates adjacency lists of vertices based on edge data.
    # Exception handling in place to ensure valid data.    
    def addEdges(self,graphFile):
        graph = xml.dom.minidom.parse(graphFile)
        try:
            edges = graph.getElementsByTagName("Edges")[0]
            eList = edges.getElementsByTagName("Edge")
            for edge in eList:
                tail = str(edge.getAttribute("tail"))
                head = str(edge.getAttribute("head"))
                weight = float(str((edge.getAttribute("weight"))))
                self.vertices[tail].adjacent[self.vertices[head]] = weight
                self.vertices[head].adjacent[self.vertices[tail]] = weight
        except:
            print("The .xml file does not contain proper edge data." +
                  " Please use a properly formatted graph .xml file.")
   
    # Dijkstra's algorithm (source: Cormen, et al., Introduction to Algorithms)    
    def dijkstra(self,s):
        source = self.vertices[s]
        source.distance = 0
        visited = set()
        unvisited = minPriorityQueue()
        
        # Populated unvisited queue with all vertices
        for n,v in self.vertices.items():
            unvisited.push(v,v.distance)
        unvisited.heapify()
        
        # Main loop. Extracts minimum element from queue, adds it to the visited
        # set, and processes its adjacent vertices.
        while len(unvisited):
            current = unvisited.pop()[1]
            visited.add(current)
            
            # Relaxation operation. Updates shortest path estimates to vertices.
            for v in current.adjacent:
                if not v in visited:
                    if v.distance > current.distance + current.adjacent[v]:
                        v.distance = current.distance + current.adjacent[v]
                        v.previous = current
                        
            # After priorities have been updated, rebuild the queue to ensure
            # min priority queue property.
            unvisited = self.rebuildQueue(unvisited)
            
        # Calculate minimum cost of visiting all vertices. For each vertex in
        # the spanning tree with a parent, add the weight of the edge from the
        # vertex to the parent to the cost. Finally, return this cost.
        cost = 0
        for v in visited:
            p = v.previous
            if not p == None:
                d = v.adjacent[p]
                cost += d
        return cost
    
    # Rebuild the min priority queue after priorities have been updated to
    # maintain the min priority queue property. Pop every element and store in
    # a temporary list. Then push them all back in with updated priorities and
    # heapify.
    def rebuildQueue(self,queue):
        temp = []
        while len(queue):
            temp.append(queue.pop()[1])
        for v in temp:
            queue.push(v,v.distance)
        queue.heapify()
        return queue
                 
# Min priority queue implementation using heapq.   
class minPriorityQueue:
    
    # Initialize queue as empty list.
    def __init__(self):
        self.queue = []
        
    # Push item as tuple of priority and the item.
    def push(self, item, priority):
        heapq.heappush(self.queue, (priority,item))
        
    # Pop the minimum item in this queue.
    def pop(self):
        return heapq.heappop(self.queue)
    
    # Transform queue into heap, in-place. (From heapq documentation.)
    def heapify(self):
        heapq.heapify(self.queue)
    
    # Return the length of the queue.
    def __len__(self):
        return len(self.queue)
     
# Unit tests
class testGraph(unittest.TestCase):
    
    # Test for correct initialization on test .xml file.
    def testInit(self):
        g = Graph("testGraph.xml")
        # Test that vertex IDs match correct vertices with correct labels.
        self.assertEquals(g.vertices['0'].label, '1')
        self.assertEquals(g.vertices['1'].label, '2')
        self.assertEquals(g.vertices['2'].label, '3')
        self.assertEquals(g.vertices['3'].label, '4')
        self.assertEquals(g.vertices['4'].label, '5')
        
        # Test to see if vertex 3 has the correct adjacency list.
        adjLabelList = []
        for v in g.vertices['2'].adjacent:
            adjLabelList.append(v.label)
        self.assertEquals(adjLabelList,['4','1','5'])
        
        # Test to see if vertex 3's adjacency list has the correct weights.
        a = g.vertices['0']
        b = g.vertices['3']
        c = g.vertices['4']
        self.assertEquals(g.vertices['2'].adjacent[a],1.6)
        self.assertEquals(g.vertices['2'].adjacent[b],1.5)
        self.assertEquals(g.vertices['2'].adjacent[c],1.2)        
        
    
    # Test to see if Dijkstra executes properly on small graph for which the
    # minimum spanning tree is unique.
    def testDijkstra(self):
        g = Graph("testGraph.xml")
        self.assertEquals(g.dijkstra('0'),7.5)

# Main program.
if main:
    
    # Create graph using given .xml file.
    g = Graph("graph.xml")
    
    # Print out the minimum cost of visiting every vertex from vertex 9 (vertex
    # ID 16).
    print(g.dijkstra('16'))