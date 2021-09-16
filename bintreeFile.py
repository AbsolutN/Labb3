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

    def __contains__(self,value):
        # True om value finns i trädet, False annars
        return finns(self.root,value)

    def write(self):
        # Skriver ut trädet i inorder
        skriv(self.root)
        print("\n")

        
        
        
def putta(root,newvalue):
    p = Bintree.put()
    
    
def finns(p,value):
        letar = True
        while letar:
            if p == None: 
                return False
            if value == p.value: 
                return True
            if value < p.value: 
                p = p.left
            if value > p.value: 
                p = p.right
                
                
def skriv():
