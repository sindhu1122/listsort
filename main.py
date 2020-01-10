import fun
n=int(input())
lis=[]
for i in range(n):
  l=list(map(str,input().split()))
  lis.append(l)
lis.sort(key=len)
print(lis)
fun.freq(lis)