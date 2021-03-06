# -*- coding: utf-8 -*-
"""
Created on Fri May  4 15:52:40 2018

@author: wan_yifei

Question#1: You have two matrixs, how to move tge first matrix (move up, down, left and right) so that
the second matrix in the two matrixs matches most?
eg: M1: ([0,0,0], [0,1,0], [1,1,0])  M2([0,1,1], [0,1,1], [0,0,0]);
"""

import numpy as np

#1. input matrix and reshape
#m1, m2 = np.array([[0,0,0], [0,1,0], [1,1,0]]), np.array([[0,1,1], [0,1,1], [0,0,0]])
#m1, m2 = np.array([[0,0,0,1], [0,1,0,0], [1,1,0,0]]), np.array([[0,1,0,1], [0,1,1,0], [0,0,0,0]])
m1, m2 = np.random.binomial(1, 0.5, size = [10, 10]), np.random.binomial(1, 0.3, size = [10, 10])

def move(m1, m2):
    shape = m1.shape
    m1 = m1.reshape([m1.shape[0] * m1.shape[1], ])
    m2 = m2.reshape(m2.shape[0] * m2.shape[1], )
    
    #2. compare two matrix
    ind1 = list(np.where(m1 == 1))[0]           ## index of 1 in 1st matrix
    ind2 = list(np.where(m2 == 1))[0]
    
    if len(ind1) > len(ind2):
        n = len(ind2)
    else: 
        n = len(ind1)
    
    
    set1, set2 = set(ind1), set(ind2)
    start = list(set1 - (set1 & set2))        ## index of start point in !st matrix
    target = list(set2 - (set1 & set2))       ## index of final location
    start.sort()
    target.sort()

         
    try:                                      ## moving via exchange points
        k = 0
        for i in start:
            temp = m1[i]
            m1[i] = m1[target[k]]
            m1[target[k]] = temp
            k = k + 1
    except IndexError:
        print('length of start: %d and target: %d'%(len(start),len(target)))
        print('Moving is completed')
    else:
        print('Moving is completed')
    
# =============================================================================
#     #double check the result:    
#     ind1 = list(np.where(m1 == 1))[0]           
#     ind2 = list(np.where(m2 == 1))[0]
#     set1, set2 = set(ind1), set(ind2)
#     check = len(set1 & set2)
#     print(check == n)   
# =============================================================================
    finalm = m1.reshape(shape, order = 'F')
    origm = m2.reshape(shape, order = 'F')
    print('Most match of 1 is %d'%(n))
    print('\n')
    #print(m1f)
    print(finalm)
    print('\n')
    print(origm)
    return finalm, origm

move(m1,m2)
    
