class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 


       // this is a node of the tree , which contains info as data, left , right
'''
def calculateHeightForSubTree(root, previousHeight):
    if root:
        leftHeight = calculateHeightForSubTree(root.left, previousHeight + 1)
        rightHeight = calculateHeightForSubTree(root.right, previousHeight + 1)
        result = max(leftHeight, rightHeight)

    else:
        result = previousHeight

    return result

def height(root):
    return calculateHeightForSubTree(root, -1)

def getHeightFor(aNumberOfNodesString, aNodeValuesString):
    tree = BinarySearchTree()
    t = int(aNumberOfNodesString)

    arr = list(map(int, aNodeValuesString.split()))

    for i in range(t):
        tree.create(arr[i])

    return height(tree.root)