p = [1,2,5,6] #Elements
w= [2,3,4,5] #Weights
tw = 8 #Total weights

def knapsack(tw,w,p,ind,we,pr):
    print(we,pr)
    if ind >= len(w):
        return pr
    if we >= tw:
        return pr
    a= 0
    if we + w[ind] <= tw:    
        a = knapsack(tw,w,p,ind+1,we+w[ind],pr+p[ind])
    b = knapsack(tw,w,p,ind+1,we,pr)
    return max(a,b)

print(knapsack(tw,w,p,0,0,0))