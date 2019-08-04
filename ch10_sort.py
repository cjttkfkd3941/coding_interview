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
#요구조건 충족 못하는 코드
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

def func2(strings=['abc']):#깔끔하게 푸는법을 모르겠음...
    table = []
    buffer = []
    for string in strings:
        value = "".join(map(chr,merge_sort(list(map(ord,string)))))
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
        

#print(func1([1,3,7,10],[2,5,8,9]))
#print(func3([15,16,19,20,25,1,3,4,5,7,10,14],5))
#a = Listy([1,1,1,1,2,2,2,3,4,4,4,4,4,5,6,7,9,10])
#print(f"listy{func4(a,5)}")
#print(func4(a,7))
strings = ["abc","bac","cab","adb","adv","cdv","dvc"]
print(func2(strings))

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
if __name__ == "__main__":
    unittest.main()
