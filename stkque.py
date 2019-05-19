class StackNode:
    def __init__(self,data=None):
        self.next = None
        self.data = data
        self.top = None
        self.min = data
        self.size = 0

    def push(self,data):
        addData = StackNode(data)
        if self.min==None:
            self.min = data
        if self.min<addData.min:
            addData.min = self.min
        else:
            self.min = addData.min
        addData.next =self.top
        self.top = addData
        addData.top = addData
        self.size += 1
        
        
    def pop(self):
        top =  self.top.data
        if top==None:
            pass
        else:
            self.top = self.top.next
        self.size -= 1
        return top
    
    def peek(self):
        top = self.top.data
        return top
    
    def isEmpty(self):
        if self.top==None:
            return True
        else:
            return False
            
    def get(self):
        l = []
        n = self.top
        l.append(n)
        while n.next:
            l.append(n.next)
            n = n.next
        l = list(reversed(l))
        for i in range(len(l)-1,-1,-1):
            print(str(l[i].data),end="->")
        print("끝")



class QueNode():
    def __init__(self,data = None):
        self.next = None
        self.data = data
        self.head = None
        self.tail = None
        
    def add(self,data):
        n = self
        new = QueNode(data)
        if n.next==None:
            self.head = new
            self.tail = new
            self.next = new
        else:
            self.tail.next = new
            self.tail = new

    def remove(self):
        n = self
        out = n.head
        n.head = n.head.next
        if n.head==None:
            n.tail = None
            n.next = None
        return out.data

    def peek(self):
        n = self
        out = n.head
        return out.data

    def isEmpty(self):
        if not(self.head) and not(self.tail):
            return True
        else:
            return False


    def get(self):
        l = []
        n = self.head
        l.append(n)
        while n.next:
            l.append(n.next)
            n = n.next
        for i in range(len(l)):
            print(str(l[i].data),end="->")
        print("끝")

#3.2
def StackMin(s):
    return s.top.min



#3.3
class SetOfStacks():
    def __init__(self,data=None):
        n = StackNode(None)
        self.next = n
        self.topN = n
        self.top = None
    def push(self,data):
        if self.next.size%5==0:
            addData = StackNode()
            addData.push(data)
            addData.top.next=self.topN.top
            self.topN = addData
            self.top = addData.top
        else:
            self.topN.push(data)
            self.top = self.topN.top
    def pop(self):
        Res = self.topN.top.data
        self.topN.top = self.topN.top.next
        self.top = self.topN.top
        return Res

    def peek(self):
        return self.top.data

    def isEmpty(self):
        if self.top==None:
            return True
        else:
            return False
