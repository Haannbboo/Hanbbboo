import numpy
import time

class sorting(object):
    def insertion(list1,output=False):
        '''list1 -> list object
        Return sorted list1 with insertion sort'''
        n=len(list1)
        insert,pop=list1.insert,list1.pop
        for i in range(n):
            for j in range(i):
                if list1[i] < list1[j]:
                    insert(j, pop(i))
                    if output:
                        print(list1)
                    break

    def selection(list1,output=False):
        '''list1 -> list object
        Return sorted list1 with selection sort'''
        n=len(list1)
        for i in range(n):
            x=i
            for j in range(i,n):
                if list1[j]<list1[x]:
                    x=j
            list1[i],list1[x]=list1[x],list1[i]
            if output:
                print(list1)
        return list1

    def bubble(list1,output=False):
        '''list1 -> list object
        Return sorted list1 with bubble sort'''
        n=len(list1)
        for i in range(n):
            for j in range(i, n):
                if list1[i]>list1[j]:
                    list1[i],list1[j]=list1[j],list1[i]
                    if output:
                        print(list1)
        return list1

    def merge(list1,output=False):
        '''list1 -> list object
        Return sorted list1 with merge sort'''
        def alg(a,b):
            result=[]
            append=result.append
            popa,popb=a.pop,b.pop
            while len(a) and len(b):
                if a[0]<=b[0]:
                    append(popa(0))
                elif b[0]<=a[0]:
                    append(popb(0))
            if len(a)!=0:
                result+=a
            elif len(b)!=0:
                result+=b
            if output:
                print(result)
            return result    
        def merge_sort(list1):
            n=len(list1)
            if n==1:
                return list1
            mid=n//2
            a=merge_sort(list1[:mid])
            b=merge_sort(list1[mid:])
            return alg(a,b)
        merge_sort(list1)

    def quick(list1,output=False):
        n=len(list1)
        def sorting(left,right):
            if left>right:
                return
            l,r=left,right
            pivot=list1[l]
            while l<r:
                while l<r and list1[r]>pivot:
                    r-=1
                while l<r and list1[l]<=pivot:
                    l+=1
                list1[l],list1[r]=list1[r],list1[l]
            if output:
                print(list1)
            list1[l],list1[left]=pivot,list1[l]
            sorting(left,l-1)
            sorting(r+1,right)
        sorting(0,n-1)
        return list1

        

        
