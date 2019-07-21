from collections import deque
#import time


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
        #print(set(filter(lambda x:x!=0,[cnt[i]*l[i] for i in range(len(l))])))
        print(set([cnt[i]*l[i] if l[i]!=0 else None for i in range(len(l))])-{0})
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

    

class Hanoi():
    cnt = 0
    def __init__(self,n):
        self.num = n
        self.stack1 = deque(list(range(n,0,-1)))
        self.stack2 = deque([])
        self.stack3 = deque([])
    def move(self,give,take,remain,k):
        if k==1:
            ring = give.pop()
            take.append(ring)
            Hanoi.cnt +=1
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

def func8(dic,seq=[]):
    if dic=={}:
        print(" ".join(seq))
    #print(dic.keys())
    keys = list(dic.keys())
    for i in keys:
        dic[i]-=1
        if dic[i]==0:
            del dic[i]
            func8(dic,seq+[i])
            dic[i]=1
        else:
            func8(dic,seq+[i])
            dic[i]+=1
    if seq==[]:
        return
    
def LtoD(l):
    table = dict()
    for _ in range(len(l)):
        num = l.pop()
        if num in table:
            table[num]+= 1
        else:
            table[num] = 1
    #print(table)
    return table
        
def func9(n,l=["()"]):
    ll = []
    if n==1:
        print(",".join(l))
        #for i in l:
        #    print(i)
        return
    for i in l:#set으로 해서 add하는게 나을듯
        ll.append("("+i+")")
        if not (i+"()") in ll:
            ll.append(i+"()")
        if not ("()"+i) in ll:
            ll.append("()"+i)
    func9(n-1,ll)


def func10(l,i,j):
    same = sameplace(l,i,j)
    color = input("변경할 색")
    l = change(l,same,color)
    return l

def sameplace(l,i,j):#l은 주어진배열,i,j는 좌표
    ll = [(i,j)]
    visit = [[0]*len(l) for _ in range(len(l))]
    queue = deque([(i,j)])
    while len(queue)!=0:
        i,j = queue.popleft()
        visit[i][j] = 1
        if i>0 and visit[i-1][j]==0 and l[i-1][j]==l[i][j]:
            queue.append((i-1,j))
            ll.append((i-1,j))
        if i<len(l)-1 and visit[i+1][j]==0 and l[i+1][j]==l[i][j]:
            queue.append((i+1,j))
            ll.append((i+1,j))
        if j>0 and visit[i][j-1]==0 and l[i][j-1]==l[i][j]:
            queue.append((i,j-1))
            ll.append((i,j-1))
        if j<len(l)-1 and visit[i][j+1]==0 and l[i][j+1]==l[i][j]:
            queue.append((i,j+1))
            ll.append((i,j+1))
    return ll

def change(l,ll,color):#l은 주어진 배열, ll은 같은 값이 있는 좌표들
    for i,j in ll:
        l[i][j] = color
    return l

def func11(n):
    l = [0]*(n+1)
    l[0]=1
    for k in [1,5,10,25]:
        for i in range(1,len(l)):
            if i-k>=0:
                l[i]+=l[i-k]
    print(l[n])
    return

def func12(n=8,m=8,queen=[]):
    if n==0:
        print(" ".join(map(str,queen)))
        return
    row = list(range(m))
    trace = [sum(i) for i in queen]
    mtrace = [(i[0]-i[1]) for i in queen]
    for i in queen:
        row.remove(i[0])
    for r in row:
        if ((r+n-1) not in trace) and ((r-n+1) not in mtrace):
            func12(n-1,m,queen+[(r,n-1)])

def func13():#일단 포기...
    n = int(input("넣을 박스 갯수"))
    l = []
    l.append(tuple(map(int,input("너비,높이,깊이").split())))
    max_tower = [l[0]]
    length = sum(list(zip(*max_tower))[2])
    for _ in range(1,n):
        now = tuple(map(int,input("너비,높이,깊이").split()))
        high,low = find_tower(l,now)
        high_t,low_t = asem_tow(high),asem_tow(low)
        now_len = high_t+[now]+low_t
        #print(high_t)
        #print(now_len)
        if length<sum(list(zip(*now_len))[2]):
            max_tower = now_len
            length = sum(list(zip(*now_len))[2])
        l.append(now)
    return length

def find_tower(l,now):
    high = []
    low = []
    for i in l:
        if i[0]<now[0] and i[1]<now[1] and i[2]<now[2]:
            high.append(i)
        elif i[0]>now[0] and i[1]>now[1] and i[2]>now[2]:
            low.append(i)
    return high, low
            
def asem_tow(box):
    if len(box)==1:
        return box
    if len(box)==0:
        return []
    max_towers = []
    len_towers= []
    for std in range(len(box)):
        high,_ = find_tower(box[:std]+box[std:],box[std])
        max_tower = asem_tow(high)+[box[std]]
        max_towers.append(max_tower)
        len_towers.append(sum(list(zip(*max_tower))[2]))
    max_index = 0
    for i in range(len(box)):
        if len_towers[i]>len_towers[max_index]:
            max_index = i
    return max_towers[i]
    
    

#func1
try:
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
x = Hanoi(n)
print("Before")
x.print()
before = time.time()
x.move(x.stack1,x.stack3,x.stack2,n)
after  = time.time()
print("after")
x.print()
print(after-before)#22개부터1초넘어가고 대략 1개당 2배늘어남
print(f"이동횟수{Hanoi.cnt}")

#func7
string = input()
l = list(string)
func7(l)

#func8
string = input()
l = list(string)
func8(LtoD(l))


#func9

n = int(input())
func9(n)


#func10
# print("받을 그림은 8*8인걸로 하겠습니다")
l = []
n = int(input("받을 크기"))
for _ in range(n):
    l.append(list(map(int,input().split())))
# l = [[1, 1, 1, 0, 0, 0, 1, 2],
#  [0, 1, 0, 0, 1, 0, 2, 2],
#  [0, 0, 0, 0, 1, 0, 2, 2],
#  [0, 3, 0, 0, 1, 0, 0, 2],
#  [3, 3, 3, 0, 0, 0, 0, 0],
#  [3, 3, 3, 1, 1, 1, 1, 1],
#  [0, 0, 0, 0, 0, 0, 0, 0],
#  [4, 4, 4, 4, 4, 4, 4, 4]]
# print(l)
i,j = map(int,input("포인트 찍을 지점").split())
print(func10(l,i,j))

#func11
n = int(input())
func11(n)


#func12
n = int(input())
func12(n,n)


#func13
print(func13())
