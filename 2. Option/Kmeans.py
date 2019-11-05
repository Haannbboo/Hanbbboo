import random
import matplotlib.pyplot as plt
import numpy as np
import time

class KMeans():

    def __init__(self, k=1):

        self.__k = k
        self.__data = None  
        self.__pointCenter = None 
        self.__result = []     
        for i in range(k):
            self.__result.append([])  


    def fit(self, data, threshold, times=100):

        self.__data = data  
        self.randomCenter() 
        centerDistance = self.calPointCenterDistance(self.__pointCenter, self.__data)  

        i = 0
        for temp in centerDistance:
            index = np.argmin(temp) 
            self.__result[index].append(self.__data[i]) 
            i += 1
        
        oldCenterPoint = self.__pointCenter
        newCenterPoint = self.calNewPointCenter(self.__result)

        while np.sum(np.sum((oldCenterPoint -  newCenterPoint)**2, axis=1)**0.5)/self.__k > threshold:
            times -= 1
            result = []
            for i in range(self.__k):
                result.append([])

            oldCenterPoint = newCenterPoint
            centerDistance = self.calPointCenterDistance(newCenterPoint, self.__data)

            i = 0
            for temp in centerDistance:
                index = np.argmin(temp)
                result[index].append(self.__data[i]) 
                i += 1
                

            newCenterPoint = self.calNewPointCenter(result)

            self.__result = result
            
        self.__pointCenter = newCenterPoint
        return newCenterPoint, self.__result
        
        
    def calPointCenterDistance(self, center, data):
        centerDistance = []
        flag = False
        for temp in data:
            centerDistance.append([np.sum((center - temp) ** 2, axis=1) ** 0.5])#使用numpy广播
            
        return np.array(centerDistance)
        

    def calNewPointCenter(self, result):
        newCenterPoint = None
        flag = False
        for temp in result:
            temps = np.array(temp)
            point = np.mean(temps, axis=0) 
            if not flag:
                newCenterPoint = np.array([point])
                flag = True
            else:
                newCenterPoint = np.vstack((newCenterPoint, point))
            return newCenterPoint


    def randomCenter(self):
        if not self.__pointCenter:
            index = random.randint(0, len(self.__data) - 1)
            self.__pointCenter = np.array([self.__data[index]])
            
        while len(self.__pointCenter) < self.__k:
            index = random.randint(0, len(self.__data) - 1)
            if self.__data[index] not in self.__pointCenter:
                self.__pointCenter = np.vstack((self.__pointCenter, self.__data[index]))


if __name__ == "__main__":

    data = np.random.randint(0, 100, 200000).reshape(100000, 2)

    startTime = time.time()
    kmeans = KMeans(k=5)
    centerPoint, result = kmeans.fit(data, 0.0001)
    
    print(time.time() - startTime)
    print(centerPoint)
    plt.plot()
    plt.title("KMeans Classification")
    i = 0
    tempx = []
    tempy = []
    color = []
    for temp in result:
        temps = [[temp[x][i] for x in range(len(temp))] for i in range(len(temp[0]))]
        color += [i] * len(temps[0])
        tempx += temps[0]
        tempy += temps[1]

        i += 2

    plt.scatter(tempx, tempy, c=color, s=30)
    plt.show()
