# task1 
def  fun(l , n) :
    res= []
    for i in range(len(l)) :
        for j in range(i+1,len(l)):
            if  ((l[i]+l[j])==n):
                res.append((l[i] , l[j]))
    
    return res
print(fun([1,2,3,4,5,6] ,6))

# task2
def freq(l) :
    r ={}
    for i in range(len(l)) :
        found =False
        for j in r :
            if(j ==l[i]):
                r[j] +=1
                found =True
                break
        if(found==False):
            r[l[i]] =1
    return r

print(freq([1,1,1,2,3,4]))
# task2 easy soln
def freq2(l):
    r= {}
    for i in range(len(l)):
        if( r.get(l[i])):
            r[l[i]] +=1
        else :
            r[l[i]]=1
    return r

print(freq2([1,2,3,1,2,3,3]))


def freq3(l):
    r = {i:l.count(i) for i in (l)}
    return r  
 
print(freq3([1,2,1,1,2]))

   
# a = {1:3 ,2:1}
# print (a.get(1))



    
        

        
        
