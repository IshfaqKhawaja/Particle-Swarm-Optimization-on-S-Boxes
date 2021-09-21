#PSO_NL
import random as r
import timeit
import sys
import math
import datetime
from adjustment import adjustment
from nonlinearity import non_linearity
from Initial_population import initial_s_box,renyi_map
def PSO_NL():
    n=int(input("Size of n in nxn S Box : "))
    N=int(input("No of initial Population : "))
    iteration=int(input("No of iteration : "))
    #Intial Parameters:
    c=float(137.0)
    xr=float(0.1234)
    initial_x=xr
    xr = renyi_map(c,xr,100)
    Population=[[] for i in range(2*N)]
    #Generate Intial Population using Renyi Map:
    for i in range(N):
            temp,xr=initial_s_box(n,c,xr)
            Population[i] = temp
    #Population[r.randint(N//4,N)] = [5, 158, 203, 81, 21, 249, 133, 33, 189, 116, 245, 157, 12, 138, 92, 103, 193, 106, 99, 117, 40, 6, 90, 59, 60, 229, 34, 156, 100, 147, 146, 244, 80, 84, 181, 113, 78, 74, 139, 2, 29, 31, 13, 240, 114, 30, 26, 207, 51, 73, 167, 7, 62, 37, 161, 214, 192, 108, 115, 124, 144, 218, 96, 104, 255, 160, 246, 32, 243, 247, 145, 54, 39, 188, 190, 107, 199, 82, 41, 86, 47, 18, 126, 168, 230, 184, 45, 211, 204, 98, 233, 93, 48, 87, 105, 91, 221, 219, 242, 4, 102, 88, 97, 76, 95, 222, 148, 254, 38, 154, 186, 241, 149, 173, 185, 225, 72, 205, 232, 68, 101, 28, 163, 182, 231, 224, 52, 110, 25, 123, 251, 171, 220, 191, 36, 67, 136, 187, 24, 236, 217, 75, 253, 79, 55, 202, 109, 200, 151, 17, 228, 252, 141, 46, 119, 137, 210, 159, 195, 239, 61, 85, 174, 143, 16, 19, 77, 179, 71, 166, 43, 175, 197, 111, 162, 216, 150, 23, 164, 22, 57, 172, 118, 194, 50, 223, 129, 83, 20, 63, 27, 58, 49, 56, 153, 213, 53, 65, 15, 212, 125, 10, 165, 196, 155, 250, 237, 132, 135, 89, 178, 152, 238, 176, 170, 1, 142, 35, 177, 112, 209, 180, 206, 66, 121, 169, 208, 42, 44, 3, 0, 14, 8, 11, 127, 183, 94, 130, 215, 64, 128, 131, 198, 70, 120, 9, 134, 201, 248, 140, 234, 122, 227, 226, 69, 235]
    #Inclusion of this leads the algo towards convergence, this sbox is used in 8*8 only
    #Calculate Fitness:
    NL=[[0,0] for _ in range(2*N)]
    for  i in range(N):
            NL.append([non_linearity(Population[i]),i])
    
    #Sort on bases of fitness value i.e Non Linearity
    NL_Sorted=sorted(NL,key=lambda x:x[0],reverse=True)
    print("NL Before")
    for i in range(N):
        print(NL_Sorted[i])
    #Chose G_best and P_best
    G_Best=Population[NL_Sorted[0][1]]
    P_Best=Population.copy()#Initially P_best is individual Score
    #Select velocity parameter
    VEL=[[ 0 for _ in range(2**n)] for _ in range(N)]
    #Select a random weight
    w = 0.6
    start=timeit.default_timer()
    itr=iteration
    count=0
    flag1=0
    while iteration:
        iteration-=1
        xr = renyi_map(c,xr,100)
        c1=xr
        xr = renyi_map(c,xr,100)
        c2=xr
        xr = renyi_map(c,xr,100)
        r1=xr
        xr = renyi_map(c,xr,100)
        r2=xr
        NL=NL_Sorted.copy()
        for i in range(N):#For every Sbox
            temp=[]
            redundant_array=[]
            indices=[]
            flag=0
            for j in range(2**n):#For Each element in selected Sbox
                #Calculate Velocity using PSO formulla
                VEL[i][j]=math.ceil(w*VEL[i][j]+c1*r1*(P_Best[i][j]-Population[i][j])+c2*r2*(G_Best[j]-Population[i][j]))
                #If Velocity of element is negative or greater than 256 adjust it
                if VEL[i][j]<0:
                     VEL[i][j]=(VEL[i][j]+2**n)%(2**n)
                val=int((Population[i][j]+VEL[i][j])%2**n)
                #Check if value not already in temp, then we need to adjust it
                if val not in temp:
                    temp.insert(j,val)
                else:
                    flag=1
                    temp.insert(j,-1)
                    indices.append(j)
                    redundant_array.append(val)
            if flag==1:
                temp=adjustment(temp,redundant_array,indices,n)
                
            Population[N+i]=temp
        #Calculate fitness of generated population
        for i in range(N):
            NL_Sorted[N+i]=[non_linearity(Population[N+i]),N+i]
        #Sort Whole population
        NL_Sorted=sorted(NL_Sorted,key=lambda x:x[0],reverse=True)

        temp_population=[[] for _ in range(N)]
        #Select only best N candidates
        for i in range(N):
            temp_population[i]=Population[NL_Sorted[i][1]]
        Population[:N]=temp_population.copy()
        
        for i in range(N):
            NL_Sorted[i][1]=i
            NL_Sorted[N+i]=[0,0]
        #Change P_best of each candidate
        for i in range(N):
            if NL[i][0]<NL_Sorted[i][0]:
                P_Best[i]=Population[i]
        #Select G_best as First candidate of population
        G_Best=Population[0]
      
    stop=timeit.default_timer()    
    print("\n***************************************************************\n")
    print("NL After :")
    for i in range(N):
        print(NL_Sorted[i])
    print("Total time taken is:",stop-start)
if __name__=='__main__':
    PSO_NL()
   
