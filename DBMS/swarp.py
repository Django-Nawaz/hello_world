from time import time
import numpy as np
from random import randrange
import random
lpos = 100*[100*[0]]
rpos = 100*[100*[0]]
def create_matrix(m,n):
    mat = m*[n*[0]]
    for i in range(m):
        for j in range(n):
            mat = np.random.random_integers(5, size=(m,n))%2
            random.seed = time()
        random.seed = time()
    return mat
def display_matrix(mat,m,n):
    print(" ",end = '')
    for i in range(m):
        for j in range(n):
            print(mat[i][j]," | ",end = '')
            
        print("\n",end = ' ')
            
def solve(a,m,n):
    
    x = int(input("Emergency Concerned Lane"))
    ct = 0
    v = 10000*[2*[0]]
    for i in range(0,m):
        if a[i][x]==1:
            v[i][0] = 99
            ct+=1
        else:
            v[i][0] = 0
    while(ct>0):
        for i in range(m-1,0,-1):
            #if v[i][0] == 99:
            
                
            pass
            
    pass
def decission_matrix():
    pass

def test():
    a =int(input("Enter the Number of Lanes : "))
    b =int(input("Enter the numbers of rows of clusters :"))
    mat = create_matrix(a,b)
    display_matrix(mat,a,b)
test()
def main():
    lane_num = input("Input the lane_number")
    cluster_length = input("Enter the Cluster Length")
    
