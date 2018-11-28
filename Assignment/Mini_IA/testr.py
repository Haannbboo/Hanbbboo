'''
Created on Oct. 18th

@author: Hanbo

:House price prediction with linear regression
'''
import os
import requests
from pyquery import PyQuery as pq
import json
import time
import string
import numpy
from numpy.linalg import inv
import math
import re
#from mpl_toolkits import mplot3d
#import matplotlib.pyplot as plt


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
            doc=pq(requests.get(url,headers=headers,timeout=5,verify=False).text)
        except Exception as e:
            doc=pq(requests.get(url,headers=headers,timeout=5,verify=False).text)
            
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
            house(url) # Call the parsing function
            time.sleep(1) # To avoid auto rejection from the websites
        except Exception as er:
            print("Error: ",er)

    if __name__=='__main__':
        #if os.access('result.txt', os.F_OK) and os.access('result.txt', os.R_OK): # Check if the result.txt exist
 #           x=open('result.txt','r').readlines()
 #           if len(x)>=1000: # Check if the result.txt file has enough data
 #               return "House price data file already exist!"
        print("Collecting data from lianjia.com")
        
        import warnings  # Eliminate warnings coming from ssl verification
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

    rx,ry=[],[]
    missx=0
    for i in raw:
        x_init=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] # Initialize x
        # x: [room,living,size,east,south,west,north,jing,jian,mao,yeselev,noelev,topflr,highflr,midflr,lowflr,btmflr,year]
        y_init=[0] # Initialize y
        # y: [house_total_price]
        
        info=i.translate(table).split(' ') # Elimination of undesired punctuations
        xRaw,yRaw=info[2:-3],info[-2]
        xRaw[2:-4]=[''.join(xRaw[2:-4])] # Get desired slices
        
        try:
            x_init[0]=int(xRaw[0][0]) # Bedroom No.
            x_init[1]=int(xRaw[0][-2]) # Living room No.
            x_init[2]=float(xRaw[1][:-2]) # Size in m2
            pos=xRaw[2]
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
            x_init[ind_fur]=1 # Furniture status
            elev={26377:10,26080:11}
            ind_ele=elev[ord(xRaw[4][0])]
            x_init[ind_ele]=1 # Elevator y/n
            flr={20302:15,20013:14,39640:13,39030:12,24213:16}
            ind_flr=flr[ord(xRaw[5][0])]
            x_init[ind_flr]=1 # Floor location
            x_init[17]=int(xRaw[6][0:4]) # Year of built
            
            y_init[0]=float(re.findall("\d+",yRaw)[0]) # Fill in y data
            rx.append(x_init)
            ry.append(y_init)
            
        except Exception:
            missx+=1
            continue
        
    x=numpy.asarray(rx)
    y=numpy.asmatrix(ry) # Matrify
    
    def featureScaling(x): # Normalization of all data
        for i in range(17):
            m=x[:,[i]].mean()
            std=x[:,[i]].std()
            for j in range(len(x)-1):
                x[j][i]=(x[j][i]-m)/math.pow(std,2)
        return x
    
    x=numpy.matrix(featureScaling(x))
    allData=[x,y] # Return value
    print("Done: {}%".format(missx/len(raw)*100))
    return allData

class linrg(object):
    '''Use for linear regression, including normal equation and graident decent
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
        result=inv(self.allData[0].getT()*self.allData[0])*self.allData[0].getT()*self.allData[1]
        return result
    def normal_specificData(self,dataSet):
        '''Normal equation for specific data set within <class linrg>
        Returns a result matrix'''
        x,y=dataSet[0],dataSet()[1]
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
    
    def GradientDecent(self,alpha=0.0000000001,times=100):
        '''Gradient decent for data from getLearnData() in <class linrg>
        :alpha: int -> learning rate of gradient decent, default 0.0000000001
        :times: int -> times of iteration, default 100
        Returns a result matrix'''
        x,y=self.getLearnData()[0],self.getLearnData()[1] # Get x & y matrix
        theta=numpy.matrix((math.sqrt(x.std())*numpy.random.randn(18,1)+x.mean())/100) # Initialize theta
        temp=theta
        J=[0]*times # Initialize cost function
        iteration=[i for i in range(1,times)] # Initialize iteration times
        for i in range(times):
            # theta j := theta j + alpha*(y-h(x))*x
            # temp=theta+alpha*numpy.sum((y-numpy.dot(x,theta))*x.getT())/2532
            # Main loop
            # Simultaneously update theta
            for j in range(18):
                temp[j]=theta[j]+alpha*numpy.sum((y-numpy.dot(x,theta))*x[:,j].getT())/2532            
            J[i]=0.5*numpy.sum(numpy.power((y-numpy.dot(x,theta)),2)) # Cost function update
            theta=temp
            if J[i]==J[i-1]:
                break
        return theta
    
    def testModel(self):
    '''Testing function
    Automatically get data and perform both normal equation and gradient decent
    Calculate RMSE of two methods, and give RMSE values'''
        data=self.getDevelopData() # Get develop data
        xt,y=data[0],data[1]
        r=normal_specificData(self.getDevelopData) # Get result using normal equation
        ytn=xt*r # Estimated y matrix
        RMSENormal=round(numpy.sqrt(numpy.power((ytn-y),2).mean()),3) # RMSE value for normal equation
        r=test.GradientDecent(0.0000000001,100)
        ytg=xt*r
        RMSEGrad=round(numpy.sqrt(numpy.power((ytg-y),2).mean()),3) # RMSE value for gradient decent
        print("="*27+"Testing with RMSE"+"="*27)
        print("Normal equation: RMSE="+str(RMSENormal)+" "*5+"|"+" "*5+"Gradient decent: RMSE="+str(RMSEGrad))
        print("="*71)
        
    def draw(self): # Not done yet
        x,y=self.getLearnData()[0],self.getLearnData()[1]
        price=numpy.array(y.getT())
        size=numpy.array(x[:,2].getT())
        year=numpy.array(x[:,-1].getT())
        import matplotlib.pyplot as plt
        ax=plt.axes(projection='3d')
        ax.scatter3D(price,size,year)
        plt.show()

def Init():
    '''User connection function
    Ask for user's features and gives back results of estimated price of both normal equation and gradient decent'''
    if os.access('result.txt', os.F_OK) and os.access('result.txt', os.R_OK):
        pass
    else:
        getData()
    global user
    user=[int(input("How many bedrooms: ")),int(input("How many livingrooms: ")),float(input("Size of the house in m2: ")),input("Direction of the rooms: "),
          input("Furnishing status: "),input("Elevator: "),input("Floor level: "),input("Year of built: ")] # Ask for user's feature and store in a list
    test=linrg() # Initialize linear regression
    r_normal=test.normal_learnData()
    r_grad=test.GradientDecent(0.0000000001,100)
    print("="*24+"User house price calculation"+"="*24)
    print("-"*20+"Result"+"-"*20)
    data=dataWash(user)
    r1=r_normal*data # Estimated price using normal equation
    r2=r_grad*data # Estimated price using gradient decent
    print("Estimated house price: "+r/10+"k RMB")
    print("="*27+"User house price calculation"+"="*27)
          
    



    
