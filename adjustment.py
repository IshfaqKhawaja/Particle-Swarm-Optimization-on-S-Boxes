

def adjustment(temp,redundant_array,indices,n):
    #print("In adjustment")
    #print("temp",temp)
    missing_list=[]
    for i in range(2**n):
        if i not in temp and i not in redundant_array:
            missing_list.append(i)
    #missing_list.sort(reverse=True)
    if len(missing_list)==len(redundant_array):
        #print(missing_list)
        k=0
        for j in indices:
            if temp[j]==-1:
                temp[j]=missing_list[k]
                k+=1
    if len(set(temp))==len(temp):
        #print("filled",temp)    
        return temp

    
