class Node:
    #하면서 드는 생각
    #클래스 한개와 두개의 장단이 있다고 생각한다.
    #내가 만든 코드에선 첫 노드는 빈노드 이여야한다.
    #head 필요로 인해 추가
    def __init__(self,data=None,head=None):
        self.next = None
        self.data = data
        if head==None:
            self.head = self
        else:
            self.head = head

    def link(self,node):
        n = self
        while n.next:
            n = n.next
        node.head = n.head
        if node.data==None:
            n.next = node.next
        else:
            n.next = node

    def append(self,data):
        end = Node(data,self.head)
        n = self
        while n.next:
            n = n.next
        n.next = end
    def pop(self,data):
        n = self
        if n.data ==data:
            n = n.next
            return 
        while n.next:
            if n.next.data==data:
                n.next = n.next.next
                return 
            n = n.next

    def get(self):
        n = self
        l = []
        ll = []
        switch = True
        while n.next:
            if n.next in l:
                l.append(n.next)
                switch = False
                break
            l.append(n.next)
            n = n.next
        for i in l:
            ll.append(i.data)
        print("->".join(map(str,ll)),end="")
        if switch:
            print()
        else:
            print("앞에나온 값 반복")
        return

    def toset1(self):
        buffer = []
        n = self
        while n.next:
            if not(n.next.data in buffer):
                buffer.append(n.next.data)
                n = n.next
            else :
                n.next = n.next.next
        return

    def toset(self):
        n = self.next
        while n.next:
            b = self
            switch = False
            while b.next:
                if b.next.data == n.data and switch ==True:
                    b.next = b.next.next
                elif b.next.data == n.data and switch ==False:
                    switch = True
                    b = b.next
                else:
                    b = b.next
            n = n.next
        return

    def size(self):
        n = self
        l = []
        while n.next:
            n = n.next
            l.append(n.data)
        return len(l)

    def find(self,k):
        l = self.size()
        ind = 0
        n = self
        while ind != l-k:
            n = n.next
            ind+=1
        return n.next.data

    def find2(self,k):
        buffer = []
        n = self
        while n.next:
            if len(buffer)==k:
                _ = buffer.pop(0)
            buffer.append(n.next.data)
            n = n.next
        return buffer.pop(0)
    

    

    def separ(self,num):
        n = self
        b = Node()
        while n.next:
            if n.next.data>=num:
                b.append(n.next.data)
                n.next = n.next.next
            else:
                n = n.next
        n.next = b.next
        return 
    

    
    def isPalin(self):
        w = self.size()
        n = self
        l=[]
        c = w//2
        r = w%2
        while n.next:
            if c!=0:
                c-=1
                l.append(n.next.data)
                n = n.next
            else:
                if r!=1:
                    if n.next.data==l.pop():
                        n = n.next
                    else:
                        return False
                else:
                    r = 0
                    n = n.next
        return True

    def findLoop(self):
        buffer = []
        n = self
        while n.next:
            if n.next in buffer:
                return n.next.data
            else:
                buffer.append(n.next)
                n = n.next
        return "Not Exist"
  
            
def sum_Linkedlist(a,b):
    if type(a)!=type(Node()) or type(b)!=type(Node()):
        raise ValueError
    n = Node()
    liftNum=0
    while a.next and b.next:
        num = a.next.data+b.next.data+liftNum
        n.append(num%10)
        liftNum = num//10
        if a.next:
            a = a.next
        if b.next:
            b = b.next
    return n

def intersection0(a,b):
    buffer = []
    while a.next:
        while b.next:
            if a.next==b.next and not(b.next in buffer):
                buffer.append(b)
            b = b.next
        b = b.head
        a = a.next
    print(buffer)
    return



#1번,2번,4번
'''
a = Node()
a.append(1)
a.append(2)
a.append(3)
a.append(5)
a.append(8)
a.append(5)
a.append(7)
a.append(10)
a.append(2)
a.append(1)
print(a.head.data)
a.get()
a.separ(5)
a.get()
'''
#2.7
'''
a = Node()
a.append(1)
a.append(2)
a.append(3)
a.append(5)
b = Node()
b.append(8)
b.append(5)
b.append(7)
b.append(10)
a.get()
a.link(b)
a.get()
c = Node()
c.append(1)
c.link(b)
print("b is",end=" ")
b.get()
c.append(17)
# 윗 부분을 추가하면 a 에도 c에도 추가되는데 이렇게 되도 되는가?,
# 만약 이러면 안되는것이라면 단일 클래스가아닌 노드와 링크드리스트라는 두개의 클래스로 표현하는게 맞지않나
print("a is",end=" ")
a.get()
print("b is",end=" ")
b.get()
print("c is",end=" ")
c.get()
intersection0(a,c)
'''


#5번
'''
a = Node()
a.append(7)
a.append(1)
a.append(6)
b = Node()
b.append(5)
b.append(9)
b.append(2)
n = sum_Linkedlist(a,b)
n.get()
'''
#6
'''
a = Node()
a.append(1)
a.append(2)
a.append(3)
a.append(5)
a.append(3)
a.append(2)
a.append(1)
a.get()
print(a.isPalin())
a.get()
'''

# a = Node()
# b = Node()
# print(a.__dir__())
# print(a.__hash__())
# print(b.__hash__())
# print(a==b)
# print(a.__hash__() == b.__hash__())


#2.8
a = Node()
a.append(3)
a.append(5)
b = Node()
b.append(2)
a.link(b)
c = Node()
c.append(7)
c.append(8)
c.append(10)
a.link(c)
a.link(b)
a.get()
print(a.findLoop())
