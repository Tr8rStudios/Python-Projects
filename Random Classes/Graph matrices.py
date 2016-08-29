class AdjacencyMatrix:

    adjMatrix = []

    def __init__(self, initSize, simple = False):
        
        self.adjMatrix = []
        for i in range(initSize):
            self.adjMatrix.append([0])
            for j in range(initSize - 1):
                self.adjMatrix[i].append(0)
                    
        self.size = initSize
        self.simple = simple
    def __repr__(self):
        string = ''
        if self.size > 0:    
            for i in range(self.size - 1):
                string += str(self.adjMatrix[i]) + '\n'

            string += str(self.adjMatrix[self.size - 1])

        else:
            string = '[]'
            
        return string

    def __str__(self):
        string = ''
        if self.size > 0:    
            for i in range(self.size - 1):
                string += str(self.adjMatrix[i]) + '\n'

            string += str(self.adjMatrix[self.size - 1])

        else:
            string = '[]'
            
        return string

    def __len__(self):
        return self.size

    def addVertex(self, index = None):
        if index == None:
            index = self.size
        else:
            assert ( self.size > row
                 and self.size > col
                 and row >= -self.size
                 and col >= -self.size ), "Index out of range"
            
        for i in range(self.size):
            self.adjMatrix[i].insert(index, 0)

        self.adjMatrix.insert(index, [0])

        for i in range(self.size):
            self.adjMatrix[index].insert(index, 0)
        
        self.size += 1

    def checkLink(self, row, col):
        assert ( self.size > row
                 and self.size > col
                 and row >= -self.size
                 and col >= -self.size ), "Index out of range"

        return self.adjMatrix[row][col]

    def link(self, row, col):
        assert ( self.size > row
                 and self.size > col
                 and row >= -self.size
                 and col >= -self.size ), "Index out of range"

        if self.simple:
            assert ( self.adjMatrix[row][col] != 1
                     and self.adjMatrix[col][row] != 1 ), "Link already exists"
            assert row != col, "Vertices cannot link to itself in a simple graph"
            
        if row != col:
            self.adjMatrix[row][col] += 1
            self.adjMatrix[col][row] += 1
            
        else:
            self.adjMatrix[row][col] += 1

    def dirLink(self, row, col):
        assert ( self.size > row
                 and self.size > col
                 and row >= -self.size
                 and col >= -self.size ), "Index out of range"

        if self.simple:
            assert self.adjMatrix[row][col] != 1, "Link already exists"

            assert row != col, "Vertices cannot link to itself in a simple graph"

        self.adjMatrix[row][col] += 1

    def removeLink(self, row, col):
        assert ( self.size > row
                 and self.size > col
                 and row >= -self.size
                 and col >= -self.size ), "Index out of range"

        assert ( self.adjMatrix[row][col] > 0
                 or self.adjMatrix[col][row] > 0 ), "No link exists between the two vertices"

        if self.adjMatrix[row][col] > 0:
            self.adjMatrix[row][col] -= 1
        
        if self.adjMatrix[col][row] > 0:
            self.adjMatrix[col][row] -= 1

    def removeDirLink(self, row, col):
        assert ( self.size > row
                 and self.size > col
                 and row >= -self.size
                 and col >= -self.size ), "Index out of range"

        assert self.adjMatrix[row][col] > 0, "No directed link exists"
        
        self.adjMatrix[row][col] -= 1

    def __getitem__(self, key):
        return self.adjMatrix[key]



