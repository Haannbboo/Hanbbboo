#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 20:39:05 2018

@author: hanbo
"""
import os
import requests
from pyquery import PyQuery as pq
import json
import time
import string
import re
import numpy
from numpy.linalg import inv
import math
import matplotlib.pyplot as plt


def getData():
    '''
    Get house info from bj.lianjia.com, a leading Chinese house service website
    Info includes house info, position info, and price info
    Will be stored in a txt called result.txt'''
    def house(url):
        '''Parsing function
        Automatically receives url with page No. from __main__ below
        Parse using PyQuery'''
        try:
            headers={
                'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
                }
            doc=pq(requests.get(url,headers=headers,timeout=5,verify=False).text) # Get url info
        except Exception:
            doc=pq(requests.get(url,headers=headers,timeout=5,verify=False).text) # Try one more time
        # Parse    
        house=doc('.houseInfo').items() # Iterable pyquery object of house info
        hr=[item.text() for item in house]
        position=doc('.flood .positionInfo').items() # Iterable pyquery object of house position info
        pr=[items.text() for items in position]
        price=doc('.priceInfo').items() # Get an iterable pyquery object of house price
        prr=[itemss.text() for itemss in price] 
            
        for i in range(len(hr)):
            # Write to file
            with open('result.txt','a',encoding='utf-8') as f:
                f.write(json.dumps(hr[i].split('/')+pr[i].split('/')+prr[i].split('/'), ensure_ascii=False)+'\n')

    def main(page):
        '''Main parsing function'''
        try:
            url='https://bj.lianjia.com/ershoufang/pg'+str(page) # url with changing page No.
            house(url) # Call the getter and parser function
            time.sleep(1) # To avoid auto rejection from the websites
        except Exception as er:
            print("Error: ",er)

    if __name__=='__main__':
        print("Collecting data from lianjia.com")
        print("Please wait for the process bar to finish")
        print("Each '>' represents 2% of process")
        import warnings  # Eliminate warnings coming from eliminating ssl verification
        warnings.filterwarnings('ignore')
        
        for i in range(1,101):
            main(i) # Call main with page number: i
            if i%2==0:
                print('>',end='')
        print("Done")
         
def getFile():
    '''Call file'''
    raw=open('result.txt','r',encoding='utf8').readlines() # Open result file and readlines to a list
    return raw

def dataWash(raw):
    '''Receive raw data from getFile()
    Data cleaning process, including: eliminating undesired puntuations, represents figurative features in numbers, applying normalization to numbers, and matrify
    Returns the list with x matrix and y matrix'''
    sign=string.punctuation.replace('.','')+'n' # Gather all punctuations that need to get rid off
    global table
    table=str.maketrans('','',sign) # Use maketrans to delete undesired characters <- 'sign'
    #global rx,ry
    rx,ry=[],[]
    global miss
    missx=0
    for i in raw:
        #x_init=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] # Initialized later in formatingX(xRaw) function
        # x: [room,living,size,east,south,west,north,jing,jian,mao,yeselev,noelev,topflr,highflr,midflr,lowflr,btmflr,year]
        #y_init=[0] # Initialized later in formatingY(yRaw) function
        # y: [house_total_price]
        
        info=i.translate(table).split(' ') # Elimination of undesired punctuations
        xRaw,yRaw=info[2:-3],info[-2]
        xRaw[2:-4]=[''.join(xRaw[2:-4])] # Get desired slices
        
        try:
            x_init=formatingX(xRaw) # Formating x data
            y_init=formatingY(yRaw) # Formating y data
            # Append to result list
            rx.append(x_init)
            ry.append(y_init)
        except Exception:
            missx+=1
    outlier_index=removeOutliers(ry)
    for ind in ourlier_index:
        ry.pop(ind)
        rx.pop(ind)
    global y_cleaned,x_cleaned
#    y_cleaned=outliers_out[0]
#    x_cleaned=outliers_out[1]
    y_cleaned=ry[:]
    x_cleaned=rx[:]
    x=numpy.asarray(x_cleaned)
    y=numpy.asmatrix(y_cleaned) # Matrify
    
    def featureScaling(x): # Normalization of all data
        for i in [0,1,2]: # Get mean and std of each x vector
            m=x[:,[i]].mean()
            std=x[:,[i]].std()
            for j in range(len(x)):
                x[j][i]=(x[j][i]-m)/math.pow(std,2) # Normalize all data
        return x
    
    fx=numpy.matrix(featureScaling(x)) # Matrify x
    allData=[fx,y] # Return value
    #print("Done: {}%".format(missx/len(raw)*100))
    return allData

def formatingX(xRaw): # Formate x raw data
    x_init=[0]*17 # Initialize x
    try:
        x_init[0]=int(xRaw[0][0]) # Bedroom No.
        x_init[1]=int(xRaw[0][-2]) # Living room No.
        x_init[2]=float(xRaw[1][:-2]) # Size in m2
        pos=xRaw[2] # Direction
        if chr(19996) in pos:
            x_init[3]=1
        if chr(21335) in pos:
            x_init[4]=1
        if chr(35199) in pos:
            x_init[5]=1
        if chr(21271) in pos:
            x_init[6]=1           # Give 1&0 to directions of house
        fur={31934:7,31616:8,27611:9}
        ind_fur=fur[ord(xRaw[3][0])] 
        x_init[ind_fur]=1 # Furnituring status
        elev={26377:10,26080:11}
        ind_ele=elev[ord(xRaw[4][0])]
        x_init[ind_ele]=1 # Elevator y/n
        flr={20302:15,20013:14,39640:13,39030:12,24213:16}
        ind_flr=flr[ord(xRaw[5][0])]
        x_init[ind_flr]=1 # Floor location
        #x_init[17]=int(xRaw[6][0:4]) # Year of built
    except Exception:
        raise ValueError # For the try-exceot in dataWash(raw) function
    return x_init
def formatingY(yRaw): # Format y raw data
    y_init=[0]
    try:
        y_init[0]=float(re.findall("\d+",yRaw)[0]) # Fill in y data with total price of the house
    except Exception:
        raise ValueError
    return y_init

def removeOutliers(y):
    temp=numpy.array(y)
    upper,lower=numpy.percentile(temp,75),numpy.percentile(temp,25)
    IQR=upper-lower
    IQRset=(lower-1.5*IQR,upper+1.5*IQR)
    index=[]
    i=0
    while i<len(temp):
        a=y[i]
        if a<=IQRset[0] or a>=IQRset[1]:
            index.append(i)
        i+=1
            
    return index

    
class linrg:
    '''Use for linear regressiorx'n, including normal equation and graident decent
    Take in a list with list[0] -> matrix of x and list[1] -> matrix of y
    Default dataWash() function'''
    def __init__(self):
        self.allData=dataWash(getFile())
    def getX(self):
        '''Get x matrix'''
        return self.allData[0]
    def getY(self):
        '''Get y matrix'''
        return self.allData[1]
    def getLearnData(self):
        '''Select some data as the learning data set
        Return the learning data set as a list of x matrix and y matrix -> list[x,y]'''
        l=len(self.allData[0])
        learnData=[numpy.matrix(numpy.vstack((self.allData[0][0:l//8],self.allData[0][l//7+1:l//6],self.allData[0][l//5+1:]))),numpy.matrix(numpy.vstack((self.allData[1][0:l//8],self.allData[1][l//7+1:l//6],self.allData[1][l//5+1:])))]
        return learnData
    
    def normal_allData(self):
        '''Normal equation for all data got from dataWash() function
        Returns a result matrix'''
        x,y=self.allData[0],self.allData[1]
        result=inv(x.getT()*x)*x.getT()*y
        return result
    def normal_specificData(self,dataSet):
        '''Normal equation for specific data set within <class linrg>
        Returns a result matrix'''
        x,y=dataSet()[0],dataSet()[1] # Get x & y matrix
        result=inv(x.getT()*x)*x.getT()*y
        return result
    
    def getTestData(self):
        '''Select some data as the test data set
        Return the testing data set as a list of x matrix and y matrix -> list[x,y]'''
        l=len(self.allData[0])
        testData=[self.allData[0][l//6:l//5],self.allData[1][l//6:l//5]]
        return testData
    def getDevelopData(self):
        '''Select some data as the develop data set
        Return the development data set as a list of x matrix and y matrix -> list[x,y]'''        
        l=len(self.allData[0])                                                                          
        developData=[self.allData[0][l//8:l//7],self.allData[1][l//8:l//7]]
        return developData
    
    def GradientDecent(self,alpha=0.000000001,times=100,n=17):
        '''Gradient decent for data from getLearnData() in <class linrg>
        :alpha: int -> learning rate of gradient decent, default 0.0000000001
        :times: int -> times of iteration, default 100
        Returns a result matrix'''
        x,y=self.getLearnData()[0],self.getLearnData()[1] # Get x & y matrix
        #theta=numpy.matrix((math.sqrt(x.std())*numpy.random.randn(18,1)+x.mean())/100) # Initialize theta
        theta=numpy.matrix(numpy.ones(n)).getT()
        temp=theta
        l=len(x)
        J=[0]*times # Initialize cost function
        #iteration=[i for i in range(1,times)] # Initialize iteration times
        for i in range(times):
            # theta j := theta j + alpha*(y-h(x))*x
            # temp=theta+alpha*numpy.sum((y-numpy.dot(x,theta))*x.getT())/2532
            # Main loop
            # Simultaneously update theta
            for j in range(n):
                temp[j]=theta[j]+alpha*numpy.sum((y-numpy.dot(x,theta)).getT()*x[:,j])/l
            #temp[17]=theta[17]+alpha*numpy.sum((y-numpy.dot(x,theta))*x[:,17].getT())/2532
            J[i]=0.5*numpy.sum(numpy.power((y-(x*theta)),2))/l # Cost function update
            if i%50==0:
                print(J[i])
            theta=temp
            if abs(J[i]-J[i-1])<1:
                break
        return theta
    
    def testModel(self):
    #Testing function
    #Automatically get data and perform both normal equation and gradient decent
    #Calculate RMSE of two methods, and give RMSE values Return RMSEs -> Normal_equation, Gradient_decent
        data=self.getDevelopData() # Get develop data
        xt,y=data[0],data[1]
        r=self.normal_specificData(self.getDevelopData) # Get result using normal equation
        ytn=xt*r # Estimated y matrix
        RMSENormal=round(numpy.sqrt(numpy.power((ytn-y),2).mean()),3) # RMSE value for normal equation
        r=self.GradientDecent(0.0000000001,100)
        ytg=xt*r
        RMSEGrad=round(numpy.sqrt(numpy.power((ytg-y),2).mean()),3) # RMSE value for gradient decent
#        print("="*27+"Testing with RMSE"+"="*27)
#        print("Normal equation: RMSE="+str(RMSENormal)+" "*5+"|"+" "*5+"Gradient decent: RMSE="+str(RMSEGrad))
#        print("="*71)
        return [RMSENormal,RMSEGrad]
        
def draw(x_cleaned,y_cleaned,n): # Not done yet
    x,y=numpy.asmatrix(x_cleaned),numpy.asmatrix(y_cleaned)
    global gradient
    gradient=r_grad
    global x_all
    x_all=[]
    for i in range(n):
        temp=numpy.array(x[:,i].getT())
        x_all.append(temp)
#        numpy.transpose(numpy.array(x)[:i])] # Get all feature data
    x_name=['Bedroom','Living room','Size','East','South','West','North',
            'Well furnitured','Simple furnitured','No furnitute',
            'Has elevator','No elevator',
            'Top floor','High floor','Middle floor','Low floor','Bottpm floor','Year']
    y_all=numpy.array(y.getT())
    import matplotlib.pyplot as plt
    plt.figure()
    global index
    index=0
    plot(2,1,2,x_all,y_all,x_name,gradient,0)
    plot(1,1,1,x_all,y_all,x_name,gradient,2)
    plot(2,2,4,x_all,y_all,x_name,gradient,3)
    plot(3,1,3,x_all,y_all,x_name,gradient,7)
    plot(2,1,2,x_all,y_all,x_name,gradient,10)
    plot(3,2,n-12,x_all,y_all,x_name,gradient,12)
##    plt.subplot(2,1,1)
##    plt.scatter(x_all[0],y_all)
##    plt.xlabel(x_name
##    plt.plot(x_all[0])
##    plt.show()
def plot(a,b,c,x_all,y_all,x_name,gradient,index):
    for i in range(1,c+1):
        #print(index)
        x=x_all[index]
        plt.subplot(a,b,i)
        plt.scatter(x,y_all)
        plt.xlabel(x_name[index])
        plt.ylabel('Price')
        plt.plot(x,gradient.item(index)*x,'r')
        plt.show()
        index+=1
        

def Init():
    '''User connection function
    Ask for user's features and gives back results of estimated price of both normal equation and gradient decent'''
    if os.access('result.txt', os.F_OK) and os.access('result.txt', os.R_OK): # Check if the result file exists
        pass
    else:
        getData()
    global user
#    user=[input("How many bedrooms: ")+'室'+input("How many livingrooms: ")+'厅',input("Size of the house in m2: ")+'平米',input("Direction of the rooms: "),
#          input("Furnishing status(精装 简装 平装 毛坯): "),input("Elevator(有无电梯): "),input("Floor level(顶层 高楼层 低楼层 中层 底层): "),input("Year of built: ")] # Ask for user's feature and store in a list
    user=['2室1厅', '77.7平米', '南北', '精装', '无电梯', '底层', '1999']
    data=formatingX(user) # Formating the user input
    test=linrg() # Initialize linear regression
    n=17 # Number of features to consider
    r_normal=test.normal_specificData(test.getLearnData) # LG using normal equation
    global r_grad
    r_grad=test.GradientDecent(0.015,1000,n) # LG using gradient decent
    # Output data
    print("="*24+"User house price calculation"+"="*24)
    print("-"*20+"Result"+"-"*20)
    global r1,r2
    r1=data*r_normal # Estimated price using normal equation
    r2=(data*r_grad).item(0) # Estimated price using gradient decent
    print("Estimated house price: "+str(round(r2*10,2))+"k RMB")
    print("="*27+"User house price calculation"+"="*27)
    #draw(x_cleaned,y_cleaned,n)
          
    



    
