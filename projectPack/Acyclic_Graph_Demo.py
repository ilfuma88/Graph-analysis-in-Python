"""
    File name: Acyclic_Graph_Demo.py
    Team: Conti 0245745.
    Members: Carlo Nicola Cavazzini & Giovanni Maria Cipriano & Riccardo Conti.
    Date created: 19/01/2018.
    Date last modified: 22/01/2018.

    This module implements a demo for graphs without close paths,
    implemented with the class AcyclicGraph.
"""



from Acyclic_Graph import AcyclicGraph


class GraphCtors(AcyclicGraph):
    """
    GraphCtors() -> new empty acyclic graph

    
    Some constructors for the class 'Acyclic_Graph.AcyclicGraph'.
    See 'Acyclic_Graph.AcyclicGraph' for further info.

    
    ----------------------------------------------------------------------
    Methods defined here:

    reset(self)
        Reinitialize the graph dictionaries.
    
    setDisk(self, a = 5, s = 7)
        Seed a tree with 5 branches and 7 leaves each branch.

    setDots(self, n = 100)
        Add one hundred un-linked nodes.

    setLine(self, n = 100)
        Add one hundred nodes in row.

    setSphere(self, b = 7, e = 5)
        Seed a tree of 6 generations and 7 sons each node.

    setStar(self, a = 5, r = 7)
        Seed a tree with 5 branches of 7 nodes.


    ----------------------------------------------------------------------
    Not implemented methods descripted here:

    setRandGraph(self, theString = '')
        Builds a graph from a string. Here You have some example syntaxs:
            - A 'line' graph is '[12]';
            - A 'star' graph is '[1, [3], [3], [3], [3]]';
            - A 'spheric' graph is '[1, [3, [9, [27, [81]]]]]'.


    ----------------------------------------------------------------------
    Data descriptors defined here:
        
        See 'Acyclic_Graph.AcyclicGraph' for further info.
    """


    def __init__(self):
        super().__init__()


    def reset(self):
        """
        Re-initialize the graph dictionaries.
        
        :return: <<None>>.
        """

        # if 'y' == input("Are You sure to reset the Graph? Press 'Y' to continue.\n").lower():
        try:
            del self.nodes
            # self.nodes.clear()
        except NameError:
            pass

        try:
            del self.adj
            # self.adj.clear()
        except NameError:
            pass

        self.__init__()


    def setDisk(self, a = 5, s = 7):
        """
        Seed a tree with 5 branches and 7 leaves each branch.

        :param a: the number of branches <<Integer>>.
        :param s: the number of sons each branch <<Integer>>.
        :return: <<None>>.
        """

        if a <= 0 or s <= 0:
            # Delete previous inserts (both nodes and edges).
            self.reset()

        else:
            # Just a sort of kind reminder.
            if 1000000 < a * s:
                print("'AcyclicGraph().setDisk(a, s)' says:\n"
                      "\tHey! You'll have more then one million nodes!\n"
                      "\tPlease, be sure You have enough memory!!\n"
                      "\t(2.000.000 nodes need at least 2GB)")

            # Delete previous inserts (both nodes and edges), and ...
            # ... add a root node.
            self.reset()
            self.addNode(0)

            # Seed 'a' branches.
            for i in range(1, a + 1):
                self.addNode(i)
                self.insertEdge(0, i, None, False)

            # Grow up the branches.
            for j in range(a + 1, a * (s + 1) + 1):
                self.addNode(j)
                self.insertEdge(j % a + 1, j, None, False)


    def setDots(self, n = 100):
        """
        Add one hundred un-linked nodes.

        :param n: the number of un-linked nodes <<Integer>>.
        :return: <<None>>.
        """

        # Just a sort of kind reminder.
        if 1000000 < n:
            print("'AcyclicGraph().setDots(n)' says:\n"
                  "\tHey! You'll have more then one million nodes!\n"
                  "\tPlease, be sure You have enough memory!!\n"
                  "\t(2.000.000 nodes need at least 2GB)")

        self.reset()

        for i in range(n):
            self.addNode(i)


    def setLine(self, n = 100):
        """
        Add one hundred nodes in row.

        :param n: the number of row nodes <<Integer>>.
        :return: <<None>>.
        """
        
        # Just a sort of kind reminder.
        if 1000000 < n:
            print("'AcyclicGraph().setLine(n)' says:\n"
                  "\tHey! You'll have more then one million nodes!\n"
                  "\tPlease, be sure You have enough memory!!\n"
                  "\t(2000000 nodes need at least 2GB)")
        
        # Delete previous inserts (both nodes and edges).
        self.reset()

        # Add a starting node, and ...
        # ... add 'n' nodes in row.
        self.addNode(0)
        for i in range(1, n):
            self.addNode(i)
            self.insertEdge(i - 1, i, None, False)


    def setSphere(self, b = 7, e = 5):
        """
        Seed a tree of 6 generations with 7 sons each node.
        (e.g. 'sum(7 ** i for i in range(5 + 1)) == 19608')

        :param b: the number of sons that every node will have <<Integer>>.
        :param e: the number of generations <<Integer>>.
        :return: <<None>>.
        """
        
        if e < 0 or b < 2:
            # Delete previous inserts (both nodes and edges).
            self.reset()

        else:
            # Just a sort of kind reminder.
            if 1000000 < sum(b ** i for i in range(e + 1)):
                print("'AcyclicGraph().setSphere(b, e)' says:\n"
                      "\tHey! You'll have more then one million nodes!\n"
                      "\tPlease, be sure You have enough memory!!\n"
                      "\t(2000000 nodes need at least 2GB)")

            # Delete previous inserts (both nodes and edges).
            self.reset()

            prevLevel = []
            currLevel = []

            # Add the leaves.
            for i in range(b ** e):
                prevLevel.append(self.nextId)
                self.addNode(self.nextId)

            # Add the inner nodes, inner level by inner level.
            for i in range(e - 1, -1, -1):
                for j in range(b ** i):
                    currLevel.append(self.nextId)
                    self.addNode(self.nextId)
                for j in range(0, b ** (i + 1), b):
                    for k in range(b):
                        self.insertEdge(currLevel[j // b], prevLevel[j + k], None, False)
                prevLevel = currLevel
                currLevel = []
            
            del prevLevel


    def setStar(self, a = 5, r = 7):
        """
        Seed a tree with 5 branches of 7 nodes.

        :param a: the number of branches of the star <<Integer>>.
        :param r: the number of nodes in row of each branch <<Integer>>.
        :return: <<None>>.
        """

        if a < 0 or r < 0:
            # Delete previous inserts (both nodes and edges).
            self.reset()

        else:
            # Just a sort of kind reminder.
            if 1000000 < a * r:
                print("'AcyclicGraph().setDisk(a, r)' says:\n"
                      "\tHey! You'll have more then one million nodes!\n"
                      "\tPlease, be sure You have enough memory!!\n"
                      "\t(2.000.000 nodes need at least 2GB)")

            # Delete previous inserts (both nodes and edges), and ...
            # ... add a root node.
            self.reset()
            self.addNode(0)

            # Seed 'a' branches.
            for i in range(1, a + 1):
                self.addNode(i)
                self.insertEdge(0, i, None, False)
            
            # Grow up the branches.
            for i in range(a + 1, a * r + 1):
                self.addNode(i)
                self.insertEdge(i - a, i, None, False)
            

    def setRandGraph(self, theInput = None):
        """
        Build up a graph starting from a string, but ...
        ... if no string is given, it builds a random acyclic graph.

        :param theInput: the (optional) string which represents the DFS of graph <<Integer>>.
        :return: <<None>>.
        """

        raise NotImplementedError("You should have implemented this method!")
        # E.g. syntax for a 'line' graph: [12].
        # E.g. syntax for a 'star' graph: [1, [3], [3], [3], [3]].
        # E.g. syntax for a 'spheric' graph: [1, [3, [9, [27, [81]]]]].


def main():
    print("\n\n################################")
    print("Welcome, this demo will run some tests.\n"
          "Some fake line comands will be printed by build-in\n"
          "function 'input', so, right now, You have to just keep\n"
          "going on by pressing 'ENTER' on your keyboard.\n"
          "(later, You'll receive more info)\n")
    theBin = input("Please, press any key to start the demo.\n>>> ")


    # Initialize class instance.
    theBin = input(">>> myGraph = AcyclicGraph()")
    theAcyclicGraph = GraphCtors()
    theBin = input(">>> print(myGraph)")
    theAcyclicGraph.print()

    # Add nodes.
    theBin = input(">>> # adding 15 nodes in background #")
    for i in range(15):
        node = theAcyclicGraph.addNode(i)

    theBin = input(">>> print(myGraph)")
    theAcyclicGraph.print()

    # Link the nodes.
    theBin = input(">>> # adding 14 double-edges in background #")
    theAcyclicGraph.insertEdge(0, 1)
    theAcyclicGraph.insertEdge(0, 2)
    theAcyclicGraph.insertEdge(0, 4)
    theAcyclicGraph.insertEdge(0, 5)
    theAcyclicGraph.insertEdge(0, 8)
    theAcyclicGraph.insertEdge(3, 0)
    theAcyclicGraph.insertEdge(3, 6)
    theAcyclicGraph.insertEdge(3, 7)
    theAcyclicGraph.insertEdge(9, 6)
    theAcyclicGraph.insertEdge(9, 12)
    theAcyclicGraph.insertEdge(9, 13)
    theAcyclicGraph.insertEdge(10, 9)
    theAcyclicGraph.insertEdge(11, 4)
    theAcyclicGraph.insertEdge(14, 9)

    theBin = input(">>> print(myGraph)")
    theAcyclicGraph.print()

    # Get some densities
    theBin = input(">>> myGraph.getNbrOfCouples(0)")
    print(theAcyclicGraph.getNbrOfCouples(0))
    theBin = input(">>> myGraph.getNbrOfCouples(3)")
    print(theAcyclicGraph.getNbrOfCouples(3))
    theBin = input(">>> myGraph.getNbrOfCouples(5)")
    print(theAcyclicGraph.getNbrOfCouples(5))
    theBin = input(">>> myGraph.getNbrOfCouples(6)")
    print(theAcyclicGraph.getNbrOfCouples(6))
    theBin = input(">>> myGraph.getNbrOfCouples(9)")
    print(theAcyclicGraph.getNbrOfCouples(9))

    # Get most frequent middle node.
    theBin = input(">>> myGraph.getMiddles()")
    print(theAcyclicGraph.getMiddles())



    # Get sample times.
    print("\n\n################################")
    if 'y' == input("Some sample times will be stored on your computer (no more then 5KB).\n"
                    "This mean You need at least 2GB of free RAM space and\n"
                    "just a few minutes to run the tests (graphs could be discontinuous\n"
                    "because of the few tests).\n"
                    "Please, press 'y' on your keyboard to continue.\n>>> ").lower():


        from time import time, gmtime, strftime
        localPath = ''
        fileIsnTLocated = True

        print("Trying to locate 2 files...\n"
              "\tconti_0245745_samples.csv\n"
              "\tconti_0245745_samples.m")
        while fileIsnTLocated:
            localPath = input("Please, write down the path where to store both files.\n(write 'None' to skip, otherwise no quotes, thanks!)\n>>> ")

            if localPath != "None":
                try:
                    theCSVF = open(localPath + "\\conti_0245745_samples.csv", "x")
                    theMathLabF = open(localPath + "\\conti_0245745_samples.m", "x")
                except FileNotFoundError:
                    print("Please, do not write a filepath, just path is needed.")
                except PermissionError:
                    print("Permission denied, try with another path (write 'None' to skip).")
                except FileExistsError:
                    print("Path is valid, but at least one file already exists...\n"
                          "They're going to be replaced, are You sure?")
                    if 'y' == input("Please, press 'y' on your keyboard to continue.\n>>> ").lower():
                        theCSVF = open(localPath + "\\conti_0245745_samples.csv", "w")
                        theMathLabF = open(localPath + "\\conti_0245745_samples.m", "w")

                        print("#", strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()), file = theCSVF)
                        print("'" + localPath + "\\conti_0245745_samples.csv'", "have been overwritten.")
                        print("%", strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()), file = theMathLabF)
                        print("'" + localPath + "\\conti_0245745_samples.m'", "have been overwritten.")

                        theCSVF = open(localPath + "\\conti_0245745_samples.csv", "a")
                        theMathLabF = open(localPath + "\\conti_0245745_samples.m", "a")

                    else:
                        theCSVF = open(localPath + "\\conti_0245745_samples.csv", "a")
                        theMathLabF = open(localPath + "\\conti_0245745_samples.m", "a")

                        print("################################\n#",
                              strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()),
                              "# SAMPLE TIMES START FROM HERE #\n", file = theCSVF)
                        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n%",
                              strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()),
                              "% SAMPLE TIMES START FROM HERE %\n", file = theMathLabF)
                        print("'" + localPath + "\\conti_0245745_samples.csv'", "won't be overwritten (writing data in append).")
                        print("'" + localPath + "\\conti_0245745_samples.csv'", "won't be overwritten (writing data in append).")
                    fileIsnTLocated = False
                except OSError:
                    print("Some OS error occured, try again (do not insert quotes or double quotes).")
                else:
                    print("#", strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()), file = theCSVF)
                    print("%", strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()), file = theMathLabF)

                    print("Path is valid, files created in: '" + localPath + "'.")
                    fileIsnTLocated = False

                
            else:
                fileIsnTLocated = False
                localPath = 'None'



        print("\n\n################################\n"
              "## Building a 'spheric' graph ##\n"
              "################################\n"
              "You'll see the algorithm run in O(n).\n")

        theBin = input("Please, press any key to continue.\n>>> ")

        u = []
        v = []
        for i in range(13):
            print("Running test #" + str(i + 1))
            u.append(sum(3 ** j for j in range(i + 1)))
            
            print("Initialization of " + str(u[i]) + " nodes...")
            startT = time()
            theAcyclicGraph.setSphere(3, i)
            print("Initialization completed in " + str(time() - startT) + " seconds.\nGoing with the test...")
            startT = time()
            theAcyclicGraph.getMiddles()
            v.append(time() - startT)
            print("Test completed in " + str(v[i]) + " seconds.\n")
            theAcyclicGraph.__init__()

        if localPath != 'None':
            print("Storing results...")

            theFirstStr = ""
            for i in range(13):
                theFirstStr += "sphere," + str(u[i]) + "," + str(v[i]) + "\n"

            print("\n# 'Few tests' means, discontinuous graphs...\n"
                  "graphType,nbrOfNodes,timeElapsed\n" + theFirstStr, file = theCSVF)

            print("\nx_1 = " + str(u) + ";\ny_a = " + str(v) + ";\n\n", file = theMathLabF)

            print("Store successful.")



        print("\n\n################################\n"
              "#### Building a 'line' graph ###\n"
              "################################\n"
              "You'll see the algorithm run in O(n ** 2).\n")

        theBin = input("Please, press any key to continue.\n>>> ")

        u = []
        v = []
        x0 = 0
        x1 = 500
        deltaX = (x1 - x0) // 10
        for i in range(x0, x1, deltaX):
            print("Running test #" + str((i // deltaX) + 1))
            u.append(i)
            
            print("Initialization of " + str(u[i // deltaX]) + " nodes...")
            startT = time()
            theAcyclicGraph.setLine(i)
            print("Initialization completed in " + str(time() - startT) + " seconds.\nGoing with the test...")
            startT = time()
            theAcyclicGraph.getMiddles()
            v.append(time() - startT)
            print("Test completed in " + str(v[i // deltaX]) + " seconds.\n")
            theAcyclicGraph.__init__()

        if localPath != 'None':
            print("Storing results...")

            theFirstStr = ""
            for i in range((x1 - x0) // deltaX):
                theFirstStr += "linear," + str(u[i]) + "," + str(v[i]) + "\n"

            print(theFirstStr, file = theCSVF)

            print("x_2 = " + str(u) + ";\ny_b = " + str(v) + ";\n\n", file = theMathLabF)

            print("Store successful.")



        print("\n\n################################\n"
              "### Building a 'radial' graph ##\n"
              "################################\n"
              "You'll see the algorithm run in O(n ** 2).\n"
              "MEMO: In this section, nodes on branches will be increased.\n")

        theBin = input("Please, press any key to continue.\n>>> ")

        u = []
        v = []
        costK = 5
        x0 = 0
        x1 = 100
        deltaX = (x1 - x0) // 10
        for i in range(x0, x1, deltaX):
            print("Running test #" + str((i // deltaX) + 1))
            u.append(1 + 5 * i)
            
            print("Initialization of " + str(u[i // deltaX]) + " nodes...")
            startT = time()
            theAcyclicGraph.setStar(costK, i)
            print("Initialization completed in " + str(time() - startT) + " seconds.\nGoing with the test...")
            startT = time()
            theAcyclicGraph.getMiddles()
            v.append(time() - startT)
            print("Test completed in " + str(v[i // deltaX]) + " seconds.\n")
            theAcyclicGraph.__init__()

        if localPath != 'None':
            print("Storing results...")

            theFirstStr = ""
            for i in range((x1 - x0) // deltaX):
                theFirstStr += "radialType1," + str(u[i]) + "," + str(v[i]) + "\n"

            print(theFirstStr, file = theCSVF)

            print("x_3 = " + str(u) + ";\ny_c = " + str(v) + ";\n\n", file = theMathLabF)

            print("Store successful.")




        print("\n\n################################\n"
              "### Building a 'radial' graph ##\n"
              "################################\n"
              "You'll see the algorithm run in O(n ** 3).\n"
              "MEMO: In this section, branches will be increased.\n")

        theBin = input("Please, press any key to continue.\n>>> ")

        v = []
        for i in range(x0, x1, deltaX):
            print("Running test #" + str(i // deltaX + 1))
            
            print("Initialization of " + str(u[(i // deltaX)]) + " nodes...")
            startT = time()
            theAcyclicGraph.setStar(i, costK)
            print("Initialization completed in " + str(time() - startT) + " seconds.\nGoing with 10 tests...")
            startT = time()
            theAcyclicGraph.getMiddles()
            v.append(time() - startT)
            print("Test completed in " + str(v[i // deltaX]) + " seconds.\n")
            theAcyclicGraph.__init__()

        if localPath != 'None':
            print("Storing results...")

            theFirstStr = ""
            for i in range((x1 - x0) // deltaX):
                theFirstStr += "radialTypes," + str(u[i]) + "," + str(v[i]) + "\n"

            print(theFirstStr, file = theCSVF)

            theFirstStr = "% x_4 = " + str(u) + ";\ny_d = " + str(v) + ";\n\n"

            theFirstStr += "% 'Few tests' means, discontinuous graphs..."

            theFirstStr += "figure\n"

            theFirstStr += "subplot(2, 2, 1)\n"
            theFirstStr += "plot(x_1, y_a)\n"
            theFirstStr += "xlabel('Levels of Nodes')\n"
            theFirstStr += "ylabel('Time (secs)')\n"
            theFirstStr += "title('Spheric Graph')\n\n"

            theFirstStr += "subplot(2, 2, 2)\n"
            theFirstStr += "plot(x_2, y_b)\n"
            theFirstStr += "xlabel('Nodes')\n"
            theFirstStr += "ylabel('Time (secs)')\n"
            theFirstStr += "title('Linear Graph')\n\n"

            theFirstStr += "% To see more interesting results,\n"
            theFirstStr += "% try with 2000 nodes!\n"
            theFirstStr += "subplot(2, 1, 2)\n"
            theFirstStr += "plot(x_2, y_b)\n"
            theFirstStr += "hold on\n"
            theFirstStr += "plot(x_3, y_c)\n"
            theFirstStr += "hold on\n"
            theFirstStr += "plot(x_3, y_d)\n"
            theFirstStr += "xlabel('Nodes')\n"
            theFirstStr += "ylabel('Time (secs)')\n"
            theFirstStr += "title('Radial Graphs')\n"


            print(theFirstStr, file = theMathLabF)

            print("Store successful.")



        print("#", strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()), file = theCSVF)
        print("%", strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()), file = theMathLabF)
        print("\n\nMEMO: The path is '" + localPath + "'.")
        
    print("\n################################")
    print("Process termined with 0 errors. Have a good time!")




if __name__ == "__main__":
    main()