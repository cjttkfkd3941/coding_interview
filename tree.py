#여기서 트리를 짜봅시다
from functools import reduce
class Graph():
    def __init__(self):
        self.vertex = set()
        self.edge = dict()
        self.count = 0
    def put(self,node):
        self.edge[node.mynum] = node.link
        self.vertex.add(node)
    def linker(self,n1,n2):
        self.switch = 0
        for node in list(self.vertex):
            if node.mynum==n1:
                node1 = node
                self.switch+=1
            if node.mynum==n2:
                node2 = node
                self.switch+=1
            if self.switch==2:
                break
        node1.linking(n2)
        node2.linking(n1)        
        #self.edge[n1].append(n2) 이거 넣으면 중복해서 들어감 근데 내가 그래프클래스에선 따로 추가 안했는데 왜 자동으로 추가되는거지?
        #self.edge[n2].append(n1) 단지 노드들에 업데이트만 했을뿐인데?
    def visit(self,n):
        for node in list(self.vertex):
            if node.mynum==n:
                break
        node.visit = True
        self.count+=1
    def isvisit(self,n):
        for node in list(self.vertex):
            if node.mynum==n:
                break
        if node.visit==True:
            return True
        else:
            return False
    
    def reset(self):
        for node in list(self.vertex):
            node.visit=False
        self.count = 0
    
class gNode():
    def __init__(self,data):
        self.mynum = data
        self.link = set()
        self.visit = False
    def linking(self,*data):
        for d in data:
            self.link.add(d)

#4.1
def connect(g,a,b):#이상해
    if g.isvisit(a):
        pass
    else:        
        g.visit(a)
        con = g.edge[a]
        if b in list(con):
            print(f"{a}-->{b}",end="\t")
            print("Exist")
            exit()
            return 
        if reduce(lambda x,y:x & y,map(g.isvisit,g.edge[a])):
            print("Not connected")
            exit()
            return    
        for i in sorted(list(con)):
            print(f"{a}-->{i}",end="\t")
            connect(g,i,b)
#4.1
'''
g = Graph()
n1 = gNode(1)
n1.linking(2)
n2 = gNode(2)
n2.linking(1,5)
n3 = gNode(3)
n3.linking(5)
n4 = gNode(4)
n4.linking(3,5)
n5 = gNode(5)
n5.linking(2,4)

nodes = [n1,n2,n3,n4,n5]
for n in nodes:
    g.put(n)
print(g.edge)
print(f"노드번호:{n1.mynum},연결:{n1.link},방문:{n1.visit}")
print(f"노드번호:{n2.mynum},연결:{n2.link},방문:{n2.visit}")
print(f"노드번호:{n3.mynum},연결:{n3.link},방문:{n3.visit}")
print(f"노드번호:{n4.mynum},연결:{n4.link},방문:{n4.visit}")
print(f"노드번호:{n5.mynum},연결:{n5.link},방문:{n5.visit}")

#g.linker(5,4)
#g.linker(3,4)
g.visit(3)
g.visit(2)
g.visit(1)
g.visit(4)
g.visit(5)
print(g.edge)
print(f"노드번호:{n1.mynum},연결:{n1.link},방문:{n1.visit}")
print(f"노드번호:{n2.mynum},연결:{n2.link},방문:{n2.visit}")
print(f"노드번호:{n3.mynum},연결:{n3.link},방문:{n3.visit}")
print(f"노드번호:{n4.mynum},연결:{n4.link},방문:{n4.visit}")
print(f"노드번호:{n5.mynum},연결:{n5.link},방문:{n5.visit}")
print()
g.reset()
print(f"노드번호:{n1.mynum},연결:{n1.link},방문:{n1.visit}")
print(f"노드번호:{n2.mynum},연결:{n2.link},방문:{n2.visit}")
print(f"노드번호:{n3.mynum},연결:{n3.link},방문:{n3.visit}")
print(f"노드번호:{n4.mynum},연결:{n4.link},방문:{n4.visit}")
print(f"노드번호:{n5.mynum},연결:{n5.link},방문:{n5.visit}")
connect(g,1,3)
'''

#4.2        
class TreeNode():
    def __init__(self,data=None,leftnode=None,rightnode=None):
        self.data = data
        self.left = leftnode
        self.right = rightnode
    def printing(self):
        print(f"{self.data}")
        if self.left:
            print("left",end=" ")
            self.left.printing()
        if self.right:
            print("right",end=" ")
            self.right.printing()

def Treelize(slist):
    le = len(slist)
    if le>=4:    
        l = Treelize(slist[:le//2])
        r = Treelize(slist[le//2+1:])
        now = TreeNode(slist[le//2],l,r)
    elif le==3:
        l = TreeNode(data = slist[0])
        r = TreeNode(data=slist[2])
        now = TreeNode(slist[1],l,r)
    elif le==2:
        l = TreeNode(data = slist[0])
        now = TreeNode(slist[1],l,None)
    elif le==1:
        now = TreeNode(slist[0])
    return now
    
#4.2
'''
root = Treelize(sorted([3,4,5,6,7,8,9,10]))

root.printing()
print(f"root:{root.data},left:{root.left.data},right:{root.right.data}")
lroot = root.left
rroot = root.right
print(f"root:{lroot.data},left:{lroot.left.data},right:{lroot.right.data}")
print(f"root:{rroot.data},left:{rroot.left.data},right:{rroot.right.data}")
llroot = lroot.left
lrroot = lroot.right
print(f"root:{llroot.data},left:{llroot.left.data},right:{llroot.right.data}")
print(f"root:{lrroot.data},left:{lrroot.left.data},right:{lrroot.right}")
rlroot = rroot.left
rrroot = rroot.right
print(f"root:{rlroot.data},left:{rlroot.left.data},right:{rlroot.right}")
print(f"root:{rrroot.data},left:{rrroot.left.data},right:{rrroot.right}")
'''


def searching(node,data,string=""):
    string = string
    left = node.left
    right = node.right
    try:
        if node.data==data:
            string=string + str(data)
            return print(string)
        elif node.data>data:
            string=string+"left "
            return searching(left,data,string)
        else:
            string = string+ "right "
            return searching(right,data,string)
    except:
        print("Not exist")

class LNode():##2장 linkedlist
    def __init__(self,data=None,head = None):
        self.data = data
        self.next = None
        if head==None:
            self.head = self
        else:
            self.head = head

    def append(self,data):
        end = LNode(data,self.head)
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

#4.3

def TreeToLinkedlist(node=TreeNode(),dic=dict(),dept = 1):
    if dic.get(dept)==None:
        dic[dept]=LNode()
        dic[dept].append(node.data)
    elif dic.get(dept):
        dic[dept].append(node.data)
    if node.left:
        dic = TreeToLinkedlist(node.left,dic,dept+1)
    if node.right:
        dic = TreeToLinkedlist(node.right,dic,dept+1)
    return dic

'''
d = TreeToLinkedlist(root)
d[1].get()
d[2].get()
d[3].get()
d[4].get()
'''


def BalanCheck(node=TreeNode(),dept = 1):
    
    if node.left:
        leftdept = BalanCheck(node.left,dept+1)
    else:
        leftdept = dept
    if node.right:
        rightdept = BalanCheck(node.right,dept+1)
    else:
        rightdept = dept
    
    if dept==1:
        if abs(leftdept-rightdept)<=1:
            return True
        else:
            return False
    if node.left!=None:
        if abs(leftdept-rightdept)<=1:
            return max(leftdept,rightdept)
        else:
            return "여기에 뭘 리턴해야하지...?"
    else:
        return dept

'''
root = Treelize(sorted([3,4,5,6,7,8,9,10]))

root.printing()
print(f"root:{root.data},left:{root.left.data},right:{root.right.data}")
lroot = root.left
rroot = root.right
print(f"root:{lroot.data},left:{lroot.left.data},right:{lroot.right.data}")
print(f"root:{rroot.data},left:{rroot.left.data},right:{rroot.right.data}")
llroot = lroot.left
lrroot = lroot.right
print(f"root:{llroot.data},left:{llroot.left.data},right:{llroot.right}")
print(BalanCheck(root))
'''


#4.5
def StyleCheck(node,parent = None,dept = 1):
    check=True
    if node.left:
        if parent:
            if node.left.data<node.data and node.left.data>parent and node.data>parent:
                check = StyleCheck(node.left,node.data,dept+1)
            elif node.left.data<node.data and node.data<parent:
                check = StyleCheck(node.left,node.data,dept+1)
            else:
                check=False
        else: 
            if node.left.data<node.data:
                check = StyleCheck(node.left,node.data,dept+1)
            else:
                check=False

    if dept!=1 and check==True:
        pass
    else:
        if check==True:
            return "Binary Search Tree"
        else:
            return "Binary Tree"

    if node.right:
        if parent:
            if node.data<node.right.data and parent>node.right.data and node.data<parent:
                check = StyleCheck(node.right,node.data,dept+1)
            elif node.data<node.right.data and node.data>parent:
                check = StyleCheck(node.right,node.data,dept+1)
            else:
                check=False
        else:
            if node.data<node.right.data:
                check = StyleCheck(node.right,node.data,dept+1)
            else:
                check=False
    if dept!=1 and check==True:
        return check
    else:
        if check==True:
            return "Binary Search Tree"
        else:
            return "Binary Tree"
'''
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(13)
root.right.left = TreeNode(11)
root.right.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(8)
root.left.right.left = TreeNode(3)

print(StyleCheck(root))
'''



class TreeNode6():
    def __init__(self,data=None,leftnode=None,rightnode=None):
        self.data = data
        self.parent = None
        self.left = leftnode
        self.right = rightnode
        self.visit = False
    def printing(self):
        print(f"{self.data}")
        if self.left:
            print("left",end=" ")
            self.left.printing()
        if self.right:
            print("right",end=" ")
            self.right.printing()

def searching6(node,data):##그러니까 중위탐색시, 왼쪽->부모->오른쪽순인데, 탐색시 다음 탐색될 노드를 찾으라는 얘기
    if node.data>data:
        return searching6(node.left,data)
    elif node.data<data:
        return searching6(node.right,data)
    else:
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node.data
        else:
            while node.parent.data<data:
                node = node.parent
                if node.parent==None:
                    return "Last Node"
            return node.parent.data
#4.6
'''
root = TreeNode6(10)
root.left = TreeNode6(5)
root.left.parent=root
root.right = TreeNode6(13)
root.right.parent = root
root.right.left = TreeNode6(11)
root.right.left.parent = root.right
root.right.right = TreeNode6(15)
root.right.right.parent = root.right
root.left.left = TreeNode6(3)
root.left.left.parent = root.left
root.left.right = TreeNode6(8)
root.left.right.parent = root.left
for i in sorted([10,5,13,11,3,15,8]):
    print(searching6(root,i))
'''


#4.7
def priority(project,relation,run=[]):
    #project = input().split(",")
    #relation = map(tuple,input().split(","))
    runset = []
    if relation!=[]:
        desti = set(list(map(list,zip(*relation)))[1])
    else:
        desti = set()
    for i in project:
        if not(i in desti):
            runset.append(i)
    if runset==[]:
        return "Not Exist"
    runVal=runset[-1]
    run.append(runVal)
    project.remove(runVal)
    for j in relation:
        if j[0]==runVal:
            relation.remove(j)
    if project!=[]:
        return priority(project,relation,run)
    else:
        return " ".join(run)
#4.7
#print(priority(['a','b','c','d','e','f'],[('a','d'),('f','b'),('b','d'),('f','a'),('d','c')]))
    

#후위탐색으로 하면 조상노드에 도달했을때, 그 이전 모든 노드를 들리게 되고 그 check 2개가 모두 true로 변함
##이거 일단 포기 도저히모르겟음...
'''
def ComPare(tree,node1,node2,check=(False,False)):
    dd = tree.data
    dd1 = node1.data
    dd2 = node2.data
    if tree.left and check!=(True,True):
        check = ComPare(tree.left,node1,node2,check)
    if tree.right and check!=(True,True):
        check = ComPare(tree.right,node1,node2,check)
    if check==(True,True):
        return tree.data
    if tree==node1:
        return (True,check[1])
    elif tree==node2:
        return (check[0],True)
    else:
        return check
'''
    
#밑에거로 하면 tree.data가 2인경우 에러    
'''
def ComPare(tree,node1,node2,root,check=0):
    ddd = tree.data
    if tree.left:
        check = ComPare(tree.left,node1,node2,root,check)
    if tree.right:
        check = ComPare(tree.right,node1,node2,root,check)
    if check==2:
        return tree.data 
    if tree==node1:
        sol1 = node1.data
        check += 1
        return check
    if tree==node2:
        sol2 = node2.data
        check += 1
        return check
    if check==2:
        return 
    elif check<2 and tree==root:
        return "Not Exist"
    else:
        return check
'''
#4.8 3번째도전
def ComPare(tree,node1,node2,n1 = False,n2 = False):
    dd,dd1,dd2 = tree.data,node1.data,node2.data
    if tree.left:
        n1 = ComPare(tree.left,node1,node2,n1,False)
    if tree.right:
        n2 = ComPare(tree.right,node1,node2,False,n2)
    if n1&n2 and type(n1)==bool and type(n2)==bool:
        return tree.data
    if (n1|n2)==True and (tree==node1 or tree==node2):
        return tree.data
    if tree==node1:
        return True
    elif tree==node2:
        return True
    if type(n1)==bool and type(n2)==bool:
        return (n1 or n2)
    else:
        return int(n2)+int(n1)

#4.8
'''
root = Treelize(list(range(3,25,2)))

root.printing()
print(f"root:{root.data},left:{root.left.data},right:{root.right.data}")
lroot = root.left
rroot = root.right
print(f"root:{lroot.data},left:{lroot.left.data},right:{lroot.right.data}")
print(f"root:{rroot.data},left:{rroot.left.data},right:{rroot.right.data}")
llroot = lroot.left
lrroot = lroot.right
lrroot.right = TreeNode(4)
print(f"root:{llroot.data},left:{llroot.left.data},right:{llroot.right}")
print(f"root:{lrroot.data},left:{lrroot.left.data},right:{lrroot.right.data}")

print(root.data)
print(ComPare(root,root.left.right.left,root.left.left.left))
'''
