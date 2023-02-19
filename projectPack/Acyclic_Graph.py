"""
    File name: Acyclic_Graph.py
    Team: Conti 0245745.
    Members: Carlo Nicola Cavazzini & Giovanni Maria Cipriano & Riccardo Conti.
    Date created: 04/01/2018.
    Date last modified: 20/01/2018.

    This module implements a graph without close paths,
    implemented by adjacency lists, and with a method to gather
    those nodes which are most frequent middle nodes in a Graph.
"""



from structures.graphPack.Graph_AdjacencyList import GraphAdjacencyList
from structures.graphPack.Base import Edge, Node


class AcyclicGraph(GraphAdjacencyList):
    """
    AcyclicGraph() -> new empty acyclic graph

    
    Acyclic undirected Graphs through adjacency lists *.
    Memory Complexity: O(|V| + |E|), where 'V' is the set of vertexs and,
    'E' is the set of un-oriented edges.

    *   By 'acyclic', we mean that the graph has the structure of a tree,
        or a forest of trees.

    For further info, see:
        'https://en.wikipedia.org/wiki/Tree_(graph_theory)'.

    
    ----------------------------------------------------------------------
    Methods defined here:

    getMiddles(self)
        Return a list of most frequent middle nodes (for further info, see the relation).

    getNbrOfCouples(self, nodeId)
        Return how many times a node is middle in the graph (for further info, see the relation).

    __init__(self)
        Initialize self (as empty graph).

    __str__(self)
        Call self.print() and return an empty string.

    areConnected(self, tailId, headId)
        Check if two nodes are already connected.

    deleteEdge(self, tail, head)
        Remove the specified edge.

    insertEdge(self, tail, head, weight = None, doTests = True)
        Adds a new edge, if it's necessary or possible.
        (You can override some checks by setting 'doTests' to False)

    isLeaf(self, nodeId)
        Check if a node is a leaf (if it has just one adjacent node).

    getNbrOfEdges(self)
        Return the number of edges in the graph.
    """


    def getMiddles(self):
        """
        Return a list of most frequent middle nodes (for further info, see the relation).

        :return: <<List>> of nodes.
        """

        # List of the candidated nodes.
        theMiddles = []
        theHighestDensity = 0

        for currentNode in self.nodes:
            # Calculate the density of the graph in node 'currentNode'.
            currentDensity = self.getNbrOfCouples(currentNode)

            # If We find a better candidate, the prevoius ones can be forgotten.
            if theHighestDensity < currentDensity:
                theHighestDensity = currentDensity
                theMiddles = [currentNode]

            # Elif We find a candidate with same density, let's keep it.
            elif theHighestDensity == currentDensity:
                theMiddles.append(currentNode)

            # Else ...
                # Nothing left to do except from going on xor exit the 'for' statement.

        return theMiddles


    def getNbrOfCouples(self, nodeId):
        """
        Return how many times a node is middle in the graph (for further info, see the relation).

        :param nodeId: the node You'd like to know how many times is middle in the graph <<Integer>>.
        :return: <<Float>>.
        """

        theFamilies = self.getAdj(nodeId)

        # Try to retrieve the second element of the adjacency List of 'nodeId'.
        try:
            # So, We suppose that 'nodeId' has more then one adjacent node. 
            myBin = theFamilies[1]
        
        except IndexError:
            # On IndexError, the 'nodeId' is a leaf because it has just one adjacent node (so indexing the second one, fails), and ...
            # ... now, We have to return 0 as 'nodeId' is 'middle node' for no couples of nodes.
            return 0
        
        else:
            # If You do not encountered any exception, the second node is surrounded by at least TWO nodes, and ...
            # ... now, We have to delete the found one.
            del myBin

        # Get the contribute from closest nodes (how many couples between 'nbrOfFamilies' elements?).
        nbrOfFamilies = len(theFamilies)
        finalResult = nbrOfFamilies * (nbrOfFamilies - 1) / 2

        # Let's consider 'nodeId' and its closest nodes, as 'visited'.
        visitedNodes = {nodeId}
        for i in theFamilies:
            visitedNodes.add(i)

        # From closest nodes, look for further relatives ...
        for family in range(0, nbrOfFamilies):
            # Retrieve one new generation.
            nextGen = self.getAdj(theFamilies[family])

            # But forgot the past!
            nextGen.remove(nodeId)

            # Let's also consider the new generation, as 'vivisted'.
            for i in nextGen:
                visitedNodes.add(i)

            # And let's now swap the close node with its sons.
            theFamilies[family] = nextGen

        # Calculate number of couples of the second generation-level nodes (
        # for each family,
        #    for each other family,
        #       contribute = nbrOfSonsAtFirstFamily * nbrOfSonsOfAtSecondsOtherFamilies
        # ).
        couplesFromGeneration = 0
        for x in range(0, len(theFamilies) - 1):
            for y in range(x + 1, len(theFamilies)):
                couplesFromGeneration += len(theFamilies[x]) * len(theFamilies[y])

        # Update contribution.
        finalResult += couplesFromGeneration

        # While there has been contributions,
        while couplesFromGeneration != 0:
            # Let's get deeper in the generation tree, as ...
            # ... for each family,
            for family in range(0, nbrOfFamilies):
                nextGen = []

                # For each son-node in the families,
                for node in range(0, len(theFamilies[family])):

                    # Let's retrieve its sons, and ...
                    l = self.getAdj(theFamilies[family][node])

                    # ... remove the greatfathers (those visited nodes, those where I came from), and ...
                    for vertex in l:
                        if vertex in visitedNodes:
                            l.remove(vertex)

                    # ... then put them in the next generation.
                    nextGen += l

                # Let's finally consider the last retreived generation, as 'vivisted'. 
                for i in nextGen:
                    visitedNodes.add(i)

                # Here You have the 'step' in the above 'while' statement.
                theFamilies[family] = nextGen

            # Calculate the number of couples of the next generation-level nodes.
            couplesFromGeneration = 0
            for x in range(0, len(theFamilies) - 1):
                for y in range(x + 1, len(theFamilies)):
                    couplesFromGeneration += len(theFamilies[x]) * len(theFamilies[y])

            # Update contribution.
            finalResult += couplesFromGeneration

        return finalResult


    def __init__(self):
        # Call the initializer of the 'super()' class.
        super().__init__()


    def __str__(self):
        # Call the inherited method aided for prints.
        # (will print the adjacency lists)
        self.print()
        return ""


    def areConnected(self, tailId, headId):
        """
        Checks if two nodes are already connected.

        :param tailId: the tail node ID <<Integer>>.
        :param headId: the head node ID <<Integer>>.
        :return: <<Bool>>.
        """

        # Let's get the 'BFS' list of nodes linked to the tail 'tailId'.
        graphPic = self.bfs(tailId)

        # If the head is could be reached from the tail,
        if headId in graphPic:
            # Tail and head are already connected!
            return True

        else:
            # Tail and head aren't connected yet!
            return False


    def deleteEdge(self, tail, head):
        """
        Remove the specified edge.

        :param tail: the tail node ID <<Integer>>.
        :param head: the head node ID <<Integer>>.
        :return: <<None>>.
        """

        # If both 'tail' and 'head' exist,
        if tail in self.nodes and head in self.nodes:
            currTail = self.adj[tail].getFirstRecord()
            currHead = self.adj[head].getFirstRecord()

            # Look for the 'head' in the adjacency list of the 'tail' and delete it.
            while currTail is not None:
                if currTail.elem == head:
                    self.adj[tail].deleteRecord(currTail)
                    break
                currTail = currTail.next

            # Look for the 'tail' in the adjacency list of the 'head' and delete it.
            while currHead is not None:
                if currHead.elem == tail:
                    self.adj[head].deleteRecord(currHead)
                    break
                currHead = currHead.next
        else:
            print("'AcyclicGraph().deleteEdge(tail, head)' says:")
            print("\tWarning! At least one of both head or tail doesn't exists, so edge couldn't be removed!")


    def insertEdge(self, tail, head, weight = None, doTests = True):
        """
        Adds a new edge, if it's necessary or possible.
        (You can override some checks by setting 'doTests' to False)

        :param tail: the tail node ID <<Integer>>.
        :param head: the head node ID <<Integer>>.
        :param weight: the (optional) edge weight <<Float>>.
        :param doTests: the (optional) bool value which will override some checks <<Bool>>.
        :return: <<None>>.
        """

        # If both nodes belong to the graph, and ...
        if tail in self.nodes and head in self.nodes:

            # ... if they're already connected by a path
            if doTests and self.areConnected(tail, head):
            # if self.areConnected(tail, head):
                print("'AcyclicGraph().insertEdge(tail, head, weight = None)' says:\n"
                      "\tWarning! Nodes are alredy connected!")
                
                # Do not insert the edge.
                return
            else:

                # 'head' added to adjancency List of 'tail'.
                self.adj[tail].addAsLast(head)
                # 'tail' adde to adjancency List of 'head'.
                self.adj[head].addAsLast(tail)
                
                # The edge has been created!
                return
        else:
            print("'AcyclicGraph().insertEdge(tail, head, weight = None)' says:\n"
                  "\tWarning! At least one of both tail and head doesn't exist, so they couldn't be linked!")

            # Can't insert the edge.
            return


    def isLeaf(self, nodeId):
        """
        Checks if a node is a leaf (if it has just one adjacent node).

        :param nodeId: the node ID <<Integer>>.
        :return: <<Bool>>.
        """
        
        # Try to retrieve the second element of the adjacency List of 'nodeId'.
        try:
            # So, We suppose that 'nodeId' has more then one adjacent node. 
            myBin = self.getAdj(nodeId)[1]
        
        except IndexError:
            # On IndexError, the 'nodeId' is a leaf because it has just one adjacent node (so indexing the second one, fails), and ...
            # ... now, We have to return 'True'.
            return True
        
        else:
            # If You do not encountered any exception, the second the node is a surrounded by at least TWO nodes, and ...
            # ... now, We have to delete the found one and return 'False'.
            del myBin
            return False


    def getNbrOfEdges(self):
        """
        Return the number of edges in the graph.

        :return: <<Float>>.
        """

        return (sum(len(adj_list) for adj_list in self.adj.values())) / 2
        # OBSERVATION: the graph is 'undirected', so We have to divide the above sum by two. 





if __name__ == "__main__":

    print(">>> # Welcome! Here You have a simple demo.")

    # Initialize class instance.
    print(">>> myGraph = AcyclicGraph()")
    theExampleGraph = AcyclicGraph()
    print(">>> print(myGraph)")
    theExampleGraph.print()

    # Add two nodes and link them.
    print(">>> myGraph.addNode(0)")
    itsBin = theExampleGraph.addNode(0)
    print(">>> myGraph.addNode(1)")
    itsBin = theExampleGraph.addNode(1)
    print(">>> myGraph.insertEdge(0, 1)")
    theExampleGraph.insertEdge(0, 1)
    print(">>> print(myGraph)")
    theExampleGraph.print()
