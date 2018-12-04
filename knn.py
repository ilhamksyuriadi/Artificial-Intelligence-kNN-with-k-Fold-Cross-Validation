# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 11:32:59 2018

@author: ilhamksyuriadi
"""

import csv
import math

#Function for load the data
def LoadData(locFile):
    with open(locFile) as csv_file:
        data = []
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                data.append([row[1],row[2],row[3],row[4],row[5],row[6]])
            line_count += 1
        return data

#Function to calculate the euclidean distance
def Euclidean(data1,data2):
    result = (float(data1[0])-float(data2[0]))**2 + (float(data1[1])-float(data2[1]))**2 + (float(data1[2])-float(data2[2]))**2 + (float(data1[3])-float(data2[3]))**2 + (float(data1[4])-float(data2[4]))**2
    return math.sqrt(result)

#Function for the implementation of k-Nearest Neighbour
def Knn(k,train,test):
    predict = []
    for i in range(0,len(test)):
        label = [0,0,0,0]#put label 0,1,2,3 as an index 0,1,2,3 on list label
        distance = []
        for j in range(0,len(train)):
            hasil = Euclidean(test[i],train[j])
            distance.append([hasil,train[j][5]])
        distance.sort()#sorting from small
        for l in range(0,k):#do the loop as much as k value (7)
            if distance[l][1] == "0":
                label[0] += 1
            elif distance[l][1] == "1":
                label[1] += 1
            elif distance[l][1] == "2":
                label[2] += 1
            elif distance[l][1] == "3":
                label[3] += 1
        predict.append(label.index(max(label)))
    return predict

#Load the data
locFile = "Data.csv"
dataTrain = LoadData(locFile)

#divide data for k-fold cross validation with k = 4
#train 0 - 600, test 601-800
dataTrain1 = dataTrain[0:600]
dataTest1 = dataTrain[600:800]

#train 0 - 400 dan 601 - 800, test 401-600
dataTrain2 = dataTrain[0:400]+dataTrain[600:800]
dataTest2 = dataTrain[400:600]

#train 0 - 200 dan 401 - 800, test 201 - 600
dataTrain3 = dataTrain[0:200]+dataTrain[400:800]
dataTest3 = dataTrain[200:400]

#train 201 - 800, test 0-200
dataTrain4 = dataTrain[200:800]
dataTest4 = dataTrain[0:200]

#use k = 7 for kNN
k = 7 #change here for try another value of k

#do the classification to the rest divided data
predict1 = Knn(k,dataTrain1,dataTest1)
predict2 = Knn(k,dataTrain2,dataTest2)
predict3 = Knn(k,dataTrain3,dataTest3)
predict4 = Knn(k,dataTrain4,dataTest4)

#collect all of classification result
predict = predict4 + predict3 + predict2 + predict1

count = 0
for i in range(0,len(predict)):
    if str(predict[i]) == dataTrain[i][5]:
        count +=1
print("K :", k)
print("Accuracy : ", round(count/len(predict)*100,4),'%')


