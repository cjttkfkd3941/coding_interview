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
            n = n.next
            return 
        while n.next != None:
            if n.next.data==data:
                n.next = n.next.next
                return 
            n = n.next

    def get(self):
        n = self
        l = []
        while n.next!=None:
            n = n.next
            l.append(n.data)
        print("->".join(map(str,l)))
        return

    def toset1(self):#2.1-1
        buffer = []
        n = self
        while n.next != None:
            if not(n.next.data in buffer):
                buffer.append(n.next.data)
                n = n.next
            else :
                n.next = n.next.next
        return

    def toset(self):#2.1-2
        n = self.next
        while n.next != None:
            b = self
            switch = False
            while b.next != None:
                if b.next.data == n.data and switch ==True:
                    b.next = b.next.next
                elif b.next.data == n.data and switch ==False:
                    switch = True
                    b = b.next
                else:
                    b = b.next
            n = n.next
        return

    def size(self):#2.2-1_1
        n = self
        l = []
        while n.next!=None:
            n = n.next
            l.append(n.data)
        return len(l)

    def find(self,k):#2.2-1_2
        l = self.size()
        ind = 0
        n = self
        while ind != l-k:
            n = n.next
            ind+=1
        return n.next.data

    def find2(self,k):#2.2-2
        buffer = []
        n = self
        while n.next!=None:
            if len(buffer)==k:
                _ = buffer.pop(0)
            buffer.append(n.next.data)
            n = n.next
        return buffer.pop(0)

    def separ(self,num):#2.4
        n = self
        b = Node()1
        while n.next!=None:
            if n.next.data>=num:
                b.append(n.next.data)
                n.next = n.next.next
            else:
                n = n.next
        n.next = b.next
        return 
