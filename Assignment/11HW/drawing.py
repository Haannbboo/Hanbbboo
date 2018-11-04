# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import time
import itertools as it

def insertion(list1):
    '''list1 -> list object
    Return sorted list1 with insertion sort'''
    n=len(list1)
    for i in range(n):
        for j in range(i):
            if list1[i]<list1[j]:
                list1.insert(j,list1.pop(i))
                break
    return list1

def selection(list1):
    '''list1 -> list object
    Return sorted list1 with selection sort'''
    for i in range(len(list1)):
        x=i
        for j in range(1,len(list1)):
            if list1[j]<list1[i]:
                x=j
        list1[i],list1[x]=list1[x],list1[i]
    return list1

def bubble(list1):
    '''list1 -> list object
    Return sorted list1 with bubble sort'''
    for i in range(len(list1)):
        for j in range(i, len(list1)):
            if list1[i] > list1[j]:
                list1[i], list1[j] = list1[j], list1[i]
    return list1

def merge(list1):
    '''list1 -> list object
    Return sorted list1 with merge sort'''
    def alg(a,b):
        result=[]
        while len(a) and len(b):
            if a[0]<=b[0]:
                result.append(a.pop(0))
            elif b[0]<=a[0]:
                result.append(b.pop(0))
        if len(a)!=0:
            result+=a
        elif len(b)!=0:
            result+=b
        return result    
    def merge_sort(list1):
        if len(list1)==1:
            return list1
        mid=len(list1)//2
        a=merge_sort(list1[:mid])
        b=merge_sort(list1[mid:])
        return alg(a,b)
    merge_sort(list1)

def timing(f,l):
    a=list(np.random.random_sample(l))
    start=time.clock()
    f(a)
    end=time.clock()
    return end-start

def drawing():
    f=open("times.txt","w")
    fig=plt.figure()
    fig.suptitle('Running time for four sorting alg')
    num=it.count(0,500)
    ts=it.takewhile(lambda x: x<=5000,num)
    x=[1000,2000,3000,4000,5000]
    data=[[],[],[],[]]
    for i in ts:
        data[0].append(timing(insertion,i))
        data[1].append(timing(selection,i))
        data[2].append(timing(bubble,i))
        data[3].append(timing(merge,i))
    l1,=plt.plot(x,data[0],color="red",label="insection")
    l2,=plt.plot(x,data[1],color="green",label="selection")
    l3,=plt.plot(x,data[2],color="blue",label="bubble")
    l4,=plt.plot(x,data[3],color="yellow",label="merge")
    
        
