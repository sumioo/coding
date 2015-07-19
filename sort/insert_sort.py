from random import randint
def insert_sort(L):
    n=len(L)
    L.insert(0,0)
    for i in range(2,n+1):
        if L[i]<L[i-1]:
            L[0]=L[i]
            for j in range(i-1,-1,-1):
                if L[j]<=L[0]:
                    L.insert(j+1,L.pop(i))
                    #print L,'*',i
                    break
            #L[0]=0
    L.pop(0)
if __name__ == '__main__':
    L=[randint(-100,100) for i in range(0,10001)]
    insert_sort(L)
