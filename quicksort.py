def partition(a,lb,ub):
  pivot=a[lb]
  i=lb
  j=ub
  while lb<=ub:
    while i<=j and a[i]<=pivot:
       i=i+1
    while i<=j and a[j]>pivot:
        j=j-1
    if i<=j:
       a[i],a[j]=a[j],a[i]
    else:
        a[lb],a[j]=a[j],a[lb]
        return j
def quicksort(a,lb,ub):
   if(lb<ub):
     pos=partition(a,lb,ub)
     quicksort(a,lb,pos-1)
     quicksort(a,pos+1,ub)
   else:
      return a
a=[34,98,0,3,2,1]
quicksort(a,0,5)
print(a)