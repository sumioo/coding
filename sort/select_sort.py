#coding:utf-8
def select_sort(L):                     #选择排序--选择当前值为最小值，比较当前值与剩余
    n=len(L)                            #序列，当发现比当前值小的，把此索引值赋给min
    for i in range(0,n-1):              #进行比较的最小值改变
        min=i
        for j in range(i+1,n):
            if L[min]>L[j]:
                min=j
        if min!=i:
            L[i],L[min]=L[min],L[i]

L=[1,9,9,1,2,3,5,4,8]
select_sort(L)
print L
