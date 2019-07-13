from collections import deque
import time


def fun1(n):
    l = [0]*(n+1)
    l[0],l[1],l[2] = 1,1,2
    for i in range(3,n+1):
        l[i] = l[i-1]+l[i-2]+l[i-3]
    print(l[n])



def fun2(l,r=0,c=0,root=[(1,1)]):
    if r==len(l)-1 and c==len(l[0])-1:
        print("->".join(map(str,root)))
        return
    
    if r<len(l)-1:
        if l[r+1][c]==1:
            path = [(r+2,c+1)]
            
            fun2(l,r+1,c,root+path)
    if c<len(l[0])-1:
        if l[r][c+1]==1:
            path = [(r+1,c+2)]
            fun2(l,r,c+1,root+path)

    
    if r==0 and c==0:
        return
        

def func3(l):
    ll = [l[i]-i for i in range(len(l))]
    top,bot = len(ll)-1,0
    index  = (top+bot)//2
    while ll[index]!=0:
        if ll[top]==0:
            index = top
            continue
        if ll[bot]==0:
            index = bot
            continue
        if ll[index]<0:
            bot = index
            index = (top+index)//2
        else:
            top = index
            index = (bot+index)//2
    print(f"{index}번째 index는 {l[index]}")
            
   
def func4(l):
    for i in range(2**len(l)):
        tem = [0]*(len(l)-len(bin(i)[2:]))+list(bin(i)[2:])
        cnt = list(map(int,tem))
        #print([cnt[i]*l[i] for i in range(len(l))])
        print(set(filter(lambda x:x!=0,[cnt[i]*l[i] for i in range(len(l))])))
        #print(set(filter(lambda x:x!=0,cnt)))
        #목표:and 연산 이용해서 

def func5(a,b):
    if a<b:
        b,a= a,b
    result = 0
    bn = list(map(int,bin(b)[2:]))
    #print(f"b={b},a={a},bn={bn}")
    for i in range(len(bn)-1,-1,-1):
        result += (a<<(len(bn)-1-i))*bn[i]
        #print(result)
    print(result)

    

class hanoi():
    def __init__(self,n):
        self.num = n
        self.stack1 = deque(list(range(n,0,-1)))
        self.stack2 = deque([])
        self.stack3 = deque([])
    def move(self,give,take,remain,k):
        if k==1:
            ring = give.pop()
            take.append(ring)
        else:
            self.move(give,remain,take,k-1)
            self.move(give,take,remain,1)
            self.move(remain,take,give,k-1)
    def print(self):
        print(f"stack1={self.stack1}")
        print(f"stack2={self.stack2}")
        print(f"stack3={self.stack3}")
            
def func7(l,res=[]):
    if len(l)==1:
        print(" ".join(res+[l[0]]))
    else:
        for i in range(len(l)):
            func7(l[:i]+l[(i+1):],res+[l[i]])

        
#func1

n = int(input())
fun1(n)
        


#fun2

l = []
r,c = map(int,input().split())
for j in range(r):
    l.append(list(map(int,input().split())))
fun2(l)


#func3
l = list(map(int,input().split()))
func3(sorted(l))

#func4
l = list(map(int,input().split()))
func4(l)

#func5
a,b = map(int,input().split())
func5(a,b)

#func6

n = int(input())
x = hanoi(n)
print("Before")
x.print()
before = time.time()
x.move(x.stack1,x.stack3,x.stack2,n)
after  = time.time()
print("after")
x.print()
print(after-before)#22개부터1초넘어가고 대략 1개당 2배늘어남

#func7

string = input()
l = list(string)
func7(l)

