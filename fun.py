
def freq(lis):
  res=[]
  freqi={}
  for i in lis:
    l=len(i)
    if(l in freqi):
      freqi[l]+=1
    else:
      freqi[l]=1
  freqi={k: v for k, v in sorted(freqi.items(), key=lambda item: item[1])}
  k=list(freqi.keys())
  v=list(freqi.values())
  for d in range(len(k)):
    for i in lis:
      if len(i)==k[d]:
        res.append(i)
        
  print(res)