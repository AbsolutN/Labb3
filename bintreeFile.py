class Node:
       def __init__(self, value):
          self.value = value
          self.down = None
          self.right = None
        
        

class Bintree:
    def __init__(self):
        self.root = None

    def put(self,newvalue):
        # Sorterar in newvalue i trädet
        self.root = putta(self.root,newvalue)

    def __contains__(self,searchedvalue):
        # True om value finns i trädet, False annars
        return finns(self.root,searchedvalue)

    def write(self):
        # Skriver ut trädet i inorder
        skriv(self.root)
        print("\n")

        
        
        
def putta(p,newvalue):
    if p == None: 
       return Node(newvalue)

    elif newvalue < p.value:
         if p.left == None:
            p.left = Node(newvalue)
         else:
            putta(p.left, newvalue)
              
    elif newvalue > p.value:
       if p.right == None:
          p.right = Node(newvalue)
       else:
            putta(p.right,newvalue)
    return p
    
    
def finns(p,value):
        if p == None: 
            return False
        if value == p.value: 
            return True
        if value < p.value: 
            return finns(p.left,value)
        if value > p.value: 
            return finns(p.right,value)
                
                
def skriv():
