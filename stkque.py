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
        elif self.top.next==self:
            self.top = None
            self.size -= 1
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
        return out

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

# 3.4
class MyQueue():
    def __init__(self):
        self.stack1 = StackNode()
        self.stack2 = StackNode()
        self.switch = 1
        #switch==1이면 stack1에 다 들어가있는거, 0이면 2에 들어가는거로 정의
    def push(self,data):
        if self.switch == 1:
            pass
        else:
            self.moving(self.stack2,self.stack1)
            self.switch = 1
        self.stack1.push(data)
    
    def pop(self):
        if self.switch == 1:
            self.moving(self.stack1,self.stack2)
            self.switch = 0
        else:
            pass
        return self.stack2.pop()

    def moving(self,stack1,stack2):
        while stack1.top:
            stack2.push(stack1.pop())

        
    def isEmpty(self):
        if self.stack1.isEmpty() and self.stack2.isEmpty():
            return True
        else:
            return False
            
def StackSort(stack1):##size,min 부분은 고려안하고 next,pop,push,top개념만 고려
    s = stack1
    s2 = StackNode()
    while s.top:
        top = s.top #top은 가장 위의 노드
        s.top = s.top.next
        top2 = s2.top#top2 는 소팅된 가장 위 노드
        if top2==None:
            top.next = s2
            s2.top = top
        else:
            if top.data<top2.data:
                top.next = s2.top
                s2.top = top
            else:
                while top2.next.data:  
                    if top.data<top2.next.data:
                        break
                    else:
                        top2 = top2.next
                top.next = top2.next
                top2.next = top
    return s2

class shelter():
    count = 0
    def __init__(self):
        self.QueCat = QueNode()
        self.QueDog = QueNode()
    def push(self,species):
        if species=='cat'or species=="Cat":
            self.QueCat.add(self.count+1)
        if species=="dog" or species=="Dog":
            self.QueDog.add(self.count+1)
        shelter.increment()
    def popCat(self):
        cat = self.QueCat.remove()
        print("Cat",end=" ")
        return cat
    def popDog(self):
        dog = self.QueDog.remove()
        print("Dog",end=" ")
        return dog
    def popAny(self):
        c = self.QueCat.peek()
        d = self.QueDog.peek()
        if c==None:
            c = QueNode(self.count+1)
        if d==None:
            d = QueNode(self.count+1)
        if c.data<d.data:
            print("Cat",end=" ")
            return self.QueCat.remove()
        elif c==d:
            return "Don't have Animal"
        else:
            print("Dog",end=" ")
            return self.QueDog.remove()

    @classmethod
    def increment(cls):
        cls.count += 1
    

#####################################################################################
#from stkque import *

#3.2
'''
a= StackNode()
a.push(1)
print(StackMin(a))
a.push(2)
print(StackMin(a))
a.push(5)
print(StackMin(a))
a.push(10)
print(StackMin(a))
a.push(-3)
print(StackMin(a))
a.get()
print(a.peek())
a.pop()
print(a.peek())
print(StackMin(a))
a.pop()
print(a.peek())
a.pop()
print(a.isEmpty())

'''


'''
a= QueNode()
a.add(1)
a.add(2)
a.add(5)
a.get()
print(a.peek())
a.remove()
print(a.peek())
a.remove()
print(a.peek())
a.remove
print(a.isEmpty())
'''


#3.3
'''
a = SetOfStacks()
a.push(3)
a.push(5)
a.push(10)
a.push(15)
a.push(20)
a.push(17)
a.push(13)
print(a.peek())
print(a.pop())
print(a.peek())
print(a.pop())
print(a.peek())
print(a.pop())
print(a.peek())
print(a.pop())
print(a.peek())
print(a.pop())
print(a.peek())
print(a.pop())
print(a.peek())
print(a.pop())
print(a.isEmpty())
'''

#3.4
'''
a = MyQueue()
a.push(3)
a.push(5)
a.push(10)
a.push(8)
a.push(20)
a.push(17)
a.push(13)
print(a.pop())
a.push(100)
print(a.pop())
print(a.pop())
print(a.pop())
print(a.pop())
a.push(200)
print(a.pop())
print(a.pop())
print(a.pop())
print(a.pop())
print(a.isEmpty())
'''

#3.5
'''
a = StackNode()
a.push(3)
a.push(5)
a.push(10)
a.push(8)
a.push(20)
a.push(17)
a.push(13)
b = StackSort(a)
print(b.pop())
print(b.pop())
print(b.pop())
print(b.pop())
print(b.pop())
print(b.pop())
print(b.pop())
print(b.isEmpty())
'''
#3.6
'''
a = shelter()
a.push("cat")#1
a.push("cat")#2
a.push("dog")#3
a.push("cat")#4
a.push("cat")#5
a.push("cat")#6
a.push("dog")#7
a.push("dog")#8
print(a.popCat())
print(a.popCat())
print(a.popCat())
print(a.popAny())
print(a.popDog())
print(a.popAny())
print(a.popDog())
print(a.popAny())
'''
