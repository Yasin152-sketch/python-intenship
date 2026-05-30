def power (num):  
    tik = []
    for i in range (num):
        list = []
        for j in range(2):
            n = int (input("enter the number you want in the list"))
            list.append(n)
        print (list)   
        tik.append(list)
    return tik
