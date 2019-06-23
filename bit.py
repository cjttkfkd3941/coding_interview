#5.1 / 2진수 형태로 입력받아서 연산후 2진법형태로 출력

n = int(input("N:"),2)
m = int(input("M:"),2)
i = int(input("i:"))
j = int(input("j:"))
n1 = n&(2**i-1)
n = (n>>j)<<j
m = m<<i
n = n+m+n1
print(bin(n)[2:])

#5.2 1번째버젼

n = float(input())
check = 1
s = "0."
while n!=0 and check<=31:
    if n>.5**check:
        n = n-.5**check
        s+="1"
    else:
        s+="0"
    check+=1

if len(s)<=32:
    print(s)
else:
    print("ERROR")

   
#5.2 ver_2
n = float(input())
if n*2**32%1!=0:
    print("ERROR")
else:
    s = "0."
    while n!=0:
        n *= 2
        s+=str(n//1)
        n = n%1
    print(s)


#5.3
n = input()
try:
    n=int(n,2)
except:
    n =int(n)
bn = "00"+bin(n)[2:]+"00"
start=len(bn)+1
mid=len(bn)+1
fin=len(bn)+1
max = 0
for i in range(len(bn)-1,-1,-1):
    if bn[i]=="0":
        if start>len(bn):
            start=i
        elif mid>len(bn):
            mid=start
            start = i
        else:
            fin = mid
            mid = start
            start = i
    if max<abs(start-fin+1):
        max = abs(start -fin+1)
if n==0:
    max = 1
print(max)
print(bn)


#5.4(64bit기준)
n = int(input())
count = 0
while n!=0:
    if n- (n>>1)*2==1:
        count +=1
    n = n>>1
min = int("1"*count,2)
max = min<<(63-count)#근데 int 63bit가 숫자고 1비트는 부호인데 그 값들을 다넘기는지,65로 해도 변환하면 됨...뭐지...
print(bin(max))
print(max)
print(bin(min))
print(min)

#5.5
n = int(input())
n2 = n-1
bn = "0"+bin(n)[2:]
bn2= "0"+bin(n2)[2:]
result = ["0"]*(len(bn))
num = (len(result)-1)
print(bn)
print(bn2)
print(num)
while num!=-1:
    if bn[-1]=="1" and bn2[-1]=="1":
        result[num] = "1"
    num-=1
    bn,bn2 = bn[:-1],bn2[:-1]

print("result = ",int("".join(result),2))
result = int("".join(result),2)
print(result==0,end=" ")
print("즉 2의 k승일때만 True")

#5.6
a,b = input().split(",")
try:
    a = int(a,2)
    b = int(b,2)
except:
    a = int(a)
    b = int(b)
ba = bin(a)[2:]
bb = bin(b)[2:]
if len(ba)-len(bb)<0:
    ba = "0"*(len(bb)-len(ba))+ba
else:
    bb = "0"*(len(ba)-len(bb))+bb
count = 0
print(ba)
print(bb)
for i in range(len(ba)):
    if ba[i]!=bb[i]:
        count += 1
print(count)

#5.7
n = int(input())
func = int("101010101010101010101010101010101010101010101010101010101010101",2)
n1 = n&func
n2 = n&(func<<1)
n1,n2 = n1<<1,n2>>1
n = n1|n2
print(n)

