p = [1,2,5,6]
w= [2,3,4,5]
tw = 8
def knapsack(p,w,tw):
    mat= []
    for j in range(len(w)+1):
        temp=[]
        for i in range(tw+1):
            temp.append(None)
        mat.append(temp)
    
    ind = 0
    while ind< (tw+1) :
        mat[0][ind] = 0
        ind += 1

    ind = 0
    while ind< (len(w) + 1) :
        mat[ind][0] = 0
        ind += 1
    #print(mat)
    item_no = 1
    while item_no < len(w)+1:
        bag_size =1
        while bag_size < tw + 1:
            if bag_size - w[item_no - 1] >= 0:
                #print(mat[item_no-1][bag_size - w[item_no - 1]] + p[item_no - 1],mat[item_no-1][bag_size])
                mat[item_no][bag_size] = max( mat[item_no-1][bag_size - w[item_no - 1]] + p[item_no - 1],mat[item_no-1][bag_size])
            else:
                mat[item_no][bag_size] = mat[item_no-1][bag_size]
                #mat[item_no-1][bag_size - w[item_no - 1]]
            bag_size += 1
        item_no += 1
    print(mat)
    return mat[len(w) ][tw]
print(knapsack(p,w,tw))