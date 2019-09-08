def swap(a,b):
    return b,a

def bubble_sort(l):
    for i in range(len(l)):
        for j in range(len(l)-1-i):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    return l

def selection_sort(l):
    for i in range(len(l)):
        ind = i
        for j in range(i,len(l)):
            if l[ind]>l[j]:
                ind = j
        l[ind],l[i] = l[i],l[ind]
    return l

def merge_sort(l):
    if len(l)>2:
        left,right = l[:len(l)//2],l[len(l)//2:]
        m_left,m_right = merge_sort(left),merge_sort(right)
    else:
        m_left,m_right = l[:len(l)//2],l[len(l)//2:]
    result = []
    while m_left and m_right:
        if m_left[0]<m_right[0]:
            result += [m_left[0]]
            m_left = m_left[1:]
        else:
            result += [m_right[0]]
            m_right = m_right[1:]
    result = result+m_left+m_right
    return result

def quick_sort(l=list()):
    if len(l)<=1:
        return l
    index = len(l)//2
    num = l[index]
    l = l[:index]+l[index+1:]
    left,right=[],[]
    for i in range(len(l)):
        if l[i]<num:
            left.append(l[i])
        if l[i]>=num:
            right.append(l[i])
    s_left,s_right = quick_sort(left),quick_sort(right)
    res = [num]
    res = s_left+res+s_right
    return res
'''
def func1(l1,l2):
    l = []
    while l1 and l2:
        if l1[0]<l2[0]:
            l += [l1[0]]
            l1 = l1[1:]
        else:
            l += [l2[0]]
            l2 = l2[1:]
    l += l1+l2
    return l
    '''

def func1(a,b):#수정변경
    a_point,b_point = len(a)-len(b)-1,len(b)-1
    t_point = len(a)-1
    while a_point!=-1 and b_point!=-1:
        if a[a_point]>b[b_point]:
            a[t_point] = a[a_point]
            a[a_point] = 0
            a_point -= 1
        else:
            a[t_point] = b[b_point]
            b[b_point] = 0
            b_point -= 1
        t_point -= 1
    a = b[:b_point+1]+a[-t_point:]
    return a

def func2(strings=['abc']):#깔끔하게 푸는법을 모르겠드아...
    table = []
    buffer = []
    for string in strings:
        value = "".join(map(chr,merge_sort(list(map(ord,string)))))#복잡도 개쓰레기ㅠㅠ
        if value not in table:
            table.append(value)
            buffer.append([string])
        else:
            for i in range(len(table)):
                if table[i]==value:
                    buffer[i]+=[string]
                    continue
    res = []
    for i in buffer:
        res += i
    return res

def func3(l=[],n=0):
    mid = (len(l)-1)//2
    start = 0
    last = len(l)-1
    if n==l[start]:
        return start
    if n==l[last]:
        return last
    while True:#case start<mid<last , last<start<mid, mid<last<start
        if last-start==1:
            return False
        if l[start]<l[mid] and l[mid]<l[last]:
            if n==l[mid]:
                return mid
            elif n<l[mid]:
                last = mid
                mid = (start+last)//2
            else:
                start = mid
                mid = (start+last)//2
        elif l[start]<l[mid] and l[start]>l[last]:
            if n==l[mid]:
                return mid
            elif n>l[mid]:
                start = mid
                mid = (start+last)//2
            elif n>l[start]:
                last = mid
                mid = (start+last)//2
            else:
                start = mid
                mid = (start+last)//2
        else:
            if n==l[mid]:
                return mid
            elif n>l[start]:
                last = mid
                mid = (start+last)//2
            elif n>l[mid]:
                start = mid
                mid = (start+last)//2
            else:
                last = mid
                mid = (start+last)//2

class Listy():
    def __init__(self,l=[]):
        self.l = l
    def elementAt(self,i):
        if i>len(self.l)-1:
            return -1
        elif i<0:
            raise ValueError
        else:
            return self.l[i]
    def __str__(self):
        return ("["+", ".join(map(str,self.l))+"]")

def func4(l=Listy(),x=0):
    n = x
    start=0
    while True:
        if l.elementAt(n)==-1:
            last = n
            break
        else:
            n *=2
    while True:
        k = l.elementAt(n)
        if last-start==1:
            return False
        if k==x:
            return n
        elif k ==-1:
            last = n
            n = (start+last)//2
        elif k<x:
            start = n
            n = (last+start)//2
        elif k>x:
            last = n
            n = (start+last)//2

def func5(word,l):#고쳐라예준아
    last = len(l)-1
    start = 0
    index = (start+last)//2
    switch = 1
    befword,bbefword = "",""
    while l[index]!=word:
        print(index,end=" ")
        if l[index]=="":
            index -= 1*switch
        else:#value 자체가 리스트에 존재하지 않는경우는?해결 but 이 경우 많은 탐색을 함
            if bbefword == l[index]:
                return "Not Exist"
            bbefword = befword
            befword = l[index]
            if l[index]<word:
                start = index
                index = (last+start)//2
                switch *= -1
            else:
                last = index
                index = (last+start)//2
                switch *= -1
    return index
# print("func5",end = " ")
# print(func5("balls",["abc","","","","ball","","","carry"]))

def func6(string,longs = 200000000000):
    #1GB씩 16개로 나눠서 각각을 정렬한후, 정렬된 문자쌍 두개를 서로 작은것부터 저장(mergesort하듯이) 
    #하지만 이렇게 하면서 메모리에 초과될수 있으니 정렬된 문자쌍에서 625000000(625MB)씩 먼저 정렬하고 한 쌍이 다 사용되면 꼬리쌍을 꺼내서 정렬한다
    #한쪽이 기존에 정렬된 쌍이 다 정렬될 경우 나머지 부분을 붙여서 save
    #합치면서 합쳐진 값이 1GB가 넘어가면 우선적으로 저장하고 추가적으로 실행
    #20GB = 200000000000Byte = 4 * 4 * 1250000000(AScii)
    #근데 전부 global 선언해버리면 공간 낭비 개심한데 어떻게 로컬로 적정하고할당해주지...?

    # if longs%32 != 0:
    #     return "Only multiples of 32" 
    long = longs//16 
    for i in range(15):#20GB스트링을 1.25GB 16개로 만듬(but 16의 배수가 아닌경우 15개는 크기가 같지만 마지막 만 크기가 다름)
        s = string[i*long:(i+1)*long]
        globals()["string{}".format(i)] = "".join(map(chr,merge_sort(list(map(ord,s)))))
    else:#마지막 16번째 스트링
        s = string[long*15:]
        globals()["string{}".format(15)] = "".join(map(chr,merge_sort(list(map(ord,s)))))
    k = 8
    while k!=0:
        for i in range(k):
            a = globals()["string"+str(2*i)]
            b = globals()["string"+str(2*i+1)]
            destination = 16//k
            #print(a)
            #print(b)
            for n in range(16//k -1):#정렬된 스트링을 625MB로 만듬. 이렇게 해서 정렬된 스트링들 정렬되게 합침
                globals()["a{}".format(n)] = a[(long//2)*n:(long//2)*(n+1)]
                globals()["b{}".format(n)] = b[(long//2)*n:(long//2)*(n+1)]
            else:
                globals()["a{}".format(16//k-1)] = a[(long//2)*(16//k-1):]
                globals()["b{}".format(16//k-1)] = b[(long//2)*(16//k-1):]
            astart = 0
            bstart = 0
            aindex = 0
            bindex = 0
            temp = ""
            sol = ""
            while astart!=destination and bstart!=destination:
                if aindex!=len(globals()["a{}".format(astart)]) and bindex!=len(globals()["b{}".format(bstart)]):#원래long//2
                    if (globals()["a{}".format(astart)])[aindex]<(globals()["b{}".format(bstart)])[bindex]:
                        temp += (globals()["a{}".format(astart)])[aindex]
                        aindex += 1
                    else:
                        temp += (globals()["b{}".format(bstart)])[bindex]
                        bindex += 1
                else:
                    sol += temp
                    temp = ""
                    if aindex==len(globals()["a{}".format(astart)]):
                        aindex = 0
                        astart += 1
                    if bindex==len(globals()["b{}".format(bstart)]):
                        bindex = 0
                        bstart +=1
            if astart==destination and aindex==0:
                while bstart!=destination:
                    sol += globals()["b{}".format(bstart)][bindex:]
                    bindex = 0
                    bstart += 1
            else:
                while astart!=destination:
                    sol += globals()["a{}".format(astart)][aindex:]
                    aindex = 0
                    astart += 1
            globals()["string{}".format(i)] = sol
        k //= 2
    return globals()["string{}".format(0)]

def func7(l,lastnumber = 2**33-1):
    #음이 아닌 정수 40억 개로 이루어진 입력파일이 있다. 이 파일에 없는 정수를 생성하는 알고리즘을 작성하라.(unsigned int)
    #단 메모리는 1GB만들 사용할수 있다.
    #int하나는 32bit라고 한다면, 4byte. 4,000,000,000  * 4 = 16 GB
    #16 = 2*8 = 2*2*4 = 2*2*2*2 = (2**5)*.5
    longs = len(l)
    long = longs//32
    for i in range(31):
        globals()["numbers{}".format(i)] = merge_sort(l[long*i:long*(i+1)])
    else:
        globals()["numbers{}".format(31)] = merge_sort(l[long*31:])
    indexs = [0]*32
    notAppear = []
    for n in range(lastnumber+1):
        for i in range(len(indexs)):
            if indexs[i]<len(globals()["numbers{}".format(i)]):
                if n == globals()["numbers{}".format(i)][indexs[i]]:
                    indexs[i] += 1
                    break
        else:
            notAppear.append(n)
    notAppear.sort()
    return notAppear


def fun8(l):
    #1부터 N(<=32000)까지의 숫자로 이루어진 배열이 있다. 배열엔 중복된 숫자가 나타날 수 있고, N이 무엇인지 알수 없다.
    #사용 가능한 메모리가 4KB일때, 중복된 원소를 모두 출력하려면 어떻게 할수있을까
    #4KB = 4000Byte = 32000 bit
    #즉 각 비트 index를 수라고 보고 크기가 32000인 bit array를 만든다
    numbers = [False]*32000 # l = bit[32001]
    for i in range(len(l)):
        num = l[i]
        if numbers[num-1] == False:
            numbers[num-1] = True
    sol = []
    for i in range(len(numbers)):
        if numbers[i]==False:
            sol.append(i)
    return sol

def func9(l,number = 0):
    #이 문제가 값이 하나밖에 존재 하지 않는다고 가정!
    m = len(l[0])
    n = len(l)
    RS,CS = 0,0#(rowstart,columnstart)
    RL,CL = n-1,m-1
    while True:
        #print(f"RS={RS},RL={RL},CS={CS},CL={CL}")
        if RS==RL and CS==CL:
            print(l[RS][CS])
            return (RS,CS)
        if not(l[RS][CS]<=number and number<=l[RS][CL]) and RS<RL:
            RS += 1
            continue
        if not(l[RS][CS]<=number and number<=l[RL][CS]) and CS<CL:
            CS += 1
            continue
        if not(l[RL][CS]<=number and number<=l[RL][CL]) and RS<RL:
            RL -= 1
            continue
        if not(l[RS][CL]<=number and number<=l[RL][CL]) and CS<CL:
            CL -= 1
            continue
        break
    return "Can\'t Find"


#10번
#priority queue 로 구현가능하긴함(불가능함
#priority queue 는 heap형태라서 이분탐색 안됨
#priority queue 를 원하는 숫자를 추출하는데 log n 되게 추출이 가능한가?(불가능한거같음)
################################################
#priority Queue Version(logn)(heap)
from queue import PriorityQueue
def find(l,number):
    start,last = 0,len(l)-1
    mid= (start+last)//2
    if l[start]==number:
        return start
    if l[last]==number:
        return last
    while l[mid]!=number:
        if l[mid]<number:
            start = mid
            mid = (start+last)//2
        else:
            last = mid
            mid = (start+last)//2
    return mid

# l = PriorityQueue()
# for i in [5,1,4,4,5,9,7,13,3]:
#     l.put(i)
# lst = l.queue
# print(find(lst,5))
################################################

#list로 구현한다고 하면,
#그래도 모르겟는데요ㅠ
class qqueue():
    def __init__(self):
        self.array = []
        self.long = 0
    def track(self,data):
        last = self.long-1
        start = 0
        if self.long == 0:
            self.array.append(data)
            self.long+=1
            return
        if self.array[start]>data:
            self.array = [data]+self.array
            self.long+=1
            return
        if self.array[last]<data:
            self.array = self.array+[data]
            self.long+=1
            return
        while last-start>1 and data!=self.array[(last+start)//2]:
            if self.array[(last+start)//2]>data:
                last = (last+start)//2
            if self.array[(last+start)//2]<data:
                start = (last+start)//2
        self.array = self.array[:last]+[data]+self.array[last:]
        self.long+=1
        return
    def getRankOfNumber(self,number):
        start = 0
        last = self.long-1
        while number!=self.array[(last+start)//2]:
            if last-start<=1:
                return "Not Exist"
            if self.array[(last+start)//2]>number:
                last = (last+start)//2
            if self.array[(last+start)//2]<number:
                start = (last+start)//2
        index = (last+start)//2
        while self.array[index]==self.array[index+1]:
            index+=1
        return index

l = qqueue()
for i in [5,1,4,4,5,9,7,13,3]:
    l.track(i)
print(l.array)
for i in range(10):
    print(l.getRankOfNumber(i))




# stream = Node()
# for i in range([5,1,4,4,5,9,7,13,3]):
#     stream.track(i)



def func11(l):
    #가장 simple
    #sorting 해서 max,min순으로 계속해서 나옴
    #but 동치들이 많을때 에러가 뜰수있음
    #큰거순, 작은거순으로 해보고 True,False로 감소 증가 판단해서 하면 될거같긴함...
    #근데 이거로 답이 안나오는데, 존재하는 답이 없다는 보장을 할수가 있는가?
    #그건 모르겟네여ㅠㅠㅠ
    #글고 이 문제가 요구하는 게 한가지 케이스만 출력하라는 건지,
    #아니면 모든 케이스를 다출력하라는 건지(근데 출력기준으로 이건 아닌거같음)
    s_l = merge_sort(l)
    switch = True
    check = True
    seq = []
    for _ in range(len(l)):
        if switch==True:
            value,s_l = s_l[-1],s_l[:-1]
            seq.append(value)
            switch = False
        else:
            value,s_l = s_l[0],s_l[1:]
            seq.append(value)
            switch = True
    switch = 1 #첫 값은 감소
    index = 1
    while index!=len(l):
        if switch*(seq[index]-seq[index-1])<0:
            index,switch = index+1,switch*(-1)
        else:
            check = False
            break
    if check==False:
        s_l = merge_sort(l)
        switch = False
        check = True
        seq = []
        for _ in range(len(l)):
            if switch==True:
                value,s_l = s_l[-1],s_l[:-1]
                seq.append(value)
                switch = False
            else:
                value,s_l = s_l[0],s_l[1:]
                seq.append(value)
                switch = True
        switch = -1 #첫 값은 증가
        index = 1
        while index!=len(l):
            if switch*(seq[index]-seq[index-1])<0:
                index,switch = index+1,switch*(-1)
            else:
                check = False
                break
    if check==False:
        return "can't find"
    else:
        return seq
        
    




#print(func1([1,3,7,10],[2,5,8,9]))
#print(func3([15,16,19,20,25,1,3,4,5,7,10,14],5))
#a = Listy([1,1,1,1,2,2,2,3,4,4,4,4,4,5,6,7,9,10])
#print(f"listy{func4(a,5)}")
#print(func4(a,7))
#strings = ["abc","bac","cab","adb","adv","cdv","dvc"]
#print(func2(strings))
#print(func6("nkgdeochifplambjabcdefghijklmnop",32))
#print("".join(sorted("nkgdeochifplambjabcdefghijklmnop")))
print(func6("abcdefghijklmnopabcdefghijklmnopabcdefghijklmnop",48))
print(func6("hefjbgkldcmai",13))
import random
permutation2 = list(range(10))
permutation2.remove(4)
permutation2.remove(8)
permutation = list(range(65))
permutation.remove(32)
permutation.remove(64)
random.shuffle(permutation)
random.shuffle(permutation2)
# for i in [1,6,11,16,3,8,12,19,5,9,14,22,7,10,15,23]:
    # print(func9([[1,6,11,16],[3,8,12,19],[5,9,14,22],[7,10,15,23]],i))
print("func11",end = "  ")
print(func11([1,3,3,3,5]))


import unittest
class Test(unittest.TestCase):
  def test_sort(self):
    array = [1,3,2,4,5,9,7,8,6]
    a = Listy([1,3,5,9,10])
    self.assertEqual(bubble_sort(array), sorted(array))
    self.assertEqual(selection_sort(array), sorted(array))
    self.assertEqual(merge_sort(array), sorted(array))
    self.assertEqual(quick_sort(array), sorted(array))
    self.assertEqual(func1([1,3,7,10,0,0,0,0],[2,5,8,9]),[1,2,3,5,7,8,9,10])
    self.assertEqual(func3([15,16,19,20,25,1,3,4,5,7,10,14],5),8)
    self.assertEqual(func4(a,1),0)
    self.assertEqual(func4(a,2),False)
    self.assertEqual(func4(a,3),1)
    self.assertEqual(func4(a,4),False)
    self.assertEqual(func4(a,5),2)
    self.assertEqual(func4(a,6),False)
    self.assertEqual(func4(a,7),False)
    self.assertEqual(func4(a,8),False)
    self.assertEqual(func4(a,9),3)
    self.assertEqual(func4(a,10),4)
    self.assertEqual(func4(a,11),False)
    self.assertEqual(func7(permutation,64),[32,64])
    self.assertEqual(func7(permutation2,9),[4,8])
if __name__ == "__main__":
    unittest.main()
