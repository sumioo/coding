#coding:utf-8
'''
外层循环控制内层循环次数，内层循环控制比较次数
'''
import pickle
from random import randint

def bubble_sort(L):
	n=len(L)
	for i in range(n-1):
		for j in range(i,n):
			if L[j]<L[i]:                #L[i]的位置是固定的，每次比较有一个数的位置是固定的
				L[i],L[j]=L[j],L[i]


def bubble_sort_2(L):
	n=len(L)
	for i in range(0,n-1):
		for j in range(-n,-i-1):
			if L[j]>L[j+1]:					#每次比较的数其位置不是固定的
				L[j],L[j+1]=L[j+1],L[j]


def bubble_sort_3(L):
	flag=True
	n=len(L)
	for i in range(0,n-1):
		if flag==True:
			flag=False
			for j in range(-n,-i-1):
				if L[j]>L[j+1]:
					L[j],L[j+1]=L[j+1],L[j]
					flag=True
					#print '**'
		else:continue


"""
with open('D:\py\list_for_sort','r') as f:
	L=pickle.load(f)
	print L[0:100]
"""
if __name__ == '__main__':
    L=[randint(-100,100) for i in range(0,10001)]
    bubble_sort_2(L)
