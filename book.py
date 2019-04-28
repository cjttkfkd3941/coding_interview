class Node:
    def __init__(self,data=None):
        self.next = None
        self.data = data
    def append(self,data):
        end = Node(data)
        n = self
        while n.next != None:
            n = n.next
        n.next = end
    def pop(self,data):
        n = self
        if n.data ==data:
            return 
        while n.next != None:
            if n.next.data==data:
                n.next = n.next.next
                return 
            n = n.next

    def get(self):
        n = self
        while n.next!=None:
            n = n.next
        return n.data
        

    def toset(self):
        n = self
        while n.next != None:
            b = n
            while b.next ==None:
                if b.next.data == n.data:
                    n.pop(b.next.data)
                    b.pop(b.next.data)
                b = b.next
            n = n.next
        
             