# Bennett Alex Myers
# CS 2050 - Homework 4
# 3 April 2016

# Lee & Hubbard Section 7.9 Problem 1:
#     Write a program to find a path between vertex 9 and 29 in the graph shown
#     in Fig. 7.9. Be sure to print the path (i.e., the sequence of vertices) 
#     that must be traversed in the path between the two vertices.

import unittest
import xml.dom.minidom

main = "__main__" == __name__

# Represents a vertex in a graph. Maintains an adjacency list of neighbors.
class Vertex:
    def __init__(self,vertexId,label):
        self.vertexId = vertexId
        self.label = label
        self.adjacent = []
        self.previous = None

# Represents a unweighted, directed graph.
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
                self.vertices[tail].adjacent.append(self.vertices[head])
        except:
            print("The .xml file does not contain proper edge data." +
                  " Please use a properly formatted graph .xml file.")
    
    # Path search algorithm.        
    def findPath(self,start,goal):
        s = self.vertices[start]
        g = self.vertices[goal]
        stack = []
        visited = set()
        stack.append(s)
                
        # Main loop. Performs a depth-first search using a stack to backtrack.
        while not stack == []:
            current = stack.pop()
            visited.add(current)
            
            if current == g:
                node = g
                path = [node.label]
                while not node.previous == None:
                    node = node.previous
                    path.append(node.label)
                    
                path.reverse()
                return path
            
            for v in current.adjacent:
                if not v in visited:
                    stack.append(v)
                    v.previous = current
                    
        # Return false if no path exists.
        return False
            
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
        self.assertEquals(adjLabelList,['4','5'])
    
    # Test to see if simple path can be found using test .xml file.
    def testFindPath(self):
        g = Graph("testGraph.xml")
        self.assertEquals(g.findPath('0','4'),['1','3','5'])

# Main program
if main:
    
    # Create graph using given .xml file.
    g = Graph("graph.xml")
    
    # Find a path from vertex 9 to 29 (vertex ID 16 and 18, respectively).
    path = g.findPath('16','18')
    
    # Convert path list into user-friendly output.
    pathStr = path[0]
    i = 1
    while i < len(path):
        pathStr += " --> " + path[i]
        i += 1
    print("The following path exists between vertex 9 and 29:\n" + pathStr)