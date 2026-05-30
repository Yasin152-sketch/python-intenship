def check(tik) :
    re = [2, 4]
    count = 0
    for i in range (len(tik)):
        for j in range (len(tik[i])):
            for k in range (len(re)):
                if tik[i][j] == re[k]:
                   count +=1 
    return count
