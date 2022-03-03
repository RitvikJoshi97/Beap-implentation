
class Node:
    def __init__(self, key, left=None, right=None, leftparent=None, rightparent=None):
        self.key = key
        self.left = left
        self.right = right
        self.leftparent = leftparent
        self.rightparent = rightparent
        

class BinaryBeap:
    def __init__(self,key,balance = None):
        self.root = Node(key)
        #make a new list of lists
        self.structure = [self.root]


    # As the order is fixed, we can make a function to define how to make the order as well
    # But this is almost as good, as the time complexity in both cases will be constant
    order = {}
    order["0"] = (None, None)
    order["1"] = (None, 0)
    order["2"] = (0, None)
    order["3"] = (None, 1)
    order["4"] = (1, 2)
    order["5"] = (2, None)
    order["6"] = (None, 3)
    order["7"] = (3, 4)
    order["8"] = (4, 5)
    order["9"] = (5, None)
    order["10"] = (None, 6)
    order["11"] = (6, 7)
        
    # O(1) - constant
    def min(self):  
        return self.structure[0].key

    # O(root(n)) 
    def max(self): 
        ## Start from the last element
        node = self.structure[-1]
        max_key = node.key
        while node.leftparent != None:
            if node.leftparent.left.key > max_key:
                max_key = node.leftparent.left.key
            node = node.leftparent.left
        return max_key


    # O(root(n)) 
    def insert(self, key): 
        def exchange(node1, node2):
            temp = node1.key
            node1.key = node2.key
            node2.key = temp

        ## Simply add the key
        self.structure.append(Node(key)) 
        node_pos = len(self.structure)-1

        ## When the node is created; it will call it's parents and change their children as well
        left_parent = self.order[str(node_pos)][0]
        
        right_parent = self.order[str(node_pos)][1]
        
        if left_parent != None:
            self.structure[node_pos].leftparent = self.structure[left_parent] 
            self.structure[left_parent].right = self.structure[node_pos]
        if right_parent != None:
            self.structure[node_pos].rightparent = self.structure[right_parent]
            self.structure[right_parent].left = self.structure[node_pos]



        runBubble = []
        
        def bubbleUp(node_pos):
            changes_made = True
            changes_made_left = True
            changes_made_right = True
            while changes_made == True:
                left_parent = self.order[str(node_pos)][0]
                right_parent = self.order[str(node_pos)][1]
                
                
                # if (check left)
                if left_parent != None:
                    if self.structure[left_parent].key > self.structure[node_pos].key:
                        exchange(self.structure[node_pos],self.structure[left_parent])
                        
                        ## add exchanged_node_pos to runBubble list 
                        runBubble.append(node_pos)

                        ## change node_pos if exchange made
                        node_pos = left_parent#self.structure[left_parent][0]
                        continue
                    else:
                        ## half part of end loop
                        changes_made_left = False
                else:
                    changes_made_left = False
            
                if right_parent != None:
                    if self.structure[right_parent].key > self.structure[node_pos].key:
                        # print("key: ", self.structure[node_pos].key, " right_parent ", self.structure[right_parent].key)
                        # print("exchange")
                        exchange(self.structure[node_pos],self.structure[right_parent])

                        ## add exchanged_node_pos to runBubble list 
                        runBubble.append(node_pos)

                        ## change node_pos if exchange made
                        node_pos = right_parent#self.structure[right_parent][1]
                        continue

                    else:
                        ## half other part to end loop
                        changes_made_right = False
                else:
                    changes_made_right = False
                
                if changes_made_left == False and changes_made_right == False:
                    changes_made = False
            return
            
        bubbleUp(node_pos)

        while len(runBubble) != 0:
            bubbleUp(runBubble[0])
            runBubble.pop(0)


    # O(root(n)) 
    def extract(self):
        def exchange(node1, node2):
            temp = node1.key
            node1.key = node2.key
            node2.key = temp
            
        elem = self.structure[0].key
        self.structure[0].key = self.structure[-1].key
        self.structure.remove(self.structure[-1])
        

        def exchange(node1, node2):
            temp = node1.key
            node1.key = node2.key
            node2.key = temp

        def bubbleDown(node):
            changes_made = True
            while changes_made == True:
                if node.left != None and node.right!= None:
                    if node.left.key < node.right.key:
                        child = node.left
                    else:
                        child = node.right
                elif node.left != None and node.right== None:
                    child = node.left
                elif node.left == None and node.right != None:
                    child = node.right
                else:
                    child = None
                
                if child != None:
                    if child.key < node.key:
                        exchange(node,child)
                        node = child
                    else:
                        changes_made = False
                else:
                        changes_made = False
        bubbleDown(self.structure[0])

        return elem

    def search(self,key):
        # Start from the node which is last
        # Then see the one above 
        # if it's more than that, then it'll be in the layers
        # else it'll be in the layers above
        # if at all
        node = self.structure[-1]
        while node != self.root:
            if node.leftparent != None:
                if key > node.leftparent.key:
                    # traverse same layer
                    while node.leftparent != None:
                        if key == node.key:
                            if node.leftparent != None and node.rightparent != None:
                                return(str(key)+" found with left parents: "+str(node.leftparent.key)+" and "+str(node.rightparent.key))
                            elif node.leftparent != None and node.rightparent == None:
                                return(str(key)+" found with left parent: "+str(node.leftparent.key))
                            elif node.leftparent == None and node.rightparent != None:
                                return(str(key)+" found with left parent: "+str(node.rightparent.key))
                        else:
                            #update the node to the left node in the same layer
                            node = node.leftparent.left
                else:
                    #change node to one level up
                    node = node.leftparent
            

        if key == self.root.key:
            return "found at root"
        else:
            return "not found"
        




    
beap = BinaryBeap(20)
beap.insert(9)
beap.insert(12)
beap.insert(6)
beap.insert(13)
beap.insert(1)
beap.insert(8)
beap.insert(7)
beap.insert(15)
beap.insert(11)

print("#####")

k = 0
for i in range(1,6):
    for j in range(1,i):
        if k < len(beap.structure):
            print(beap.structure[k].key, end=" ")
            k += 1
    print()


print("#####")

print("min: ", beap.min())

print("#####")

print("max: ", beap.max())



print("#####")
print("extract: ", beap.extract())

print("#####")

print("min: ", beap.min())

# print("#####")
# print("extract")
# print(beap.extract())
# print("#####")
# print("extract")
# print(beap.extract())
# print("#####")
# print("extract")
# print(beap.extract())
# print("#####")
# print("extract")
# print(beap.extract())
# print("#####")
# print("extract")
# print(beap.extract())
print("#####")
print("print:")

k = 0
for i in range(1,6):
    for j in range(1,i):
        if k < len(beap.structure):
            print(beap.structure[k].key, end=" ")
            k += 1
    print()

print("#####")

beap.insert(1)

print("#####")

print("search 11: ", beap.search(11))
print("search 15: ", beap.search(15))
print("search 13: ", beap.search(13))

print("#####")
print("Max: ",beap.max())


print("#####")

k = 0
for i in range(1,6):
    for j in range(1,i):
        if k < len(beap.structure):
            print(beap.structure[k].key, end=" ")
            k += 1
    print()


