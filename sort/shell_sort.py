#coding:utf-8
from random import randint
def shell_sort(L):
    n=len(L)
    increment=1
    while increment<=n/3:
        increment=increment*3+1
    while increment>=1:
        for i in range(increment,n):
            #print i,'-'
            for j in range(i,increment-1,-increment):
                if L[j-increment]>L[j]:
                    L[j],L[j-increment]=L[j-increment],L[j]
                    #print 'swap',j,j-increment
                else:
                    #print j,'+++'
                    break
        increment/=3
        #print '/////////////'
        #print L
def check(L):
    for i,j in zip(L,L[1:]):
        if i>j:
            print i,j
            print 'list is not sorted'

if __name__ == '__main__':
    L=[randint(-100,100) for i in range(0,10001)]
    #L=['S','H','E','L','L','S','O','R','T','E','X','A','M','P','L','E']
    #L=[15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]
    print L[0:100]
    shell_sort(L)
    #print L
    #check(L)
